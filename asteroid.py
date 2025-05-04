import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, 'pink', self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    random_angle = random.uniform(20, 50)
    asteroid1_vector = self.velocity.rotate(random_angle)
    asteroid2_vector = self.velocity.rotate(-random_angle)
    
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
    new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

    new_asteroid1.velocity = asteroid1_vector * 2
    new_asteroid2.velocity = asteroid2_vector * 2

    