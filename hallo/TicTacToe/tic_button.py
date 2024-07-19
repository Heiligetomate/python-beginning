import pygame
import sys
from button import Button


class Hello:
    def __init__(self, buttons: list[Button]):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_size = 1000
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        self.buttons = buttons


    def main_loop(self):
        while True:
            self.clock.tick(60)
            self.screen.fill((155, 255, 155))
            for button in self.buttons:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if button.button_rect.collidepoint(event.pos):
                            return button.button_id
                            #print(event.pos)
                if button.button_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(button.button_surface, (127, 255, 212), (1, 1, 148, 48))
                else:
                    pygame.draw.rect(button.button_surface, (0, 0, 0), (0, 0, 150, 50))
                    pygame.draw.rect(button.button_surface, (255, 255, 255), (1, 1, 148, 48))
                    pygame.draw.rect(button.button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
                    pygame.draw.rect(button.button_surface, (0, 100, 0), (1, 48, 148, 10), 2)
                button.button_surface.blit(button.text, button.text_rect)
                self.screen.blit(button.button_surface, (button.button_rect.x, button.button_rect.y))
                pygame.display.update()
