// TelemetryItem.swift
// SwiftData Persistent Model for Sovereign Biz Box
import Foundation
import SwiftData

@Model
public final class TelemetryItem {
    @Attribute(.unique) public var id: String
    public var timestamp: Date
    public var topic: String
    public var value: Double
    public var isSynced: Bool

    public init(id: String = UUID().uuidString, timestamp: Date = Date(), topic: String, value: Double, isSynced: Bool = false) {
        self.id = id
        self.timestamp = timestamp
        self.topic = topic
        self.value = value
        self.isSynced = isSynced
    }
}