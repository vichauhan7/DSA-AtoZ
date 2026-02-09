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

def print4(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1, end='')
        print()

def print5(n):
    for i in range(n):
        for j in range(n-i):
            print('*', end='')
        #n=n-1   
        print()

def print6(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end='')
        print()

def print7(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end='')
        for j in range((i*2)+1):
            print('*', end='')
        for j in range(n-i-1):
            print(' ', end='')                        
        print()

def print8(n):
    for i in range(n):
        for j in range(i):
            print(' ', end='')
        for j in range((n*2) - (i*2) -1):
            print('*', end='')
        for j in range(i):
            print(' ', end='')                        
        print()

def print9(n):

    for i in range(n):
        for j in range(n-i-1):
            print(' ', end='')
        for j in range((i*2)+1):
            print('*', end='')
        for j in range(n-i-1):
            print(' ', end='')                        
        print()
        
    for i in range(n):
        for j in range(i):
            print(' ', end='')
        for j in range((n*2) - (i*2) -1):
            print('*', end='')
        for j in range(i):
            print(' ', end='')                        
        print()


def print10(n):
    for i in range((2*n)-1):
        star = i + 1
        if i > n - 1: star = (2*n)-i -1      
        for j in range(star):
            print('*', end='')
        print()


def print11(n):
    for i in range(n):
        for j in range(i+1):
            print((j+i+1)%2, end='')
        print()

#print11(5)



