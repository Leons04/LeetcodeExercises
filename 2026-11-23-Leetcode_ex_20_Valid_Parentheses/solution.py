class Solution:
    def isValid(self, s: str) -> bool:

        numRoundBrackets = 0
        numFancyBrackets = 0
        numSquaredBrackets = 0

        for c in s:
            match c:
                case "(":
                    numRoundBrackets+=1
                    break
                case "{":
                    numFancyBrackets+=1
                    break
                case "[":
                    numSquaredBrackets+=1
                    break
                case ")":
                    numRoundBrackets-=1
                    break
                case "}":
                    numFancyBrackets-=1
                    break
                case "]":
                    numSquaredBrackets-=1
                    break

        return numRoundBrackets == 0 and numFancyBrackets==0 and numSquaredBrackets==0