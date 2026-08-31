class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}

        for character in s:
            count[character] = count.get(character, 0) + 1
        
        for character in t:
            if character in count and count[character] > 0:
                count[character] -= 1
                if count[character] == 0:
                    count.pop(character)
            else:
                return False

        return not count