class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Create the answer variable for return
        answer = ""
        # Take strs[0] as the one to check against all others
        for i in range(len(strs[0])):
            # Loop through all to check if it is in the matching prefix
            for j in range(1, len(strs)):
                # Check if we are at the end of any str or any mismatching
                if (i >= len(strs[j])) or (strs[0][i] != strs[j][i]):
                    return answer
            # If not break, it means matching, add to the answer
            answer += strs[0][i]
        # Return the answer
        return answer