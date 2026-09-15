#!/usr/bin/env python3
"""
Zero-Dependency REST Microservice Adapter for swift-apple-ecosystem-suite
Port: 8767
Features: OpenAPI 3.1, Interactive Swagger UI (/docs), APNs Push, SwiftData Sync
Author: Russell Alan Powers
"""
import sys
import os
import json
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

SOLUTION_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SOLUTION_ROOT))

from src.core import CoreEngine

PORT = int(os.environ.get("SBB_APPLE_PORT", 8767))

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [AppleAdapter] %(message)s")
logger = logging.getLogger("AppleAdapter")

engine = CoreEngine()

OPENAPI_SPEC = {
    "openapi": "3.1.0",
    "info": {
        "title": "SBB Solution 07: Native macOS & iOS SwiftUI Suite API",
        "description": "Apple platform integration microservice providing APNs Push Notification dispatching, CoreData/SwiftData offline delta synchronization, Combine reactive event streaming, and SwiftUI component generation.",
        "version": "1.0.0",
        "contact": {"name": "Russell Alan Powers", "email": "russell@sovereignbizbox.io"}
    },
    "servers": [{"url": f"http://127.0.0.1:{PORT}", "description": "Local Apple Gateway"}],
    "paths": {
        "/healthz": {
            "get": {
                "summary": "Service Health & Platform Status",
                "responses": {"200": {"description": "Health status", "content": {"application/json": {"schema": {"type": "object"}}}}}
            }
        },
        "/api/v1/apns/dispatch": {
            "post": {
                "summary": "FEAT-007-05: Dispatch Apple Push Notification (APNs)",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "device_token": {"type": "string", "example": "740f4707be531f182e4bb85e"},
                                    "title": {"type": "string", "example": "Critical Edge Alert"},
                                    "body": {"type": "string", "example": "Raspberry Pi CPU Temp reached 85°C"},
                                    "badge": {"type": "integer", "example": 1},
                                    "sound": {"type": "string", "example": "default"}
                                },
                                "required": ["device_token", "title"]
                            }
                        }
                    }
                },
                "responses": {"200": {"description": "APNs dispatch result"}}
            }
        },
        "/api/v1/swiftdata/sync": {
            "post": {
                "summary": "FEAT-007-02: Synchronize SwiftData / CoreData Offline Delta",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "client_sync_token": {"type": "string", "example": "STOKEN-initial"},
                                    "records": {"type": "array", "items": {"type": "object"}}
                                }
                            }
                        }
                    }
                },
                "responses": {"200": {"description": "Delta commit summary"}}
            }
        },
        "/api/v1/menubar/status": {
            "get": {
                "summary": "FEAT-007-03: Get macOS Menu Bar Daemon Heartbeat",
                "responses": {"200": {"description": "Daemon menu status"}}
            }
        },
        "/api/v1/combine/publish": {
            "post": {
                "summary": "FEAT-007-04: Publish Reactive Combine Event",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "event_type": {"type": "string", "example": "DEVICE_PAIRED"},
                                    "data": {"type": "object"}
                                },
                                "required": ["event_type"]
                            }
                        }
                    }
                },
                "responses": {"200": {"description": "Event broadcast confirmation"}}
            }
        },
        "/api/v1/swiftui/render": {
            "post": {
                "summary": "FEAT-007-01: Generate Native SwiftUI View Code",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "view_type": {"type": "string", "example": "MetricCard"},
                                    "props": {"type": "object"}
                                }
                            }
                        }
                    }
                },
                "responses": {"200": {"description": "Generated Swift code snippet"}}
            }
        }
    }
}

SWAGGER_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>SBB Solution 07 - Swift Apple Ecosystem API</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css" />
  <style>body {{ margin: 0; padding: 0; background: #fafafa; }} .topbar {{ display: none; }}</style>
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    window.onload = () => {{
      window.ui = SwaggerUIBundle({{
        url: '/openapi.json',
        dom_id: '#swagger-ui',
        deepLinking: true,
        presets: [SwaggerUIBundle.presets.apis]
      }});
    }};
  </script>
</body>
</html>"""

class AppleHandler(BaseHTTPRequestHandler):
    def _send_json(self, status: int, data: dict):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ("/healthz", "/health", "/"):
            self._send_json(200, engine.health_check())
        elif self.path == "/openapi.json":
            self._send_json(200, OPENAPI_SPEC)
        elif self.path == "/docs":
            body = SWAGGER_HTML.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/api/v1/menubar/status":
            self._send_json(200, engine.menubar.get_status())
        else:
            self._send_json(404, {"error": "Not Found"})

    def do_POST(self):
        auth_header = self.headers.get("X-SBB-Auth")
        if auth_header != os.environ.get("SBB_SHARED_SECRET", "sbb_local_dev_secret_2026"):
            self.send_response(401)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "Unauthorized"}')
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8") if length > 0 else "{}"
        try:
            data = json.loads(body)
        except Exception:
            data = {}

        # Universal Action Gateway for n8n custom node
        if self.path in ("/api/v1/execute", "/"):
            action = data.get("action", "render_swiftui_views")
            payload = data.get("payload", {})
            self._send_json(200, engine.execute_action(action, payload))
            return

        if self.path == "/api/v1/apns/dispatch":
            dev = data.get("device_token", "default_device")
            title = data.get("title", "SBB Notification")
            msg = data.get("body", "")
            badge = int(data.get("badge", 1))
            sound = data.get("sound", "default")
            self._send_json(200, engine.apns.dispatch(dev, title, msg, badge, sound))
        elif self.path == "/api/v1/swiftdata/sync":
            token = data.get("client_sync_token", "INITIAL")
            records = data.get("records", [])
            self._send_json(200, engine.sync.sync_records(token, records))
        elif self.path == "/api/v1/combine/publish":
            etype = data.get("event_type", "GENERIC_COMBINE_EVENT")
            payload = data.get("data", data)
            self._send_json(200, engine.combine.publish_event(etype, payload))
        elif self.path == "/api/v1/swiftui/render":
            vtype = data.get("view_type", "MetricCard")
            props = data.get("props", {})
            self._send_json(200, engine.swiftui.render_view(vtype, props))
        else:
            self._send_json(404, {"error": "Not Found"})

    def log_message(self, format, *args):
        pass

def run():
    server = HTTPServer(("0.0.0.0", PORT), AppleHandler)
    logger.info("Swift Apple Suite Microservice listening on http://0.0.0.0:%d (Swagger UI at /docs)", PORT)
    server.serve_forever()

if __name__ == "__main__":
    run()
