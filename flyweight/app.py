import pygame
import random
from patron import Bullet, BulletFactory
WIDTH, HEIGHT = 800, 600

class ShooterGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Juego CON Flyweight - Disparos")
        self.clock = pygame.time.Clock()
        self.running = True
        self.bullets = []
        self.player_pos = [WIDTH // 2, HEIGHT // 2]
        self.player_color = (0, 0, 0)
        self.colors = ['rojo', 'azul', 'verde']
        self.damages = [10, 20, 30]
        self.target_pos = [random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)]
        self.target_radius = 30

    def shoot(self, x, y, color, damage):
        bullet_type = BulletFactory.get_bullet_type(color, damage)
        bullet = Bullet(x, y, bullet_type)
        self.bullets.append(bullet)

    def draw_player(self):
        pygame.draw.rect(self.screen, self.player_color, (*self.player_pos, 40, 40))

    def draw_bullets(self):
        for bullet in self.bullets:
            bullet.draw(self.screen)

    def draw_stats(self):
        font = pygame.font.SysFont("Arial", 24)
        num_bullets = len(self.bullets)
        num_types = len(BulletFactory._bullet_types)
        bullet_mem = num_bullets * 24 + num_types * 40
        stats = [
            f"Balas disparadas: {num_bullets}",
            f"Memoria balas: {bullet_mem} bytes",
            f"Tipos de bala (Flyweight): {num_types}",
        ]
        for i, text in enumerate(stats):
            img = font.render(text, True, (0, 0, 0))
            self.screen.blit(img, (10, 10 + i * 30))

    def check_bullet_hits(self):
        for bullet in self.bullets:
            dx = bullet.x - self.target_pos[0]
            dy = bullet.y - self.target_pos[1]
            distance = (dx**2 + dy**2) ** 0.5
            if distance < self.target_radius + 8:
                self.target_pos = [random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)]
                self.bullets.remove(bullet)
                break

    def draw_target(self):
        pygame.draw.circle(self.screen, (255, 200, 0), self.target_pos, self.target_radius)

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.screen.fill((200, 200, 200))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    mx, my = pygame.mouse.get_pos()
                    color = random.choice(self.colors)
                    damage = random.choice(self.damages)
                    self.shoot(self.player_pos[0] + 20, self.player_pos[1] + 20, color, damage)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.player_pos[0] -= 5
            if keys[pygame.K_d]:
                self.player_pos[0] += 5
            if keys[pygame.K_w]:
                self.player_pos[1] -= 5
            if keys[pygame.K_s]:
                self.player_pos[1] += 5

            self.draw_player()
            self.draw_target()
            self.draw_bullets()
            self.check_bullet_hits()
            self.draw_stats()
            pygame.display.flip()
        pygame.quit()
        return

if __name__ == "__main__":
    game = ShooterGame()
    game.run()