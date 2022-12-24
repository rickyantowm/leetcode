class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = {}
        
        for i in range(len(nums)):
            cari = target - nums[i]
            if cari in mp:
                return i, mp[cari]
            else:
                mp[nums[i]] = i
                