from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from panda3d.core import InputDevice

class RealisticPlayer(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = 8
        self.sprint_speed = 12
        self.is_sprinting = False
        self.height = 2
        
        # Add a visual model for the player (placeholder)
        self.model = Entity(
            parent=self,
            model='cube',
            color=color.green,
            scale=(1, 2, 1),
            position=(0, 1, 0),
            visible=False # Hide for local player
        )

    def update(self):
        super().update()
        
        # --- Cross-Platform Input (Gamepad Support) ---
        # Left Stick: Movement
        move_x = pxd.get_axis('left_x')
        move_y = pxd.get_axis('left_y')
        if abs(move_x) > 0.1 or abs(move_y) > 0.1:
            self.direction = Vec3(move_x, 0, move_y).normalized()
            
        # Right Stick: Camera Rotation (Xbox/PS5)
        look_x = pxd.get_axis('right_x')
        look_y = pxd.get_axis('right_y')
        if abs(look_x) > 0.1:
            self.rotation_y += look_x * 100 * time.dt
        if abs(look_y) > 0.1:
            self.camera_pivot.rotation_x -= look_y * 100 * time.dt
            self.camera_pivot.rotation_x = clamp(self.camera_pivot.rotation_x, -89, 89)

        # Sprinting logic (PC: Left Shift, Console: Left Stick Click)
        if held_keys['left shift'] or pxd.get_button('left_stick'):
            self.speed = self.sprint_speed
            self.is_sprinting = True
        else:
            self.speed = 8
            self.is_sprinting = False

        # Add bobbing or other realistic movement effects here
        if self.is_sprinting and any(held_keys[k] for k in ('w', 'a', 's', 'd')):
            # Add camera shake or FOV change for sprint
            camera.fov = lerp(camera.fov, 100, 5 * time.dt)
        else:
            camera.fov = lerp(camera.fov, 90, 5 * time.dt)

    def input(self, key):
        super().input(key)
        # Handle interaction keys
        if key == 'e':
            print("Interacting...")
