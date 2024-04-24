import java.util.*;

public class EvenOddToBoolean {
    public static void main(String... args) {
        int[] number = {4, 5, 8, 8, 8, 2, 9};
        boolean[] result = toBoolean(number);
        System.out.println("Input array: " + Arrays.toString(number));
        System.out.println("Output array: " + Arrays.toString(result));
    }

    public static boolean[] toBoolean(int[] numbers) {
        boolean[] result = new boolean[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            result[i] = numbers[i] % 2 != 0;
        }
        return result;
    }
}