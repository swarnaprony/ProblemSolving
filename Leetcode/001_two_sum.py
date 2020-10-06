# Sum of two indices

class Solution:
    def twoSum(self, nums, target):

        i = 0
        while i< len(nums):
            for j in range(len(nums)):
                if i < j:
                    if nums[i] + nums[j] == target:
                        indices = [i, j]
                        return indices
            i=i+1
mySolution = Solution()
num = [2, 7, 11, 15]
tar = 9
print(mySolution.twoSum(num, tar))
