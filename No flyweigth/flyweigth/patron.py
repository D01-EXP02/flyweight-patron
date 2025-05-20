import pygame

class Bullet:
    def __init__(self, x, y, color, damage):
        self.x = x
        self.y = y
        self.color = color
        self.damage = damage
        self.speed = 10

    def get_rgb(self):
        if self.color == 'rojo':
            return (255, 0, 0)
        elif self.color == 'azul':
            return (0, 0, 255)
        elif self.color == 'verde':
            return (0, 255, 0)
        return (0, 0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.get_rgb(), (self.x, self.y), 8)
        self.x += self.speed