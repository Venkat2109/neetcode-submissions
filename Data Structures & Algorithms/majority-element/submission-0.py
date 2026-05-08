class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=defaultdict(int)
        res=maxCount=0
        for n in nums:
            c[n]+=1
            if maxCount<c[n]:
                res=n
                maxCount=c[n]
        return res