import plotly.express as px
import random as r

a = []
b = []


while True:
    fruit = input("Enter an element. You can always continue with s ")
    if fruit.lower() == "s":
        break
    else:
        b.append(fruit)

for i in b:
    while True:
        c = input(f"Wie oft {i} ? ")
        try:
            message = int(c)
            break
        except ValueError:
            print("Invalid")
    a.append(int(c))

print(a)
print(b)
fig = px.pie(a, b, a)
fig.show()
