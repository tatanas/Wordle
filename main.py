from first_guess import compare, ANSWERS, GUESSES, get_remaining_possible_answers
from collections import defaultdict

def get_best_guess(remaining_answers):
    values = defaultdict(list)
    for i, guess in enumerate(GUESSES):
        for answer in remaining_answers:
            comparison = compare(guess, answer)
            remaining = len(get_remaining_possible_answers(comparison, remaining_answers))
            values[guess].append(remaining)
        # values[guess] = sum(values[guess]) / len(values[guess])
        # choosing now through best worst case scenario
        values[guess] = max(values[guess])

    for guess in values.copy():
        if guess not in remaining_answers and values[guess] < 1.1:
            del values[guess]        
    best_guess = min(values, key=values.get)

    return best_guess, values[best_guess]

while True:
    remaining_answers = ANSWERS
    guess = "roate"
    for i in range(6):
        output = input(f"[{i + 1}] Enter your output after playing {guess}: ")
        if output == "": 
            print() 
            break

        comparison = [(a, int(b)) for a,b in zip(guess, output)]
        remaining_answers = get_remaining_possible_answers(comparison, remaining_answers)
        print(f"Remaining answers: {len(remaining_answers)} {(remaining_answers if len(remaining_answers) <= 10 else "")}")
        if guess == "roate" and i == 0:
            # fetch the best answer from the files
            filename = f"roate_{output}.txt"
            with open(filename) as f:
                result = f.readline()
                print(f"Your next best guess is: {result}")
                guess = result.split(":")[0]
        else:
            # if there's one remaining answer, do that one. if there's two, do either (choosing the first one for convenience).
            if len(remaining_answers) <= 2:
                best_guess, average = remaining_answers[0], 1.0
                print(f"Your next best guess is {best_guess} ({average})\n")
                break                
            else:
                best_guess, average = get_best_guess(remaining_answers)
                print(f"Your next best guess is {best_guess} ({average})\n")
            guess = best_guess