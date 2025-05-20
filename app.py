import random

# Flyweight
class BulletType:
    def __init__(self, color, damage):
        self.color = color
        self.damage = damage

    def draw(self, x, y):
        print(f"Disparo {self.color} en ({x},{y}) con daño {self.damage}")

# Flyweight Factory
class BulletFactory:
    _bullet_types = {}

    @classmethod
    def get_bullet_type(cls, color, damage):
        key = (color, damage)
        if key not in cls._bullet_types:
            cls._bullet_types[key] = BulletType(color, damage)
        return cls._bullet_types[key]

# Contexto
class Bullet:
    def __init__(self, x, y, bullet_type):
        self.x = x
        self.y = y
        self.bullet_type = bullet_type

    def draw(self):
        self.bullet_type.draw(self.x, self.y)

# Juego
class ShooterGame:
    def __init__(self):
        self.bullets = []

    def shoot(self, x, y, color, damage):
        bullet_type = BulletFactory.get_bullet_type(color, damage)
        bullet = Bullet(x, y, bullet_type)
        self.bullets.append(bullet)

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

# Ejemplo de uso
if __name__ == "__main__":
    game = ShooterGame()
    colors = ['rojo', 'azul', 'verde']
    damages = [10, 20, 30]

    # Disparar 10 balas aleatorias
    for _ in range(10):
        x, y = random.randint(0, 100), random.randint(0, 100)
        color = random.choice(colors)
        damage = random.choice(damages)
        game.shoot(x, y, color, damage)

    game.draw()