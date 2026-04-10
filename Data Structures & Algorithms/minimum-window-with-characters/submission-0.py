from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}

        required = len(need)
        formed = 0

        l = 0
        res = (float("inf"), 0, 0)

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                formed += 1

            # shrink when valid
            while formed == required:
                if (r - l + 1) < res[0]:
                    res = (r - l + 1, l, r)

                left_char = s[l]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                l += 1

        return "" if res[0] == float("inf") else s[res[1]:res[2]+1]