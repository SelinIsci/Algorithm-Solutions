# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        return num == num[::-1] 