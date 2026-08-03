class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Create two pointers, one for each of the string
        ps = 0
        pt = 0
        
        # Transverse to see if s is a subsequence of t
        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
        
        # While loop break: either a subsequence or not
        if ps == len(s):
            return True
        return False