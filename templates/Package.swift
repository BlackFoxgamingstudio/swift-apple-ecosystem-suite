// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "SBBAppleEcosystemKit",
    platforms: [
        .iOS(.v17),
        .macOS(.v14),
        .watchOS(.v10),
        .visionOS(.v1)
    ],
    products: [
        .library(
            name: "SBBAppleEcosystemKit",
            targets: ["SBBAppleEcosystemKit"]),
    ],
    dependencies: [],
    targets: [
        .target(
            name: "SBBAppleEcosystemKit",
            dependencies: [],
            path: "Sources"
        ),
        .testTarget(
            name: "SBBAppleEcosystemKitTests",
            dependencies: ["SBBAppleEcosystemKit"],
            path: "Tests"
        ),
    ]
)