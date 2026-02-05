import platform
import sys

def get_platform():
    """
    Detects the current platform.
    Returns: 'PC', 'Xbox', or 'PS5' (Simulation based on environment)
    """
    system = platform.system()
    
    # In a real console environment, we would use platform-specific SDK checks
    # For now, we detect based on OS and allow manual overrides
    if system == 'Windows':
        # Check if running in Xbox Game Core environment (Simplified)
        if hasattr(sys, 'getwindowsversion') and sys.getwindowsversion().build > 22000:
            return "PC/Xbox"
        return "PC"
    elif system == 'Linux':
        return "PC/SteamDeck"
    
    return "Unknown"

def is_console():
    return get_platform() in ["Xbox", "PS5"]

def get_network_metadata():
    return {
        "platform": get_platform(),
        "version": "1.0.0-4k-hdr",
        "crossplay_enabled": True
    }
