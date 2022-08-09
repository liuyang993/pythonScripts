import sys
def hello(p1):
    print("print text from another script" , p1)

if __name__ == '__main__':
    hello(sys.argv[1])