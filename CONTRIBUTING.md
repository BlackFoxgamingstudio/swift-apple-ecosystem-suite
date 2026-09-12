# Contributing to Swift & Apple Multi-Platform Ecosystem Suite

We welcome contributions from Apple, iOS, and macOS developers worldwide!

## Guidelines
1. **Idiomatic Swift**: All client code templates must conform to modern Swift 5.9+ and SwiftUI guidelines.
2. **Offline-First Resilience**: Always assume network connectivity may be intermittent. Ensure SwiftData deltas persist locally before syncing.
3. **Zero Python Dependencies**: Backend adapter must remain pure Python standard library.

## Pull Request Workflow
1. Fork repository and create a feature branch (`feat/your-feature`).
2. Run test suite: `pytest tests/ -v`.
3. Submit PR against `main` branch.
