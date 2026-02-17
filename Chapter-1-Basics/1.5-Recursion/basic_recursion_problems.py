def printname(name, n):
    if n < 0:
        print("EXIT")
        return
    n = n -1
    print(name)
    printname(name, n)
  


def printnumberseries(i,n):
    if  i > n:
        print("EXIT")
        return
    print(i)
    i = i + 1
    printnumberseries( i,n)


def printnumberseries1(n):
    if  n <= 0:
        return
    printnumberseries1(n-1)
    print(n)
printnumberseries1(22)


def printrevnumberseries(n):
    if  n <= 0:
        print("EXIT")
        return
    print(n)
    printrevnumberseries(n-1)
   


def printnumberseriesbybacktracking(i,n):
    if  i < 1:
        print("EXIT")
        return
    printnumberseriesbybacktracking( i-1,n)
    print(i)
    #print statements are executed in reverse order when we backtrack from the base case to the original call.
    # first we call the function recursively until we reach the base case, and then we print the numbers as we backtrack through the recursive calls. 
    # This results in the numbers being printed in reverse order compared to a normal iterative approach.
#printnumberseriesbybacktracking(5,5)   


#print n to 1 using backtracking
def printnumberseriesbybacktrackingrev(i,n):
    if  i > n:
        print("EXIT")
        return
    printnumberseriesbybacktrackingrev( i+1, n)
    print(i)
#printnumberseriesbybacktrackingrev(1,5)     