from ursina import *

class Vehicle(Entity):
    def __init__(self, name, speed, max_seats=6, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.speed = speed
        self.max_seats = max_seats
        self.occupants = []
        self.is_driven = False

    def enter(self, player):
        if len(self.occupants) < self.max_seats:
            self.occupants.append(player)
            player.visible = False
            player.enabled = False
            if len(self.occupants) == 1:
                self.is_driven = True
            print(f"{player} entered {self.name}")

    def exit(self, player):
        if player in self.occupants:
            self.occupants.remove(player)
            player.visible = True
            player.enabled = True
            player.position = self.position + Vec3(2, 0, 0)
            if len(self.occupants) == 0:
                self.is_driven = False
            print(f"{player} exited {self.name}")

    def update(self):
        if self.is_driven:
            # Handle vehicle movement logic
            if held_keys['w']:
                self.position += self.forward * self.speed * time.dt
            if held_keys['s']:
                self.position -= self.forward * self.speed * time.dt
            if held_keys['a']:
                self.rotation_y -= 50 * time.dt
            if held_keys['d']:
                self.rotation_y += 50 * time.dt

class Glider(Vehicle):
    def __init__(self, **kwargs):
        super().__init__(name="Glider", speed=15, max_seats=2, **kwargs)
        self.model = 'cube' # Placeholder
        self.color = color.cyan

    def update(self):
        super().update()
        if self.is_driven:
            # Glider specific logic: constant forward movement and slow descent
            self.position += self.forward * self.speed * time.dt
            self.y -= 1 * time.dt # Descend
