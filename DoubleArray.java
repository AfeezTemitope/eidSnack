import java.util.*;

public class DoubleArray {
    public static void main(String... args) {
        int[] sample = {4, 5, 8};
        int[] result = doubleArray(sample);
        System.out.println("Input array: " + Arrays.toString(sample));
        System.out.println("Output array: " + Arrays.toString(result));
    }


 public static int[] doubleArray(int[] numbers) {
        int[] result = new int[numbers.length * 2];
        for (int i = 0; i < numbers.length; i++) {
            result[i] = numbers[i];
            result[i + numbers.length] = numbers[i] * 2;
        }
        return result;
    }




}