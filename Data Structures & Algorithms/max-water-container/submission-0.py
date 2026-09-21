class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        curr_max = 0
        curr_height = min(heights[i], heights[j])
        curr_max = curr_height * (j-i)
        while i < j:
            new_height = min(heights[i], heights[j])
            if new_height > curr_height:
                curr_area = new_height * (j-i)
                curr_max = max(curr_max, curr_area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return curr_max                