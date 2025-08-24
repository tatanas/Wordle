import os
from first_guess import compare, get_remaining_possible_answers
# check every roate_XXXXX.txt file.
# get the possible answers stemming from such comparison.
# if the list has only one of those

# get every file that starts with roate_XXXXX.txt in this folder.
files = [name for name in os.listdir() if name.startswith("roate_")]

for file in files:
    comparison_str = [int(i) for i in file.split("_")[1][:-4]]
    with open(file, "r") as f:
        lines = f.readlines()
    comparison = [(a, int(b)) for a, b in zip("roate", comparison_str)]
    results = get_remaining_possible_answers(comparison)
    if len(results) == 1:
        best_guess = results[0]
        # find the line that contains the best guess,
        # remove it,
        # and then add it to the start.
        new_lines = [line for line in lines if not line.startswith(best_guess)]
        new_lines = ["ANSWER: " + best_guess + "\n"] + new_lines
        # write out lines to file
        with open(file, "w") as f:
            for item in new_lines:
                f.write(item)
    