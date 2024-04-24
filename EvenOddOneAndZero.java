import java.util.*;

public class EvenOddOneAndZero {
    public static void main(String[] args) {
        int[] inputArray = {4, 5, 8, 8, 8, 2, 9};
        int[] outputArray = evenOdd(inputArray);
        System.out.println("Input array: " + Arrays.toString(inputArray));
        System.out.println("Output array: " + Arrays.toString(outputArray));
    }

    public static int[] evenOdd(int[] arr) {
        int[] result = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            result[i] = (arr[i] % 2 == 0) ? 0 : 1;
        }
        return result;
    }
}
