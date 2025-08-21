from main import GUESSES, ANSWERS, compare, get_remaining_possible_answers

BEST_WORD = "roate"
ANSWERS_COUNT = len(ANSWERS)

guesses_and_comparisons = {}

from datetime import datetime

for second_guess in ANSWERS:
    print(f"[{datetime.now()}] Checking guess: {second_guess}")
    for answer in ANSWERS:
        first_comparison = compare(BEST_WORD, answer)
        first_comparison_str = f"{first_comparison[0][1]}{first_comparison[1][1]}{first_comparison[2][1]}{first_comparison[3][1]}{first_comparison[4][1]}"
        possible_answers_after_first = get_remaining_possible_answers(first_comparison)
        second_comparison = compare(second_guess, answer)
        possible_answers_after_second = get_remaining_possible_answers(second_comparison, possible_answers_after_first)
        if (second_guess, first_comparison_str) not in guesses_and_comparisons:
            guesses_and_comparisons[(second_guess, first_comparison_str)] = [len(possible_answers_after_second)]
        else:
            guesses_and_comparisons[(second_guess, first_comparison_str)].append(len(possible_answers_after_second))

end_dictionary = {}

for key in guesses_and_comparisons:
    end_dictionary[key] = (sum(guesses_and_comparisons[key]) / len(guesses_and_comparisons[key])) / ANSWERS_COUNT

possible_comparisons = set([comparison for (_, comparison) in guesses_and_comparisons.keys()])

# get best word (minimum value) when comparison is "20000"

for c in possible_comparisons:
    best_word = None
    best_value = float("inf")
    for (second_guess, comparison), value in end_dictionary.items():
        if comparison == c and value < best_value:
            best_value = value
            best_word = second_guess
    print(f"Best word for comparison '{c}':", best_word)

# create a file for each possible comparison
# each file should list each word and its value, like
# afoot: 0.001
#etc

for c in possible_comparisons:
    filename = f"wordle_second_guess_{c}.txt"
    with open(filename, "w") as f:
        for (second_guess, comparison), value in end_dictionary.items():
            if comparison == c:
                f.write(f"{second_guess}: {value}\n")