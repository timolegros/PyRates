from sstate import State
import sys

def main():
    inp = []
    print(sys.argv)
    for index in range(1, len(sys.argv)):
        inp.append(int(sys.argv[index]))
    print(inp)
            
main()