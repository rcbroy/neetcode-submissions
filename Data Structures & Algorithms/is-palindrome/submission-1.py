import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = [l.lower() for l in s if l in string.ascii_letters or l in string.digits]
        word = "".join(word)
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True