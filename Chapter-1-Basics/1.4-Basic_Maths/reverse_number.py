def reverse(x: int) -> int:
    minus_ind = 0
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31 
    reverse_num : int = 0
    if x < 0:
        minus_ind = 1
        x = x * -1    
    while x > 0:
        reverse_num =  (x % 10 ) + (reverse_num * 10)
        x = x // 10
    if minus_ind == 1:
        reverse_num = reverse_num * -1

    if reverse_num >= INT_MAX  or reverse_num <= INT_MIN:
        print (0)
    else:
        print (reverse_num)




def isPalindrome(x: int) -> bool:
    if x < 0 :
        return False
    dup = x
    int_max = 2**31 - 1
    rev = 0
    while x:
        digit = x % 10
        x = x // 10
        rev = (rev * 10 ) + digit
    print(rev)
    if rev >= int_max :
        return False
    elif dup == rev:
        return True
    else :
        return False

res = isPalindrome(10)
print(res)