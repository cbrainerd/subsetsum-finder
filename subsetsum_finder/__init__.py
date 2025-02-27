from typing import Optional

def combination_sum(nums: list[int], target: int, max_length: Optional[int]= None):
    """
    Find all unique combinations in the input list that sum up to the target.

    Args:
        nums (list of int): The list of integers to find combinations from.
        target (int): The target sum for the combinations.
        max_length (int, optional): If specified, only combinations up to this length will be considered.

    Returns:
        list of list of int: A list of lists, where each inner list is a unique combination of numbers that sum up to the target.

    Example:
        >>> combination_sum([2, 3, 6, 7], 7)
        [[7], [2, 2, 3]]

    Originally generated with the assistance of ChatGPT (https://openai.com)
    """
    result = []
    nums.sort()  # Sort the input list to ensure uniqueness

    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])  # Found a valid combination
            return
        for i in range(start, len(nums)):
            if nums[i] > target:
                break  # No need to continue if the number exceeds target
            if i > start and nums[i] == nums[i - 1]:
                continue  # Skip duplicates to ensure uniqueness
            backtrack(
                i + 1, target - nums[i], path + [nums[i]]
            )  # Move to the next number

    backtrack(0, target, [])
    return result
