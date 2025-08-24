# sort the roate_XXXX files by best worst case scenario.
# on ties, use minimum average.
import os

files = [name for name in os.listdir() if name.startswith("roate")]

for filename in files:
    with open(filename) as file:        
        lines = [line.strip().split(":") for line in file.readlines()]
        if lines[0][0] == "ANSWER":
            continue
        lines = [[line[0], line[1].strip(" ()").split(",")] for line in lines]
        lines = [[line[0], [float(i) for i in line[1]]] for line in lines]
        
    # sort lines according to the worst case scenario (line[1][1]) then average (line[1][0])
    sorted_lines = sorted(
        lines,
        key=lambda x: (x[1][1], x[1][0])  # (worst, average)
    )

    # write back
    with open(filename, "w") as file:
        for line in sorted_lines:
            file.write(line[0] + ": " + str(line[1][1]) + ", " + str(line[1][0]) + ", " + str(line[1][2]) + "\n")
