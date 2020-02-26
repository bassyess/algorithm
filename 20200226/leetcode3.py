'''
3. 无重复最长子串
思路：滑动窗口+双指针
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        if not s:
            return 0
        if len(s)==1:
            return 1
        left, right, counter= 0, 0, 0
        maxLen = 0
        windows = defaultdict(int)
        while right<len(s):
            if windows[s[right]]>0:
                counter += 1
            windows[s[right]] += 1
            right += 1
            while counter:
                if windows[s[left]]>1:
                    counter -= 1
                windows[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, right-left)
        return maxLen