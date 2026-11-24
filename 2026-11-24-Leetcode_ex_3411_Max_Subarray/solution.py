class Solution:

    def prod(self, list:list[int]) -> int:
        p = 1
        for i in list:
            p *= i
        return p

    def gcd(self, list:list[int]) -> int:
        gcd = 1

        for gcdtemp in range(1,max(list)):
            b = True
            for i in list:
                if (i % (gcdtemp) != 0):
                    b = False
            if (b):
                gcd = gcdtemp

        return gcd

    def lcm(self, list:list[int]) -> int:
        lcm = 1

        for lcmtemp in range(1, 1000000):
            b = True
            for i in list:
                if (lcmtemp % (i) != 0):
                    b = False
            if (b):
                lcm = lcmtemp
                break

        return lcm

    def maxLength(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            irev = len(nums) - i
            for space in range(len(nums)- irev):
                #print(space)
                subnums = nums[(0+space):(irev+space)]
                print(subnums)
                if (self.prod(subnums) == self.lcm(subnums) * self.gcd(subnums)):
                    subnums = subnums
                    #break
        print(subnums)
        return len(subnums)

if __name__ == "__main__":
    sol = Solution()
    #print(sol.gcd([1,12]))
    #print(sol.lcm([3,4,27]))
    print(sol.maxLength([1,2,1,2,1,1,1]))
    print(sol.maxLength([2,3,4,5,6]))
    print(sol.maxLength([1,2,3,1,4,5,1]))