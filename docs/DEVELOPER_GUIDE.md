# Swift & Apple Multi-Platform Ecosystem Suite — Developer Guide

## 1. Quick Start

### Prerequisites
- Python 3.10+ (Zero external dependencies for backend adapter)
- Xcode 15+ / Swift 5.9+ (For compiling native Apple targets)
- macOS Sonoma or newer (Recommended for local menu bar testing)

### Installation & Standalone Run
```bash
cd solutions/swift-apple-ecosystem-suite
python3 -m unittest discover tests/
python3 n8n/webhook_adapter.py
```
The microservice starts on `http://127.0.0.1:8767` with interactive Swagger UI available at `http://127.0.0.1:8767/docs`.

## 2. CLI Tool Reference

The suite includes a multi-command CLI (`src/cli.py`):

```bash
# Dispatch an APNs Push Notification
python3 src/cli.py apns --token device_tok_123 --title "Critical Warning" --body "Temp > 82C"

# Synchronize SwiftData Delta Changes
python3 src/cli.py sync --client client-ios-01 --delta '{"items": [{"id": 1, "value": "val"}]}'

# Query macOS Menu Bar Status
python3 src/cli.py menubar

# Publish an Event to the Combine Stream
python3 src/cli.py publish-event --topic "iot.alert" --payload '{"node": "pi-01", "temp": 85.5}'
```

## 3. OpenAPI / REST Endpoints Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Microservice liveness and active module status |
| `GET` | `/docs` | Interactive Swagger UI API playground |
| `GET` | `/openapi.json` | OpenAPI 3.1 schema specification |
| `POST` | `/api/v1/swiftui/render` | Render parametric SwiftUI view code |
| `POST` | `/api/v1/swiftdata/sync` | Process offline delta synchronization |
| `POST` | `/api/v1/menubar/status` | Read or update macOS menu bar daemon status |
| `POST` | `/api/v1/combine/publish` | Publish event to reactive stream bus |
| `POST` | `/api/v1/apns/dispatch` | Transmit push notification to device token |

## 4. Native Swift Integration

To include this suite in your Xcode project, link the provided `templates/Package.swift` or copy `templates/ContentView.swift` and `templates/TelemetryItem.swift` into your app target.
