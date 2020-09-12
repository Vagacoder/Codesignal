package javasrc.Arcade.Intro;

/* 
 * Intro 04 Adjacent Elements Product
 * Given an array of integers, find the pair of adjacent elements that has the 
 * largest product and return that product.

 * Example

    For inputArray = [3, 6, -2, -5, 7, 3], the output should be
    adjacentElementsProduct(inputArray) = 21.

    7 and 3 produce the largest product.

 * Input/Output

    [execution time limit] 3 seconds (java)

    [input] array.integer inputArray

    An array of integers containing at least two elements.

    Guaranteed constraints:
    2 ≤ inputArray.length ≤ 10,
    -1000 ≤ inputArray[i] ≤ 1000.

    [output] integer

    The largest product of adjacent elements.

 */

public class Intro04AdjacentElementsProduct {
    
    public static int adjacentElementsProduct(int[] inputArray) {
        int n = inputArray.length;
        
        int max = inputArray[0] * inputArray[1];
    
        for(int i = 1; i < n-1; i++){
            int product = inputArray[i] * inputArray[i+1];
            if(product > max){
                max = product;
            }
        }
        return max;
    }
    
    public static void main(String[] args){
        int[] a1 = {3, 6, -2, -5, 7, 3};
        int r1 = adjacentElementsProduct(a1);
        System.out.printf("Expected: %d, result: %d\n", 21, r1);
        
        int[] a2 = {-1, -2};
        int r2 = adjacentElementsProduct(a2);
        System.out.printf("Expected: %d, result: %d\n", 2, r2);
                
        int[] a3 = {5, 1, 2, 3, 1, 4};
        int r3 = adjacentElementsProduct(a3);
        System.out.printf("Expected: %d, result: %d\n", 6, r3);
                
        int[] a4 = {1, 2, 3, 0};
        int r4 = adjacentElementsProduct(a4);
        System.out.printf("Expected: %d, result: %d\n", 6, r4);

        int[] a5 = {1, 0, 1, 0, 1000};
        int r5 = adjacentElementsProduct(a5);
        System.out.printf("Expected: %d, result: %d\n", 0, r5);
    }
}
