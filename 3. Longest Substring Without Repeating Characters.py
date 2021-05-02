class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = []
        prevlongest = 0
        for i in s:
            if i not in longest:
                longest.append(i)
            else:
                prevlongest = max(prevlongest, len(longest))
                longest = longest[longest.index(i)+1:]
                longest.append(i)
        return max(prevlongest, len(longest))
        