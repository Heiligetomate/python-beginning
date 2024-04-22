from zahl_rate_game import is_zahl_erraten
from quiz_game import quiz_game
from calculator import calculator

print("Welcome to the mega super multitool!!!")
text = '''
  __  __ _    _ _   _______ _____ _______ ____   ____  _
 |  \/  | |  | | | |__   __|_   _|__   __/ __ \ / __ \| |
 | \  / | |  | | |    | |    | |    | | | |  | | |  | | |
 | |\/| | |  | | |    | |    | |    | | | |  | | |  | | |
 | |  | | |__| | |____| |   _| |_   | | | |__| | |__| | |____
 |_|  |_|\____/|______|_|  |_____|  |_|  \____/ \____/|______|   '''
print(text)

print("What would you like to do? ")
print("[a]: calculator")
print("[b]: dice")
print("[c]: story maker")
print("[d]: quiz game")
print("[e]: rate game")
user_input = input("")
if user_input.lower() == "d":
    quiz_game()
elif user_input.lower() == "a":
    calculator()
