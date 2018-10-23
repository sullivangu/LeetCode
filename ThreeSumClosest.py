class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = nums[0] + nums[1] + nums[2]
        distance = abs(result - target)
        nums.sort()
        N = len(nums)
        for index in range(N):
            number = nums[index]
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            i, j = index+1, N-1
            while i < j:
                orgDistance = nums[i] + nums[j] + number - target
                newDistance = abs(orgDistance)
                if newDistance == 0:
                    return target
                if newDistance < distance:
                    distance = newDistance
                    result = nums[i] + nums[j] + number
                if orgDistance > 0:
                    j -= 1
                if orgDistance < 0:
                    i += 1

        return result