

color = "lightgoldenrodyellow"


print(color[::-1])
guess = str(input("Enter the original color: "))

if guess == "lightgoldenrodyellow":
    print("CORRECT! THE ANSWER IS INDEED lightgoldenrodyellow! YOU HAVE WON THE GRAND PRIZE!")

elif guess == "LightGoldenRodYellow":
    print("remember, no uppercases!")
else:
    print("wrong")

