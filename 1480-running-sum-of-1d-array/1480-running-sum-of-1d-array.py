class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        runSum = 0
        for i,num in enumerate(nums):
            runSum += num
            ans[i] = runSum
        
        return ans
        