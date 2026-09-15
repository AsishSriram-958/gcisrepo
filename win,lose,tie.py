your_score = int(input("Enter your score: "))
opponent_score = int(input("Enter opponent's score: "))
if your_score > opponent_score:
    print("You win!")
elif your_score < opponent_score:
    print("You lose!")
else:
    print("It's a tie!")

def game_outcome(your_score, opponent_score):
    if your_score > opponent_score:
        return "You win!"
    elif your_score < opponent_score:
        return "You lose!"
    else:
        return "It's a tie!"

def main():
    print("Your score:", int(your_score))
    print("Opponent's score:", int(opponent_score))
    print(game_outcome(your_score, opponent_score))
main()        