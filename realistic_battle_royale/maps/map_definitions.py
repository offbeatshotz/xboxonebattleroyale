class MapInfo:
    def __init__(self, name, size, terrain_type):
        self.name = name
        self.size = size # 'Big', 'Medium'
        self.terrain_type = terrain_type

MAP_LIST = [
    MapInfo("Veridian Forest", "Big", "Forest"),
    MapInfo("Dusty Plains", "Big", "Desert"),
    MapInfo("Frost Peak", "Big", "Snow"),
    MapInfo("Urban Jungle", "Medium", "City"),
    MapInfo("Coastal Bay", "Medium", "Island"),
    MapInfo("Industrial Zone", "Medium", "Industrial"),
    MapInfo("Swampy Marsh", "Big", "Swamp"),
    MapInfo("Canyon Pass", "Medium", "Canyon"),
    MapInfo("Alpine Valley", "Big", "Mountain"),
    MapInfo("Neon District", "Medium", "Cyberpunk/Night City")
]

def get_map_config(map_name):
    for m in MAP_LIST:
        if m.name == map_name:
            return m
    return None
