import pygame
import sys

# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()

# Create a Pygame window
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pygame Clickable Button')

# Create a font object
font = pygame.font.Font(None, 24)

# Create a surface for the button
button_surface = pygame.Surface((100, 100))

# Render text on the button
text = font.render("Click Me", True, (0, 0, 0))
text_rect = text.get_rect(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))

# Create a pygame.Rect object that represents the button's boundaries
button_rect = pygame.Rect(125, 125, 150, 50)  # Adjust the position as needed

# Start the main loop
while True:
    # Set the frame rate
    clock.tick(60)

    # Fill the display with color
    screen.fill((255, 255, 255))

    # Get events from the event queue
    for event in pygame.event.get():
        # Check for the quit event
        if event.type == pygame.QUIT:
            # Quit the game
            pygame.quit()
            sys.exit()

        # Check for the mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Call the on_mouse_button_down() function
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")

    pygame.display.update()