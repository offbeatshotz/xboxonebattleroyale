from ursina import *
from player.player_controller import RealisticPlayer

def start_game():
    # Configure 4K and HDR settings before initializing Ursina
    window.vsync = True
    window.fullscreen = True
    window.render_mode = 'hdr' # Enable HDR rendering
    window.title = 'Realistic Battle Royale - 4K HDR'
    
    app = Ursina(
        development_mode=False,
        borderless=True,
        fullscreen=True,
        forced_aspect_ratio=1.77, # 16:9
        size=(3840, 2160) # 4K Resolution
    )

    # High Quality Lighting & Shadows
    sun = SunLight(direction=(1, -1, 1), resolution=4096) # 4K Shadow Map
    sun.shadow_map_resolution = 4096
    AmbientLight(intensity=0.6)

    # Post-processing (Realistic effects)
    EditorCamera() # For dev view
    
    # Environment
    ground = Entity(
        model='plane', 
        collider='box', 
        scale=500, 
        texture='grass', 
        texture_scale=(50,50),
        shader=lit_with_shadows_shader # Enable realistic shading
    )

    # Player
    player = RealisticPlayer(position=(0, 2, 0))

    # Sky
    Sky()

    app.run()

if __name__ == '__main__':
    start_game()
