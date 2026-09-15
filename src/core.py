"""
Unified Apple Platform Ecosystem Coordinator
Author: Russell Alan Powers
Domain: Apple Ecosystem & Mobile
"""
from typing import Dict, Any
from .apns_dispatcher import APNSDispatcher
from .swiftdata_sync import SwiftDataSyncLayer
from .menubar_worker import MenuBarWorker
from .combine_stream import CombineStreamBus
from .swiftui_components import SwiftUIComponentRenderer

class CoreEngine:
    def __init__(self):
        self.apns = APNSDispatcher()
        self.sync = SwiftDataSyncLayer()
        self.menubar = MenuBarWorker()
        self.combine = CombineStreamBus()
        self.swiftui = SwiftUIComponentRenderer()

    def execute_action(self, action: str, payload: Dict[str, Any] = None) -> Dict[str, Any]:
        payload = payload or {}
        act = action.strip().lower()

        # FEAT-007-01: SwiftUI Reusable Component Library
        if act in ("render_swiftui_views", "render_swiftui", "swiftui.render", "swiftui_render"):
            view_type = payload.get("view_type") or payload.get("viewType") or "MetricCard"
            props = payload.get("props") or payload
            return self.swiftui.render_view(view_type, props)
        elif act in ("list_swiftui_views", "swiftui.list", "swiftui_list"):
            return self.swiftui.list_supported_views()

        # FEAT-007-05: APNs Dispatcher
        elif act in ("dispatch_apns", "apns_dispatch", "apns.send"):
            device = payload.get("device_token") or payload.get("device") or "default_token"
            title = payload.get("title", "SBB Notification")
            body = payload.get("body", "")
            badge = int(payload.get("badge", 1))
            sound = payload.get("sound", "default")
            return self.apns.dispatch(device, title, body, badge, sound)

        # FEAT-007-02: SwiftData Sync
        elif act in ("sync_swiftdata", "swiftdata_sync", "swiftdata.sync"):
            token = payload.get("client_sync_token") or payload.get("token") or "INITIAL"
            records = payload.get("records", [])
            return self.sync.sync_records(token, records)

        # FEAT-007-04: Combine Stream
        elif act in ("publish_combine_event", "combine_publish", "combine.publish"):
            etype = payload.get("event_type", "GENERIC_EVENT")
            data = payload.get("data") or payload
            return self.combine.publish_event(etype, data)

        # FEAT-007-03: MenuBar Status
        elif act in ("get_menubar_status", "menubar_status", "menubar.status"):
            return self.menubar.get_status()

        return {
            "success": False,
            "error": f"Unknown action '{action}' for swift-apple-ecosystem-suite",
            "supported_actions": [
                "render_swiftui_views", "list_swiftui_views",
                "dispatch_apns", "sync_swiftdata",
                "publish_combine_event", "get_menubar_status"
            ]
        }

    def health_check(self) -> Dict[str, Any]:
        return {
            "status": "HEALTHY",
            "service": "swift-apple-ecosystem-suite",
            "port": 8767,
            "platform": "Apple macOS & iOS",
            "menubar_status": self.menubar.status,
            "synced_records": len(self.sync._cloud_ledger),
            "events_streamed": len(self.combine._history),
            "version": "1.0.0"
        }
