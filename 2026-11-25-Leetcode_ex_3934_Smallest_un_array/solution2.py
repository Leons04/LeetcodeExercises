class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        l = 0
        subnumDic = {}
        for i in range(1,len(nums)):
            for space in range(len(nums) + 1 - i):
                subnums = nums[(0 + space):(i + space)]
                if (str(subnums) in subnumDic):
                    subnumDic[str(subnums)] += 1
                else:
                    subnumDic.update({str(subnums): 1})
        subnumDic.update({str(nums) : 1})

        for lst in subnumDic:
            if (subnumDic[lst] == 1):
                actList = lst.split(',')
                l = len(actList)
                break

        return l


if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestUniqueSubarray([3,3,3]))
    print(sol.smallestUniqueSubarray([2,1,2,3,3]))
    print(sol.smallestUniqueSubarray([1,1,2,2,1]))