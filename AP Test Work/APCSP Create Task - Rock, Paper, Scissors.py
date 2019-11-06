import random


def game():
    # Intro
    print("Welcome to Rock, Paper, Scissors! The game is simple. Get 2/3 to win")
    # AI
    game_cards = ["R", "P", "S"]
    r_computer = random.randint(0, 2)
    computer_score_counter = 0
    player_score_counter = 0
    number_of_games = 100
    for x in range(number_of_games):
        player_input = input("Rock, Paper, Or Scissors? Use R, P, and S")
        r_computer = random.randint(0, 2)
        computer = game_cards[r_computer]
        print("Player:", player_input, ", Computer:", computer)  # Print Choices
        if player_input == computer:
            print("That's a Tie! Lets play again.")
            number_of_games += 1
        elif computer == game_cards[0]:  # Rock vs. Paper
            if player_input == "P":
                print("YOU WIN!!!")
                player_score_counter += 1
            elif player_input == "S":  # Rock vs. Scissors
                print("COMPUTER WINS!!!")
                computer_score_counter += 1
        elif computer == game_cards[1]:  # Paper vs. Rock
            if player_input == "R":
                print("COMPUTER WINS!!!")
                computer_score_counter += 1
            elif player_input == "S":  # Paper vs. Scissors
                print("YOU WIN!!!")
                player_score_counter += 1
        elif computer == game_cards[2]:  # Scissors vs. Rock
            if player_input == "R":
                print("YOU WIN!!!")
                player_score_counter += 1
            elif player_input == "P":  # Scissors vs. Paper
                print("COMPUTER WINS!!!")
                computer_score_counter += 1
        total_wins = player_score_counter + computer_score_counter
        if player_input not in game_cards:
            print("Sorry, but you can't do that.")
            number_of_games += 1 + x
        if player_score_counter >= 2:
            print("Congrats! You have won the game with a SCORE OF:", player_score_counter, " POINTS OUT OF 3, with a total win count of:", total_wins)
            break
        elif computer_score_counter >= 2:
            print("Sorry, but the computer has won with a SCORE OF:", computer_score_counter, " POINTS OUT OF 3, with a total win count of:", total_wins)
            break


game()
play_again = input("Would you like to play again?")
if play_again == "Yes":
    game()
else:
    print("Ok")
