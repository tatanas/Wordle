import datetime 

# list of all 4-tuples with each element being a number from 0 to 5
POSSIBLE_SOLUTIONS = [f"{a}{b}{c}{d}" for a in range(6) for b in range(6) for c in range(6) for d in range(6)]

def compare(guess, answer):
    used = [False, False, False, False]
    red_pins = 0
    white_pins = 0
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            red_pins += 1
            used[i] = True

    for i in range(len(guess)):
        if guess[i] in answer and answer[i] != guess[i]:
            index_in_answer = answer.index(guess[i])

            while used[index_in_answer]:
                index_in_answer = answer.find(guess[i], index_in_answer + 1)
                if index_in_answer == -1:
                    break
            
            if index_in_answer != -1:
                white_pins += 1
                used[index_in_answer] = True
    
    return (red_pins, white_pins)

def get_remaining_possible_solutions(guess, comparison):
    result = []
    for possible_solution in POSSIBLE_SOLUTIONS:
        comparison_to_possible_solution = compare(guess, possible_solution)
        if comparison_to_possible_solution == comparison:
            result.append(possible_solution)
    return result

# create a random answer. a string with 4 characters, each being a digit from 0 to 5
import random
answer = ''.join(random.choice('012345') for _ in range(4))
print(f"Answer is: {answer}")

NUMBER_OF_GUESSES = 6
POSSIBILITIES = []
for i in range(NUMBER_OF_GUESSES):
    guess = ''.join(random.choice('012345') for _ in range(4))
    comparison = compare(guess, answer)
    possibilities = get_remaining_possible_solutions(guess, comparison)
    POSSIBILITIES.append(possibilities)
    print(f"Guess {i+1}: {guess}, Comparison: {comparison}, Remaining possibilities: {len(possibilities)}")

# Calculate the intersection of all possibilities
final_possibilities = set.intersection(*map(set, POSSIBILITIES))
print(f"Final possibilities: {final_possibilities}, Count: {len(final_possibilities)}")



