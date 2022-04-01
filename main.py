import random


def get_range_max() -> int:
    limit = input("\tWhat is the limit for the random number ? ")
    while not limit.isdigit() and int(limit) < 1:
        limit = input("\t\tEnter a number greater than 1 > ")
    return int(limit)


def user_input():
    user = input("\t> ")
    while not user.isdigit():
        user = input("\t\tEnter a number > ")
    return int(user)


def guess_number(lim):
    failed_sentences = ("Almost...", "Ah! Close!", "Sorry...", "Nope")
    number_to_guess = random.randint(1, lim)
    number_move = 1
    print("\tEnter your guess")
    user_guess = user_input()
    while user_guess != number_to_guess:
        number_move += 1
        if user_guess > number_to_guess:
            print("\t\tToo high.", random.choice(failed_sentences))
        else:
            print("\t\tToo low.", random.choice(failed_sentences))
        user_guess = user_input()
    print("*************************")
    print("***** YEAH! VICTORY *****")
    print("*************************")
    print(f"\tYou found the secret number in {number_move} moves")


if __name__ == "__main__":
    print("****************************")
    print("***** GUESS THE NUMBER *****")
    print("****************************")
    maximum = get_range_max()
    guess_number(maximum)
