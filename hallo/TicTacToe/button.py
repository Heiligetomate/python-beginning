import pygame

class Button:
    def __init__(self, caption, left, top, width, height, button_id):
        pygame.init()
        self.button_id = button_id
        self.font = pygame.font.Font(None, 24)
        self.button_surface = pygame.Surface((width, height))
        self.text = self.font.render(caption, True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.button_surface.get_width() / 2, self.button_surface.get_height() / 2))
        self.button_rect = pygame.Rect(left, top, width, height)


