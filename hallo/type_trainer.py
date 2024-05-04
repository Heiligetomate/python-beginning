import random as r
import time


chars_upper = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "!", "§", "$", "%", "&", "/", "(", ")", "=", "?", "}", "]", "[", "{", "*", "+", "~", "#", "@"]


def make_random_exercise(length):
    exercise = ""
    for i in range(length):
        exercise += r.choice(chars_upper)
    return exercise


old_time = time.time()
a = make_random_exercise(10)
print(a)
user = input()
new_time = time.time()
if user == a:
    print("Correct!")
    print(f"Time: {int(new_time - old_time)} sec")
