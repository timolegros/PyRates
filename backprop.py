from sstate import State
import sys

def main():
    inp = []
    c = 0
    for index in range(1, len(sys.argv)):
        inp[c] = sys.argv[index]
        print(type(inp[c]))