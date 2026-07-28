class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        total_water = 0

        while left < right:
            if max_left <= max_right:
                left += 1
                h = height[left]
                if h < max_left:
                    total_water += max_left - h
                else:
                    max_left = h
            else:
                right -= 1
                h = height[right]
                if h < max_right:
                    total_water += max_right - h
                else:
                    max_right = h

        return total_water