# input sample: 3
# output sample: 1 2
# this script outputs digits which are needed to sum an input's one, and also their amount

import sys

def find_sum(initial_number):
    consists = []
    initial_number = int(initial_number)
    i = 1
    while i < initial_number + 1:
        if initial_number - i >= i + 1:
            initial_number -= i
            consists.append(i)
        i += 1
    consists.append(initial_number)
    print(len(consists))
    for j in range(0, len(consists)):
        print(consists[j], end=" ")

if __name__ == '__main__':
    find_sum(sys.stdin.read())
