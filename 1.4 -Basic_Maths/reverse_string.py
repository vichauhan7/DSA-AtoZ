class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        while x > 0 :
            rev = (x % 10) * 10 + rev
        return rev
