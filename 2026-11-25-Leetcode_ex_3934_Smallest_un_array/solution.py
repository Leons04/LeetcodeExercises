class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        l = 0
        subnumList = []
        for i in range(1,len(nums)):
            for space in range(len(nums) + 1 - i):
                subnums = nums[(0 + space):(i + space)]
                subnumList.append(subnums)
        subnumList.append(nums)

        for lst in subnumList:
            tmpSubnumList = subnumList.copy()
            tmpSubnumList.remove(lst)
            if (not(lst in tmpSubnumList)):
                l = len(lst)
                break
        return l

if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestUniqueSubarray([3,3,3]))
    print(sol.smallestUniqueSubarray([2,1,2,3,3]))
    print(sol.smallestUniqueSubarray([1,1,2,2,1]))

