package javasrc.Arcade.Intro;

/*
 * Intro 07. Almost Incereasing Sequence
 * Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

 * Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

 * Example

    For sequence = [1, 3, 2, 1], the output should be
    almostIncreasingSequence(sequence) = false.

    There is no one element in this array that can be removed in order to get a strictly increasing sequence.

    For sequence = [1, 3, 2], the output should be
    almostIncreasingSequence(sequence) = true.

    You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

 * Input/Output

    [execution time limit] 3 seconds (java)

    [input] array.integer sequence

    Guaranteed constraints:
    2 ≤ sequence.length ≤ 105,
    -105 ≤ sequence[i] ≤ 105.

    [output] boolean

    Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.

 */
public class Intro07AlmostIncreaseSeq {

    // * Solution # 1
    public static boolean almostIncreasingSequence(int[] sequence) {
        int n = sequence.length;

        for (int i = 0; i < n - 1; i++) {
            if (sequence[i] >= sequence[i + 1]) {
                int[] temp1 = new int[n - 1];
                for (int j = 0; j < n - 1; j++) {
                    if (j < i) {
                        temp1[j] = sequence[j];
                    } else {
                        temp1[j] = sequence[j + 1];
                    }
                }

                int[] temp2 = new int[n - 1];
                for (int j = 0; j < n - 1; j++) {
                    if (j <= i) {
                        temp2[j] = sequence[j];
                    } else {
                        temp2[j] = sequence[j + 1];
                    }
                }

                if (!isIncreasing(temp1) && !isIncreasing(temp2)) {
                    return false;
                }
            }
        }

        return true;
    }

    private static boolean isIncreasing(int[] s){
        for(int i = 0; i < s.length-1; i++){
            if(s[i] >= s[i+1]){
                return false;
            }
        }
        return true;
    }

    // * Solution # 2
    public static boolean almostIncreasingSequence1(int[] sequence) {
        int numErr = 0;
        for (int i = 0; i < sequence.length - 1; i++) {
            if (sequence[i] - sequence[i+1] >= 0) {
                numErr += 1;
                if (i - 1 >= 0 && i + 2 <= sequence.length - 1
                   && sequence[i] >= sequence[i+2]
                   && sequence[i-1] >= sequence[i+1] ) {
                    return false;
                }
            }
        }
        
        return numErr <= 1;
    }

    public static void main(String[] args){
        int[] a1 = {1, 3, 2, 1};
        boolean r1 = almostIncreasingSequence1(a1);
        System.out.println(r1);

        int[] a2 = {1, 3, 2};
        boolean r2 = almostIncreasingSequence1(a2);
        System.out.println(r2);

        int[] a3 = {10, 1, 2, 3, 4, 5};
        boolean r3 = almostIncreasingSequence1(a3);
        System.out.println(r3);
    }
}
