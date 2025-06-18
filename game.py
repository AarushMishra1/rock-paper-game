import random

u = input("Rock, Paper or Scissors? ")
c = random.choice(["Rock", "Paper", "Scissors"])
print("Computer:", c)

if u == c:
    print("Tie")
elif u == "Rock" and c == "Scissors":
    print("Win")
elif u == "Paper" and c == "Rock":
    print("Win")
elif u == "Scissors" and c == "Paper":
    print("Win")
else:
    print("Lose")
