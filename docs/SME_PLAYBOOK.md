# Swift & Apple Multi-Platform Ecosystem Suite — SME Playbook

## 1. Role Definition & Scope
The Apple Ecosystem SME oversees client device fleet synchronizations, APNs cryptographic credential lifecycles, iOS App Store and macOS TestFlight build deployments, and offline storage consistency.

## 2. Operational Runbooks

### Runbook 01: APNs Token Expiration & Invalidation
**Symptoms**: Push notification delivery fails with `410 BadDeviceToken`.
**Procedure**:
1. Inspect APNs dispatch logs:
   ```bash
   curl http://127.0.0.1:8767/api/v1/apns/status?token=<TOKEN>
   ```
2. Mark the expired device token as inactive in the subscriber registry.
3. Prompt client app on next foreground launch to register for remote notifications via `UNUserNotificationCenter`.

### Runbook 02: SwiftData Delta Conflict Storm
**Symptoms**: High conflict count during client reconnect after extended offline mode.
**Procedure**:
1. Check delta conflict metrics:
   ```bash
   curl -X POST http://127.0.0.1:8767/api/v1/swiftdata/sync \
     -H "Content-Type: application/json" \
     -d '{"client_id":"diagnostics","deltas":[]}'
   ```
2. Validate that the deterministic Last-Write-Wins (LWW) timestamp rule resolved conflicts without data loss.
3. Verify client local cache against central vault ledger on port 8766.
