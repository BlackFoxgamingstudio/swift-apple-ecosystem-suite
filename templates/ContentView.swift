// ContentView.swift
// Sovereign Biz Box Native Apple Companion View
import SwiftUI

public struct SBBCompanionView: View {
    @State private var serverStatus: String = "Online"
    @State private var telemetryItems: [String] = ["Node 01: 42.1°C", "Node 02: 39.8°C"]

    public init() {}

    public var body: some View {
        NavigationStack {
            List {
                Section(header: Text("Infrastructure Status")) {
                    HStack {
                        Image(systemName: "circle.fill")
                            .foregroundColor(.green)
                        Text("SBB Central Mainframe")
                        Spacer()
                        Text(serverStatus)
                            .font(.caption)
                            .foregroundColor(.secondary)
                    }
                }

                Section(header: Text("Live Telemetry Feeds")) {
                    ForEach(telemetryItems, id: \.self) { item in
                        Text(item)
                    }
                }
            }
            .navigationTitle("SBB Sovereign Suite")
        }
    }
}