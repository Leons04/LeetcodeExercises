class Solution:

    def prod(self, list:list[int]) -> int:
        p = 1
        for i in list:
            p *= i
        return p

    def gcd(self, list:list[int]) -> int:
        gcd = 1

        for h in range(0,max(list)):
            gcdtemp = max(list) - h
            b = True
            for i in list:
                if (i % (gcdtemp) != 0):
                    b = False
            if (b):
                gcd = gcdtemp
                return gcd

    def lcm(self, list:list[int]) -> int:
        lcm = 1

        for lcmtemp in range(1, 10000):
            b = True
            for i in list:
                if (lcmtemp % (i) != 0):
                    b = False
            if (b):
                lcm = lcmtemp
                return lcm

    def maxLength(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            irev = len(nums) - i
            for space in range(len(nums) + 1 - irev):
                subnums = nums[(0+space):(irev+space)]
                if (self.prod(subnums) == self.lcm(subnums) * self.gcd(subnums)):
                    return len(subnums)

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxLength([3,7,1,8,9,5]))
    print(sol.maxLength([6,1,6,5,1,5,4,3,1,1,9,9,5,1,1,2,1,8,9,5,3,2,7,5,1,3,9,10,9,7,3,10,6,1,2,9,9,8,2,1,4,3,3,3,4,6,1,3,9,6]))
