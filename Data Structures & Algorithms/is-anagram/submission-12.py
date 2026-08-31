class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        character_count = {}

        for character in s:
            character_count[character] = character_count.get(character, 0) + 1

        for character in t:
            if character in character_count and character_count[character] > 0:
                character_count[character] -= 1
                if character_count[character] == 0:
                    character_count.pop(character)
            else:
                return False

        return not character_count