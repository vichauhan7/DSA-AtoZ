def print1(n):
    for i in range(n):
        for j in range(n):
            print('*', end='')
        print()

def print2(n):
    for i in range(n):
        for j in range(i):
            print('*', end='')
        print()

def print3(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end='')
        print()


print3(5)
