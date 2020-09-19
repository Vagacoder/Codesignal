package javasrc.Arcade.Intro;

/*
 * Intro 10. Common Character Count
 * 
 * Given two strings, find the number of common characters between them.

 * Example
 
 For s1 = "aabcc" and s2 = "adcaa", the output should be
 commonCharacterCount(s1, s2) = 3.
 
Strings have 3 common characters - 2 "a"s and 1 "c".

* Input/Output

[execution time limit] 3 seconds (java)

[input] string s1

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length < 15.

[input] string s2

    A string consisting of lowercase English letters.
    
    Guaranteed constraints:
    1 ≤ s2.length < 15.
    
    [output] integer

    */

import java.util.HashMap;

public class Intro10CommonCharacterCount {

    // * Solution 1
    public static int commonCharacterCount(String s1, String s2) {
        int n1 = s1.length();
        int n2 = s2.length();

        HashMap<Integer, Integer> map1 = new HashMap<>();
        HashMap<Integer, Integer> map2 = new HashMap<>();

        for (int i = 0; i < n1; i++) {
            int c = s1.charAt(i);
            if (map1.containsKey(c)) {
                map1.put(c, map1.get(c) + 1);
            } else {
                map1.put(c, 1);
            }
        }

        for (int i = 0; i < n2; i++) {
            int c = s2.charAt(i);
            if (map2.containsKey(c)) {
                map2.put(c, map2.get(c) + 1);
            } else {
                map2.put(c, 1);
            }
        }

        int count = 0;
        for (Integer key : map1.keySet()) {
            if (map2.containsKey(key)) {
                count += Math.min(map1.get(key), map2.get(key));
            }
        }

        return count;
    }

    // * Solution 2
    public static int commonCharacterCount1(String s1, String s2) {
        int[] a = new int[26], b = new int[26];
        for (char c : s1.toCharArray())
            a[c - 'a']++;
        for (char c : s2.toCharArray())
            b[c - 'a']++;
        int s = 0;
        for (int i = 0; i < 26; ++i)
            s += Math.min(a[i], b[i]);
        return s;
    }

    public static void main(String[] args) {
        String s1 = "aabcc";
        String s2 = "adcaa";
        int count = commonCharacterCount(s1, s2);
        System.out.printf("Expect: 3, result: %d\n", count);
    }
}
