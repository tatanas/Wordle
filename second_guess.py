from first_guess import GUESSES, ANSWERS, compare, get_remaining_possible_answers
from collections import defaultdict

BEST_WORD = "roate"

def get_comparison_string(comparison):
    return f"{comparison[0][1]}{comparison[1][1]}{comparison[2][1]}{comparison[3][1]}{comparison[4][1]}"

# format: (comparison_string, second_guess): list of remaining answers -> (average number of remaining answers, worst case scenario)
dictionary = defaultdict(list)

if __name__ == "__main__":
    for second_guess in GUESSES:
        print(f"Testing second guess {second_guess}")
        for answer in ANSWERS:
            first_comparison = compare(BEST_WORD, answer)
            first_remaining = get_remaining_possible_answers(first_comparison)
            second_comparison = compare(second_guess, answer)
            second_remaining = get_remaining_possible_answers(second_comparison, first_remaining)
            dictionary[(get_comparison_string(first_comparison), second_guess)].append(len(second_remaining))

    comparison_strings = []
    result = {}

    for key in dictionary:
        average = sum(dictionary[key]) / len(dictionary[key])
        worst_case = max(dictionary[key])
        best_case = min(dictionary[key])
        if key[0] not in comparison_strings:
            comparison_strings.append(key[0])
        result[key] = (average, worst_case, best_case)

    # write out to files, sorted from min to max average
    for key in sorted(result, key=lambda x: result[x][0]):
        with open(f"{BEST_WORD}_{key[0]}.txt", "a") as f:
            f.write(f"{key[1]}: {result[key]}\n")
