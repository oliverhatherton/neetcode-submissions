class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = {}
        t_list = {}

        for i in range(len(s)):
            if s[i] in s_list:
                s_list[s[i]] += 1
            else:
                s_list[s[i]] = 1

            if t[i] in t_list:
                t_list[t[i]] += 1
            else:
                t_list[t[i]] = 1

        return s_list == t_list
