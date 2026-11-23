class Solution:

    def isValid(self, s: str) -> bool:
        mem = []
        tempBool = True
        for c in s:
            match c:
                case "(":
                    mem.append("(")
                case "{":
                    mem.append("{")
                case "[":
                    mem.append("[")
                case ")":
                    if(mem != [] and mem[-1] == "("):
                        mem.pop()
                    else:
                        tempBool = False
                        break
                case "}":
                    if (mem != [] and mem[-1] == "{"):
                        mem.pop()
                    else:
                        tempBool = False
                        break
                case "]":
                    if (mem != [] and mem[-1] == "["):
                        mem.pop()
                    else:
                        tempBool = False
                        break

        return bool(tempBool and mem == [])

if __name__ == "__main__":
    sol = Solution()

    print(sol.isValid("()"))
    print(sol.isValid("()[]{}"))
    print(sol.isValid("(]"))
    print(sol.isValid("([])"))
    print(sol.isValid("([)]"))

    print(sol.isValid(""))
    print(sol.isValid("]"))