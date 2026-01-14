public class Solution {
    public String longestCommonPrefix(String[] strs) {
        String[] input = strs;
        String output = input[0];

        for(String word : strs){
            output = findCommonPrefix(output, word);
        }

        return output;
    }

    public String findCommonPrefix (String str1, String str2){
        String output = "";
        for (int i = 0; i < Math.min(str1.length(), str2.length()); i++){
            if (str1.charAt(i) == str2.charAt(i)){
                output += str1.charAt(i);
            } else {
                break;
            }
        }
        return output;
    }
}
