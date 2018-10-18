class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        nums.sort()
        N = len(nums)
        for index in range(N):
            number = nums[index]
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            i, j = index+1, N-1
            while i < j:
                if nums[i] + nums[j] == -number:
                    result.append([number, nums[i], nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                if nums[i] + nums[j] > -number:
                    j -= 1
                if nums[i] + nums[j] < -number:
                    i += 1
        return result