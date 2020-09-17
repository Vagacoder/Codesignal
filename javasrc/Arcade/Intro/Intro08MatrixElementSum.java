package javasrc.Arcade.Intro;

/*
 * Intro 08, Matrix Elements Sum
 * After becoming famous, the CodeBots decided to move into a new building together. 
 * Each of the rooms has a different cost, and some of them are free, but there's 
 * a rumour that all the free rooms are haunted! Since the CodeBots are quite 
 * superstitious, they refuse to stay in any of the free rooms, or any of the 
 * rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

Example

    For

    matrix = [[0, 1, 1, 2], 
              [0, 5, 0, 0], 
              [2, 0, 3, 3]]

    the output should be
    matrixElementsSum(matrix) = 9.
 */



public class Intro08MatrixElementSum {
    
    // TODO
    public static int matrixElementsSum(int[][] matrix){
        int rowN = matrix.length;
        int colN = matrix[0].length;

        int sum = 0;
        
        for(int c = 0; c < colN; c++){
            for(int r = 0; r < rowN; r++){
                if (matrix[r][c] == 0){
                    break;
                }
                sum += matrix[r][c];
            }
        }
        
        return sum;
    }

    public static void main(String[] args){
        int[][] room = {{0, 1, 1, 2},
                        {0, 5, 0, 0},
                        {2, 0, 3, 3}};

        System.out.printf("Expect: 9, result: %d\n", matrixElementsSum(room));

        int[][] room1 = {{1, 1, 1, 0},
                        {0, 5, 0, 1},
                        {2, 1, 3, 10}};

        System.out.printf("Expect: 9, result: %d\n", matrixElementsSum(room1));
    }
}
