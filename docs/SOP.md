# Swift & Apple Multi-Platform Ecosystem Suite — Standard Operating Procedures (SOP)

## SOP-AP-001: APNs Auth Key (.p8) Deployment
1. Log in to Apple Developer Portal (`developer.apple.com`).
2. Generate an APNs Authentication Key (.p8 file) under Certificates, Identifiers & Profiles.
3. Record the 10-character Key ID and Team ID.
4. Save key file securely to `secrets/AuthKey_APNS.p8` with `chmod 600`.
5. Populate environment variables in `.env` and n8n variable registry.

## SOP-AP-002: Menu Bar Worker Diagnostic
1. Check menu bar daemon memory usage:
   ```bash
   ps aux | grep -i menubar
   ```
2. Query health status endpoint: `curl http://127.0.0.1:8767/api/v1/menubar/status`.
3. If hung, restart worker gracefully via `python3 src/cli.py menubar --action restart`.
