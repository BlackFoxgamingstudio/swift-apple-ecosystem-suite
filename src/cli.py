#!/usr/bin/env python3
"""
CLI Invocation Harness for swift-apple-ecosystem-suite
Author: Russell Alan Powers
"""
import sys
import json
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.core import CoreEngine

def main():
    parser = argparse.ArgumentParser(description="SBB Swift Apple Ecosystem Suite CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    subparsers.add_parser("health", help="Check service health")

    apns_p = subparsers.add_parser("apns", help="Dispatch Apple Push Notification")
    apns_p.add_argument("--device", type=str, required=True, help="Device token")
    apns_p.add_argument("--title", type=str, required=True, help="Alert title")
    apns_p.add_argument("--body", type=str, default="", help="Alert body")

    sync_p = subparsers.add_parser("sync", help="Synchronize SwiftData records")
    sync_p.add_argument("--token", type=str, default="INITIAL_TOKEN", help="Client sync token")
    sync_p.add_argument("--records", type=str, default="[]", help="JSON array of records")

    subparsers.add_parser("menubar", help="Check menu bar daemon status")

    evt_p = subparsers.add_parser("publish-event", help="Publish Combine stream event")
    evt_p.add_argument("--type", type=str, required=True, help="Event type")
    evt_p.add_argument("--data", type=str, default="{}", help="Event data JSON")

    # FEAT-007-01: SwiftUI Component Library
    swiftui_p = subparsers.add_parser("render-swiftui", help="FEAT-007-01: Render a SwiftUI reusable component")
    swiftui_p.add_argument("--view-type", type=str, default="MetricCard",
                           help="View type: MetricCard, NavigationLink, TabView, ListRow, AlertBanner, ProgressRing, ActionButton, ChartCard")
    swiftui_p.add_argument("--props", type=str, default="{}", help="JSON props: title, metric, accent_color, subtitle, action_label")

    subparsers.add_parser("list-swiftui-views", help="FEAT-007-01: List all supported SwiftUI component types")

    args = parser.parse_args()
    engine = CoreEngine()

    if args.command == "health" or not args.command:
        print(json.dumps(engine.health_check(), indent=2))
    elif args.command == "apns":
        res = engine.apns.dispatch(args.device, args.title, args.body)
        print(json.dumps(res, indent=2))
    elif args.command == "sync":
        records = json.loads(args.records)
        res = engine.sync.sync_records(args.token, records)
        print(json.dumps(res, indent=2))
    elif args.command == "menubar":
        print(json.dumps(engine.menubar.get_status(), indent=2))
    elif args.command == "publish-event":
        data = json.loads(args.data)
        res = engine.combine.publish_event(args.type, data)
        print(json.dumps(res, indent=2))
    elif args.command == "render-swiftui":
        props = json.loads(args.props)
        res = engine.swiftui.render_view(args.view_type, props)
        print(json.dumps(res, indent=2))
    elif args.command == "list-swiftui-views":
        res = engine.swiftui.list_supported_views()
        print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
