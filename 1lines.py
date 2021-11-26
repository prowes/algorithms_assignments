# input: amount of lines and their coordinates
# output: minimum of possible intersections and their coordinates
import sys

if __name__ == '__main__':
    data = sys.stdin.readlines()
    amount = data[0]
    initial_lines = []
    for i in range(1, len(data)):
        initial_lines.append([int(data[i].split()[0]), int(data[i].split()[1])])

    initial_lines.sort(key=lambda x:x[1],reverse=False)
    first = range(initial_lines[0][0], initial_lines[0][1] + 1, 1)
    result = []
    result.append(initial_lines[0][1])
    while bool(initial_lines):
        if all(x < initial_lines[0][0] for x in result):
            result.append(initial_lines[0][1])
        initial_lines.pop(0)
    print(len(result))
    for j in range(0, len(result)):
        print(result[j], end=" ")