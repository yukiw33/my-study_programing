import sys
from itertools import product

input = sys.stdin.readline

def isvalid(S):
    count = 0
    for s in S:
        if s == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return False
    return(count == 0)


def main(N):
    for S in product(['(',')'], repeat=N):
        if isvalid((S)):
            print(*S, sep=(''))
    

if __name__ == '__main__':
    N = int(input())
    main(N)

