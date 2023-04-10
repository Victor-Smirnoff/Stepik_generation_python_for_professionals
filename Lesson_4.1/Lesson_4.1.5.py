import sys

print(len([line.strip() for line in sys.stdin if line.strip()[0] == '#']))




