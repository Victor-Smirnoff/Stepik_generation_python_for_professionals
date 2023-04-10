import sys
import pickle


s1 = input()

with open(s1, 'rb') as file:
    res = pickle.load(file)

data = list(map(str.strip, sys.stdin))

print(res(*data))
