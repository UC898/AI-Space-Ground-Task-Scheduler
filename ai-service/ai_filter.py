# Simple domain keyword based AI filter

VALID_KEYWORDS = [
    "earth", "observation", "terrain", "surface", "imagery",
    "remote", "sensing", "geospatial", "topography",
    "vegetation", "ecosystem", "environment",

    "flood", "flooding", "inundation", "water", "overflow",
    "river", "basin", "watershed", "rainfall", "zone",

    "wildfire", "forest", "fire", "burn", "smoke",
    "heat", "thermal", "hotspot", "fireline",
    "deforestation", "reforestation", "spread",

    "agriculture", "agricultural", "crop", "farm", "harvest",
    "yield", "irrigation", "soil", "moisture",
    "fertility", "plantation", "cultivation", "land",

    "weather", "climate", "storm", "cyclone",
    "hurricane", "tornado", "monsoon", "wind",
    "temperature", "humidity", "pressure",
    "forecast", "prediction", "atmosphere", "path",

    "ocean", "sea", "marine", "coastal",
    "shoreline", "erosion", "wave", "tide",
    "salinity", "current", "coral", "reef",

    "glacier", "ice", "polar", "snow",
    "iceberg", "arctic", "antarctic",
    "melting", "freeze", "movement",

    "urban", "city", "infrastructure",
    "building", "road", "traffic",
    "transport", "construction",
    "expansion", "population",

    "pollution", "air", "quality",
    "emission", "carbon", "greenhouse",
    "contamination", "waste", "environmental",
    "index",

    "disaster", "damage", "assessment",
    "emergency", "response", "recovery",
    "hazard", "risk", "evacuation",
    "relief", "crisis",

    "search", "rescue", "survivor",
    "location", "tracking", "distress",
    "detection", "scanning",

    "defense", "security", "border",
    "surveillance", "reconnaissance",
    "military", "threat", "target",
    "patrol", "monitoring",

    "satellite", "telemetry", "health",
    "diagnostic", "payload", "orbit",
    "attitude", "navigation", "guidance",
    "uplink", "downlink", "check",
    "onboard", "routine",

    "mission", "spacecraft", "probe",
    "lander", "rover", "station",
    "deployment", "launch", "trajectory",

    "communication", "signal", "network",
    "bandwidth", "relay", "transmission",
    "broadcast", "connectivity",

    "ai", "artificial", "intelligence",
    "machine", "learning", "training",
    "retraining", "inference", "model",
    "classification", "segmentation",
    "analytics", "analysis",

    "data", "processing", "pipeline",
    "compression", "aggregation",
    "storage", "streaming", "optimization",

    "compute", "computation", "workload",
    "task", "scheduling", "resource",
    "allocation", "execution",

    "node", "cluster", "load",
    "balancing", "latency", "performance",
    "throughput", "availability",

    "battery", "energy", "power",
    "consumption", "efficiency",
    "charging",

    "mapping", "cartography", "survey",
    "geolocation", "localization",
    "positioning", "route", "image",

    "medical", "epidemic",
    "outbreak", "disease", "hospital",

    "vehicle", "fleet", "logistics",
    "shipment", "cargo", "delivery",

    "research", "experiment",
    "scientific", "study",
    "investigation"
]


def is_valid_task(text: str) -> bool:
    text = text.lower()

    for keyword in VALID_KEYWORDS:
        if keyword in text:
            return True

    return False