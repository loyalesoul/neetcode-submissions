class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # A dictionary to store numbers seen so far and their indices.
        # Key: number, Value: index
        num_map = {}

        # Iterate through the list of numbers with their indices
        for i, num in enumerate(nums):
            # Calculate the 'complement' needed to reach the target
            complement = target - num

            # Check if the complement already exists in our map
            if complement in num_map:
                # If it does, we found the two numbers.
                # Return the index of the complement from the map and the current index 'i'.
                return [num_map[complement], i]
            
            # If the complement is not found, add the current number and its index to the map.
            # This prepares for future checks.
            num_map[num] = i
        
        # If no solution is found after checking all numbers (though the problem usually guarantees one)
        return []
        

