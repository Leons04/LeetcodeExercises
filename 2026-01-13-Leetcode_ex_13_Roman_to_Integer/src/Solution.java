class Solution {
    public int romanToInt(String s) {
        String input = s;
        int output = 0;

        for (int i = 0; i < s.length(); i++){
            switch (input.charAt(i)){
                case 'M':
                    output += 1000;
                    break;
                case 'D':
                    output += 500;
                    break;
                case 'C':
                    if (i < s.length() - 1) {
                        if (input.charAt(i+1) == 'I' || input.charAt(i+1) == 'V' || input.charAt(i+1) == 'X' || input.charAt(i+1) == 'L' || input.charAt(i+1) == 'C') {
                            output += 100;
                        } else {
                            output -= 100;
                        }
                        break;
                    } else {
                        output += 100;
                    }
                    break;
                case 'L':
                    output += 50;
                    break;
                case 'X':
                    if (i < s.length() - 1) {
                        if (input.charAt(i+1) == 'X' || input.charAt(i+1) == 'V' || input.charAt(i+1) == 'I' || input.charAt(i+1) == 'D' || input.charAt(i+1) == 'M') {
                            output += 10;
                        } else {
                            output -= 10;
                        }
                        break;
                    } else {
                        output += 10;
                    }
                    break;
                case 'V':
                    output += 5;
                    break;
                case 'I':
                    if (i < s.length() - 1) {
                        if (input.charAt(i+1) == 'I' || input.charAt(i+1) == 'L' || input.charAt(i+1) == 'C' || input.charAt(i+1) == 'D' || input.charAt(i+1) == 'M') {
                            output++;
                        } else {
                            output--;
                        }
                        break;
                    } else {
                        output++;
                    }
                    break;
                default:
                    break;
            }
        }
        return output;
    }
}
