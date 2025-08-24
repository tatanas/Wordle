from main import get_remaining_possible_answers, compare, GUESSES, ANSWERS
from collections import defaultdict

while True:
    first_input = input("Enter your output after playing \"roate\": ")
    with open(f"roate_{first_input}.txt", "r") as file:
        first_line = file.readline().strip()
        print(first_line)
        second_guess = first_line.split(":")[0]
    first_comparison = [(a, int(b)) for a, b in zip("roate", first_input)]
    first_results = get_remaining_possible_answers(first_comparison)
    print(f"Possible solutions are {len(first_results)}" + (": " + str(first_results) if len(first_results) < 10 else ""))

    second_input = input(f"Enter your output after playing \'{second_guess}\': ")
    second_comparison = [(a, int(b)) for a, b in zip(second_guess, second_input)]
    second_results = get_remaining_possible_answers(second_comparison, first_results)
    print(f"Possible solutions are {len(second_results)}:", second_results)

    best_guesses = defaultdict(list)

    for guess in GUESSES:
        for answer in second_results:
            comparison = compare(guess, answer)
            possible_answers = get_remaining_possible_answers(comparison, second_results)
            best_guesses[guess].append(len(possible_answers))
        best_guesses[guess] = sum(best_guesses[guess]) / len(best_guesses[guess])

    # remove any entries from best_guesses that have a value of 1 but are not in answers
    for guess in best_guesses.copy():
        if guess not in second_results and best_guesses[guess] < 1.1:
            del best_guesses[guess]    

    # get guess in best_guesses with minimum average
    best_guess = min(best_guesses, key=best_guesses.get)
    print(f"Best guess: {best_guess} ({best_guesses[best_guess]})\n")