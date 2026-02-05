from ursina import *
import random

class BloodEffect(Entity):
    def __init__(self, position, **kwargs):
        super().__init__(
            model='sphere',
            color=color.red,
            scale=0.1,
            position=position,
            **kwargs
        )
        self.fade_out(0, duration=0.5)
        self.animate_scale(0.5, duration=0.2)
        destroy(self, delay=0.5)

    def update(self):
        self.position += Vec3(
            random.uniform(-1, 1),
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        ) * time.dt * 5
        self.y -= 2 * time.dt # Gravity effect

class Attachment:
    def __init__(self, name, type, stats_mod):
        self.name = name
        self.type = type # 'scope', 'muzzle', 'grip', 'magazine', 'stock'
        self.stats_mod = stats_mod # Dict of modifiers

class WeaponBase(Entity):
    def __init__(self, name, damage, fire_rate, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.damage = damage
        self.fire_rate = fire_rate
        self.attachments = {
            'scope': None,
            'muzzle': None,
            'grip': None,
            'magazine': None,
            'stock': None
        }
        self.max_attachments = 5
        self.ammo_count = 30
        self.is_reloading = False

    def add_attachment(self, slot, attachment):
        if slot in self.attachments:
            self.attachments[slot] = attachment
            print(f"Added {attachment.name} to {slot}")

    def fire(self):
        if self.ammo_count > 0 and not self.is_reloading:
            self.ammo_count -= 1
            
            # Raycast for hit detection
            hit_info = raycast(camera.world_position, camera.forward, distance=100)
            
            if hit_info.hit:
                # If we hit something (e.g., another player)
                print(f"Hit {hit_info.entity}!")
                
                # Spawn multiple blood particles for a "spray" effect
                for _ in range(15):
                    BloodEffect(position=hit_info.world_point)
                
            print(f"Firing {self.name}! Ammo: {self.ammo_count}")
            return True
        return False

    def reload(self):
        if not self.is_reloading:
            self.is_reloading = True
            invoke(setattr, self, 'is_reloading', False, delay=2)
            self.ammo_count = 30 # Reset to max
            print("Reloaded.")
