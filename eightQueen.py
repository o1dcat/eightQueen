# board size

N=8


# check whether position(n,c) is free from attacks
def isplaceok(a, n, c):
    for i in range(1, n):
        if(a[i] == c) or (a[i]-i == c-n) or (a[i]+i == c+n):
            return false
        return true


# print a board
def printsolution(a):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if a[i] == j:
                print("X")
            else:
                print("-")
        print("\n")
    print("\n")


# add to board 'a' all queens 'n' to 'N'
def addqueen(a, n):
    if n > N:  # all queens have been placed?
        printsolution(a)
    else:
        for c in range(1, N+1):
            print("run here first")
            if isplaceok(a, n, c):
                a[n] = c  # place n-th queen at column 'c'
                addqueen(a, n+1)


# run the program
if __name__ == "__main__":
    addqueen({}, 1)


