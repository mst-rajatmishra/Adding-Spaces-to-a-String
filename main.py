class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        prev_index = 0
        
        for index in spaces:
            result.append(s[prev_index:index])  # Add the substring before the space
            result.append(" ")  # Add the space
            prev_index = index  # Move the pointer to the next part of the string
        
        # Add the remaining part of the string after the last space index
        result.append(s[prev_index:])
        
        return ''.join(result)  # Join all parts to form the final string
