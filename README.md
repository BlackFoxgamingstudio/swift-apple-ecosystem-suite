# 🍎 Swift & Apple Multi-Platform Ecosystem Suite

[![CI](https://github.com/BlackFoxgamingstudio/swift-apple-ecosystem-suite/actions/workflows/ci.yml/badge.svg)](https://github.com/BlackFoxgamingstudio/swift-apple-ecosystem-suite/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Zero-Dependency](https://img.shields.io/badge/Dependencies-Standard%20Library-green.svg)](pyproject.toml)
[![OpenAPI 3.1](https://img.shields.io/badge/OpenAPI-3.1-orange.svg)](http://localhost:8767/openapi.json)
[![Swift 5.9+](https://img.shields.io/badge/Swift-5.9+-f05138.svg)](templates/Package.swift)

The **Swift & Apple Multi-Platform Ecosystem Suite** (`SOL-007`, Port `8767`) is the official Apple ecosystem integration suite for the Sovereign Biz Box platform. It connects iOS, macOS, iPadOS, watchOS, and visionOS applications with offline-first SwiftData synchronization, parametric SwiftUI components, lightweight macOS menu bar daemons, Combine event streams, and APNs push notification dispatchers.

---

## ⚡ Key Highlights
- **Parametric SwiftUI Components**: Generates clean, declarative SwiftUI views for cross-platform Apple applications.
- **Offline-First SwiftData Sync**: Deterministic delta journaling with Last-Write-Wins conflict resolution.
- **macOS Menu Bar Daemon**: Lightweight background worker (< 15MB) with system status item updates.
- **Combine Reactive Stream Bus**: Pub-sub event pipeline emulating Apple Combine framework semantics.
- **APNs Dispatch Gateway**: High-throughput Apple Push Notification service dispatcher.
- **Zero Third-Party Pip Dependencies**: Pure Python 3.10+ standard library backend.

---

## 🛠️ Micro-Tool Function Catalog (100-Fold Decomposition)

| Micro-Tool | Endpoint | CLI Subcommand | Domain |
|---|---|---|---|
| **SwiftUI View Generator** | `POST /api/v1/swiftui/render` | `swiftui` | UI Rendering |
| **SwiftData Delta Sync** | `POST /api/v1/swiftdata/sync` | `sync` | Offline Persistence |
| **macOS Menu Bar Status** | `POST /api/v1/menubar/status` | `menubar` | Background Daemon |
| **Combine Stream Publish** | `POST /api/v1/combine/publish` | `publish-event` | Reactive Event Stream |
| **APNs Push Dispatcher** | `POST /api/v1/apns/dispatch` | `apns` | Push Notifications |

---

## 🚀 Quick Start

```bash
# 1. Run unit test suite
python3 -m unittest discover tests/

# 2. Launch HTTP Microservice Adapter on port 8767
python3 n8n/webhook_adapter.py

# 3. View Interactive Swagger Documentation
open http://127.0.0.1:8767/docs
```

---

## 📦 Native Apple Client Integration

To integrate with your iOS or macOS Xcode project:
1. Copy `templates/Package.swift` into your SPM setup.
2. Add `templates/ContentView.swift` and `templates/TelemetryItem.swift` to your Swift source files.
3. Configure `APNS_BUNDLE_ID` in your `.env` file to match your App ID (`io.sovereignbizbox.companion`).

---

## 📜 License
MIT License. Developed for the Sovereign Biz Box autonomous platform ecosystem.
