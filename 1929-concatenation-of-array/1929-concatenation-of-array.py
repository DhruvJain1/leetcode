class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
    
#         n = len(nums)
#         ans = [] * 2*n
#         ans[0:n] = nums
#         ans[n:n*2] = nums
        
#         return ans