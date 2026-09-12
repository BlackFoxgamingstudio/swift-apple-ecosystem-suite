import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.apns_dispatcher import APNSDispatcher
from src.swiftdata_sync import SwiftDataSyncLayer
from src.menubar_worker import MenuBarWorker
from src.combine_stream import CombineStreamBus
from src.swiftui_components import SwiftUIComponentRenderer
from src.core import CoreEngine

class TestAppleSuiteSolution(unittest.TestCase):
    def test_apns_dispatch(self):
        apns = APNSDispatcher()
        res = apns.dispatch("740f4707be531f182e4bb85e", "Alert", "Critical Temp 85C")
        self.assertTrue(res["success"])
        self.assertEqual(res["status"], "DELIVERED")
        self.assertIn("APNS-", res["apns_id"])

    def test_swiftdata_sync_and_idempotency(self):
        sync = SwiftDataSyncLayer()
        records = [{"id": "rec_01", "name": "SensorConfig", "version": 1}]
        r1 = sync.sync_records("TOKEN_0", records)
        self.assertTrue(r1["success"])
        self.assertEqual(r1["upserted_count"], 1)
        self.assertIn("STOKEN-", r1["new_sync_token"])

    def test_swiftdata_conflict_resolution(self):
        sync = SwiftDataSyncLayer()
        sync.sync_records("TOKEN_0", [{"id": "rec_01", "val": "v2", "version": 2}])
        res = sync.sync_records("TOKEN_1", [{"id": "rec_01", "val": "v1", "version": 1}])
        self.assertEqual(res["conflicts_count"], 1)
        self.assertEqual(res["conflicts"][0]["resolution"], "SERVER_WINS")

    def test_menubar_worker(self):
        mb = MenuBarWorker()
        status = mb.get_status()
        self.assertTrue(status["success"])
        self.assertEqual(status["daemon_status"], "ACTIVE")

    def test_combine_event_stream(self):
        bus = CombineStreamBus()
        res = bus.publish_event("THERMAL_TRIP", {"celsius": 88})
        self.assertTrue(res["success"])
        self.assertEqual(res["pipeline_status"], "FILTERED_AND_PUBLISHED")

    def test_swiftui_component_renderer(self):
        renderer = SwiftUIComponentRenderer()
        res = renderer.render_view("MetricCard", {"title": "CPU Temperature", "metric": "42.5°C"})
        self.assertTrue(res["success"])
        self.assertIn("import SwiftUI", res["swift_code"])

    def test_core_apple_health(self):
        engine = CoreEngine()
        health = engine.health_check()
        self.assertEqual(health["status"], "HEALTHY")
        self.assertEqual(health["port"], 8767)

if __name__ == "__main__":
    unittest.main()
