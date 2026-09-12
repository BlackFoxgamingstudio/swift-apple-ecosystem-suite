# Swift & Apple Multi-Platform Ecosystem Suite — Architecture

## 1. Executive Summary
The **Swift & Apple Multi-Platform Ecosystem Suite** (`SOL-007`, Port `8767`) provides a native Apple integration bridge connecting iOS, macOS, iPadOS, watchOS, and visionOS client devices to the Sovereign Biz Box multi-agent platform. It combines offline-first CoreData/SwiftData delta synchronizers, parametric SwiftUI view generators, background menu bar daemons, Combine reactive event publishers, and Apple Push Notification service (APNs) dispatchers.

## 2. Subsystem Topology

```
+-----------------------------------------------------------------------------------+
|                        Swift & Apple Ecosystem Suite                              |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [FEAT-007-01: SwiftUI View Library] <---> [FEAT-007-02: SwiftData Sync Layer]    |
|   Parametric Code Rendering                 Offline Delta Journal & Tombstones    |
|   Dynamic Control Hierarchy                 Vector Clock Conflict Resolution      |
|             ^                                       ^                             |
|             |                                       |                             |
|  [FEAT-007-03: macOS Menu Bar Daemon] <-> [FEAT-007-04: Combine Stream Bus]      |
|   Low-Memory Status Bar Worker             Reactive Pipeline & Filtering          |
|   Local Cache Buffering                    Backpressure & Debounce Controls       |
|             ^                                       ^                             |
|             +-------------------+-------------------+                             |
|                                 |                                                 |
|                   [FEAT-007-05: APNs Notification Dispatcher]                    |
|                    Cryptographic Payload Signing & Silent Wakeups                 |
+-----------------------------------------------------------------------------------+
                                  |
                +-----------------+-----------------+
                |                                   |
        [HTTP / REST Gateway]              [n8n Workflow Canvas]
          Port 8767 FastAPI/BaseHTTP        wf-007-apple-suite
          Swagger UI /docs                   Topic: io.sovereignbizbox.apple.*
```

## 3. Core Modules & Contracts

### 3.1 SwiftUI Component Generator (FEAT-007-01)
- **File**: `src/swiftui_components.py`
- **Class**: `SwiftUIRenderer`
- **Specification**: Generates clean, idiomatic Swift 5.9+ SwiftUI code definitions dynamically based on platform telemetry models and agent states.

### 3.2 SwiftData / CoreData Delta Sync Layer (FEAT-007-02)
- **File**: `src/swiftdata_sync.py`
- **Class**: `SwiftDataSyncLayer`
- **Specification**: Manages bidirectional offline delta sync between Apple client device SQLite stores and the sovereign central cloud vault. Supports deterministic last-write-wins conflict resolution and deletion tombstones.

### 3.3 macOS Menu Bar Status Worker (FEAT-007-03)
- **File**: `src/menubar_worker.py`
- **Class**: `MenuBarDaemonWorker`
- **Specification**: Simulates and controls native `NSStatusItem` menu bar status icons, background heartbeats, and user quick-action popovers with minimal memory footprint (< 15MB).

### 3.4 Combine Reactive Event Stream Bus (FEAT-007-04)
- **File**: `src/combine_stream.py`
- **Class**: `CombineEventStream`
- **Specification**: Emulates Apple's Combine framework `PassthroughSubject` and `CurrentValueSubject` patterns in standard Python, supporting subscriber callbacks, operators, and backpressure buffering.

### 3.5 Apple Push Notification (APNs) Dispatcher (FEAT-007-05)
- **File**: `src/apns_dispatcher.py`
- **Class**: `APNsDispatcher`
- **Specification**: Dispatches HTTP/2 JWT-signed push notification alerts, badge updates, and background silent sync wakeups to iOS and macOS clients.
