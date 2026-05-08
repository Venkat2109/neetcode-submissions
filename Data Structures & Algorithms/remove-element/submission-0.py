class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        t=[]
        for i in nums:
            if i!=val:
                t.append(i)
        for i in range(len(t)):
            nums[i]=t[i]
        return len(t)