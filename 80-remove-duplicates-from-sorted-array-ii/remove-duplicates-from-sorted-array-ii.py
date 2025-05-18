class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        left = 2
        right = 2

        while right < len(nums):
            if nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1
            right += 1

        return left