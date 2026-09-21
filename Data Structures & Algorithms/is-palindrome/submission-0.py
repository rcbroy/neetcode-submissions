class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join([l for l in s if l.isalnum()]).lower()
        print(word)
        return word == word[::-1]