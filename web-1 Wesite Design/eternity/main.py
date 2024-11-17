import pygame


pygame.init()


window = pygame.display.set_mode((480,580))
pygame.display.set_caption("Eternity made by: yours trully Vian pogi")

runnig = True
while runnig:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
            runnig = False

  pygame.quit()