package javasrc.Arcade.Intro;

/*
 * Intro 05 Shape Area
 * Below we will define an n-interesting polygon. Your task is to find the area 
 * of a polygon for a given n.

    A 1-interesting polygon is just a square with a side of length 1. An 
    n-interesting polygon is obtained by taking the n - 1-interesting polygon 
    and appending 1-interesting polygons to its rim, side by side. 
    You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

    n = 1:

    O

    n = 2:

     O
    OOO
     O

    n = 3:

      O
     OOO
    OOOOO
     OOO
      O

 * Example

    For n = 2, the output should be
    shapeArea(n) = 5;
    For n = 3, the output should be
    shapeArea(n) = 13.

 * Input/Output

    [execution time limit] 3 seconds (java)

    [input] integer n

    Guaranteed constraints:
    1 ≤ n < 104.

    [output] integer

    The area of the n-interesting polygon.

 */
public class Intro05ShapeArea {
    
    public static int shapeArea(int n) {
        int sum = 0;
        for(int i = 1; i <=n; i++){
            sum +=(i*2-1);
        }
        return sum * 2 - (n*2-1);
    }

    public static void main(String[] args){

        int[] ns =      {1, 2, 3, 5, 7000, 8000};
        int[] areas =   {1, 5, 13, 41, 97986001, 127984001};
        for(int i = 0; i < ns.length; i++){
            System.out.printf("For n = %d, expected: %d, result: %d\n", 
                ns[i], areas[i], shapeArea(ns[i]));
        }
    }
}
