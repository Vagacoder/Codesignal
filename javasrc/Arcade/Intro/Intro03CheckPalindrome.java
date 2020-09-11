package javasrc.Arcade.Intro;

/*
 * Intro 03, Check Palindrome
 * Given the string, check if it is a palindrome.

 * Example

    For inputString = "aabaa", the output should be
    checkPalindrome(inputString) = true;
    For inputString = "abac", the output should be
    checkPalindrome(inputString) = false;
    For inputString = "a", the output should be
    checkPalindrome(inputString) = true.

 * Input/Output

    [execution time limit] 3 seconds (java)

    [input] string inputString

    A non-empty string consisting of lowercase characters.

    Guaranteed constraints:
    1 ≤ inputString.length ≤ 105.

    [output] boolean

    true if inputString is a palindrome, false otherwise.

 */

public class Intro03CheckPalindrome {
    
    // * Solution #1, recursive 
    public static boolean checkPalindrome1(String inputString) {
        int n = inputString.length();
        
        if(n <= 1){
            return true;
        } 
        
        if(inputString.charAt(0) != inputString.charAt(n-1)){
            return false;
        }
        
        return checkPalindrome1(inputString.substring(1, n-1));
    }


    // * Solution #2,
    public static boolean checkPalindrome2(String inputString) {
        return inputString.equals(new StringBuilder(inputString).reverse().toString());
    }

    
    public static void main(String[] args){
        String[] strs = {"aabaa", "abac", "a", "az", "abacaba", "z", "aaabaaaa", 
                                "zzzazzazz", "hlbeeykoqqqqokyeeblh", "hlbeeykoqqqokyeeblh"};
        boolean[] expected = {true, false, true, false, true, true, false, false, true, true};

        int n = strs.length;
        
        for(int i = 0; i < n; i++){
            boolean result = checkPalindrome2(strs[i]);
            if(result == expected[i]){
                System.out.printf("Test #%d is passed\n", i);
            }else{
                System.out.printf("Test #%d is failed, expected: %s, result: %s",
                i, ""+expected[i], ""+result);
            }
        }
    }
    
}
