import pygame

# Flyweight
class BulletType:
    def __init__(self, color, damage):
        self.color = color
        self.damage = damage

    def get_rgb(self):
        if self.color == 'rojo':
            return (255, 0, 0)
        elif self.color == 'azul':
            return (0, 0, 255)
        elif self.color == 'verde':
            return (0, 255, 0)
        return (0, 0, 0)

    def draw(self, screen, x, y):
        pygame.draw.circle(screen, self.get_rgb(), (x, y), 8)

# Flyweight Factory
class BulletFactory:
    _bullet_types = {}

    @classmethod
    def get_bullet_type(cls, color, damage):
        key = (color, damage)
        if key not in cls._bullet_types:
            cls._bullet_types[key] = BulletType(color, damage)
        return cls._bullet_types[key]


class Bullet:
    def __init__(self, x, y, bullet_type):
        self.x = x
        self.y = y
        self.bullet_type = bullet_type
        self.speed = 10

    def draw(self, screen):
        self.bullet_type.draw(screen, self.x, self.y)
        self.x += self.speed  
