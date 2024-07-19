import tic_with_ui as tic
import tic_button as hello
import button as btn
import pygame
import sys

buttonStart = btn.Button("Starten", 125, 125, 150, 50, 1)
buttonEnd = btn.Button("Stoppen", 325, 125, 150, 50, 2)

buttons = list()
buttons.append(buttonStart)
buttons.append(buttonEnd)

hello_view = hello.Hello(buttons)

button_id = hello_view.main_loop()
if button_id == 1:
    t = tic.TicTacToeView()
    t.run()
else:
    pygame.quit()
    sys.exit()