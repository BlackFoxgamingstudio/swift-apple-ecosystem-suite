# Sovereign Swift Apple Ecosystem Suite (`swift-apple-ecosystem-suite`)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![OpenAPI 3.1](https://img.shields.io/badge/OpenAPI-3.1.0-brightgreen.svg)](/openapi.json)
[![Swagger UI](https://img.shields.io/badge/Swagger_UI-Port_8767-blue.svg)](http://localhost:8767/docs)

Native macOS and iOS SwiftUI offline-first architecture microservice featuring:
- **Apple Push Notification (APNs) Dispatcher**: Direct APNs alert dispatching with badge and sound payload formatting.
- **SwiftData / CoreData Sync Layer**: Offline-first delta synchronization with deterministic version-based conflict resolution.
- **macOS Menu Bar Worker**: Native AppKit/SwiftUI background daemon status and heartbeat.
- **Combine Reactive Event Bus**: Real-time event pipeline publisher for multi-subscriber architectures.
- **SwiftUI Component Generator**: Parametric Swift source generator producing production-grade SwiftUI view structures.

## Microservice API
- **Swagger UI**: [http://localhost:8767/docs](http://localhost:8767/docs)
- **OpenAPI 3.1**: [http://localhost:8767/openapi.json](http://localhost:8767/openapi.json)
- **Health Check**: `GET http://localhost:8767/healthz`
