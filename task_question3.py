""" Given an array of integers nums and an integer target, return two numbers such that
# they add up to target. You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order."""

nums = [2, 17, 11, 7]
target = 9
nums_dict = {}
for i in range(len(nums)):
    if nums[i] in nums_dict:
        print(nums[nums_dict[nums[i]]], nums[i])
    else:
        nums_dict[target-nums[i]] = i
