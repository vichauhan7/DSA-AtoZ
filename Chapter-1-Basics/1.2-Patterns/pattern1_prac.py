def print1(n):
    for i in range(n):
        for j in range(n):
            print('*', end='')
        print()

def print2(n):
    for i in range(n):
        for j in range(i):
            print(j + 1, end='')
        print()


print1(4)
print2(5)