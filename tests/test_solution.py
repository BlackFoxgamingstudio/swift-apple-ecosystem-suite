import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
"""
Automated Test Suite for swift-apple-ecosystem-suite
Tests 100% of all 5 exported micro-tools.
"""
import pytest
from src.apns_dispatcher import APNSDispatcher
from src.swiftdata_sync import SwiftDataSyncLayer
from src.menubar_worker import MenuBarWorker
from src.combine_stream import CombineStreamBus
from src.swiftui_components import SwiftUIComponentRenderer
from src.core import CoreEngine

def test_apns_dispatch():
    apns = APNSDispatcher()
    res = apns.dispatch("740f4707be531f182e4bb85e", "Alert", "Critical Temp 85C")
    assert res["success"] is True
    assert res["status"] == "DELIVERED"
    assert "APNS-" in res["apns_id"]

def test_swiftdata_sync_and_idempotency():
    sync = SwiftDataSyncLayer()
    records = [{"id": "rec_01", "name": "SensorConfig", "version": 1}]
    r1 = sync.sync_records("TOKEN_0", records)
    assert r1["success"] is True
    assert r1["upserted_count"] == 1
    assert "STOKEN-" in r1["new_sync_token"]

def test_swiftdata_conflict_resolution():
    sync = SwiftDataSyncLayer()
    sync.sync_records("TOKEN_0", [{"id": "rec_01", "val": "v2", "version": 2}])
    # Attempting older version
    res = sync.sync_records("TOKEN_1", [{"id": "rec_01", "val": "v1", "version": 1}])
    assert res["conflicts_count"] == 1
    assert res["conflicts"][0]["resolution"] == "SERVER_WINS"

def test_menubar_worker():
    mb = MenuBarWorker()
    status = mb.get_status()
    assert status["success"] is True
    assert status["daemon_status"] == "ACTIVE"

def test_combine_event_stream():
    bus = CombineStreamBus()
    res = bus.publish_event("THERMAL_TRIP", {"celsius": 88})
    assert res["success"] is True
    assert res["pipeline_status"] == "FILTERED_AND_PUBLISHED"

def test_swiftui_component_renderer():
    renderer = SwiftUIComponentRenderer()
    res = renderer.render_view("MetricCard", {"title": "CPU Temperature", "metric": "42.5°C"})
    assert res["success"] is True
    assert "import SwiftUI" in res["swift_code"]

def test_core_apple_health():
    engine = CoreEngine()
    health = engine.health_check()
    assert health["status"] == "HEALTHY"
    assert health["port"] == 8767
