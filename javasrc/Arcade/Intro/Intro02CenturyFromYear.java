package javasrc.Arcade.Intro;

/*
 * Intro 02, Century From Year
 * Given a year, return the century it is in. The first century spans from the 
 * year 1 up to and including the year 100, the second - from the year 101 up to 
 * and including the year 200, etc.
 * 
 * Example
 *
 *  For year = 1905, the output should be
 *  centuryFromYear(year) = 20;
 *  For year = 1700, the output should be
 *  centuryFromYear(year) = 17.
 * 
 * Input/Output

 *  [execution time limit] 3 seconds (java)

 *  [input] integer year

 *  A positive integer, designating the year.

 *  Guaranteed constraints:
 *  1 ≤ year ≤ 2005.

 *  [output] integer

 *  The number of the century the year is in.

*/


public class Intro02CenturyFromYear{

    // * Solution #1
    public static int centuryFromYear1(int year) {
        return (int) Math.ceil(year*1.0/100);
    }

    // * Solution #2
    public static int centuryFromYear2(int year){
        return 1 + (year - 1)/100;
    }

    // * Solution #3
    public static int centuryFromYear3(int year){
        return (year + 99)/100;
    }

    public static void main(String[] args){
        int[] years = {1905, 1700, 1988, 2000, 2001, 200, 374, 45, 8, 1};
        int[] expected = {20, 17, 20, 20, 21, 2, 4, 1, 1, 1};

        int n = years.length;
        for(int i = 0; i < n; i++){
            int result = centuryFromYear3(years[i]);
            if(result == expected[i]){
                System.out.printf("Test #%d is passed\n", i );
            }else {
                System.out.printf("Test #%d (%d) is failed, expected: %d, result: %d", 
                    i, years[i], expected[i], result);
            }
        }
    }
}