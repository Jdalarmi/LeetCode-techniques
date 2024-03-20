class Solution(object):
    def removeElement(self, nums, val):
        i = len(nums) -1
        while i >=0:
            if nums[i] == val:
                nums.pop(i)
            i -= 1             


solution = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
