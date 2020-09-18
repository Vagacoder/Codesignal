package javasrc.Arcade.Intro;

/*
 * Intro 09. All Longest String
 * Given an array of strings, return another array containing all of its longest 
 * strings.

 * Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

 * Input/Output

    [execution time limit] 3 seconds (java)

    [input] array.string inputArray

    A non-empty array.

    Guaranteed constraints:
    1 ≤ inputArray.length ≤ 10,
    1 ≤ inputArray[i].length ≤ 10.

    [output] array.string

    Array of the longest strings, stored in the same order as in the inputArray.

 */

public class Intro09AllLongestString {

    // * Soluiotn 1
    public static String[] allLongestStrings(String[] inputArray) {

        int n = inputArray.length;
        int maxLength = inputArray[0].length();
        int count = 1;

        for (int i = 1; i < n; i++) {
            int curLength = inputArray[i].length();
            if (curLength > maxLength) {
                maxLength = curLength;
                count = 1;
            } else if (curLength == maxLength) {
                count++;
            }
        }

        String[] result = new String[count];
        int index = 0;
        for (int i = 0; i < n; i++) {
            int curLength = inputArray[i].length();
            if (curLength == maxLength) {
                result[index++] = inputArray[i];
            }
        }

        return result;
    }

    // * Solution 2, smart but there is a bug, what if string contains "-"
    public static String[] allLongestStrings2(String[] inputArray) {
        String l = "";

        for (String s : inputArray) {
            if (l.indexOf("-") == s.length()) {
                l += s + "-";
            } else if (l.indexOf("-") < s.length()) {
                l = s + "-";
            }
        }

        return l.split("-");
    }

    public static void main(String[] args) {
        String[] in1 = { "aba", "aa", "ad", "vcd", "aba" };
        String[] re1 = allLongestStrings(in1);
        for (String s : re1) {
            System.out.println(s);
        }

    }
}
