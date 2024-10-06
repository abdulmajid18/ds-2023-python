public class Solution {
    public int getSum(int a, int b) {
        // Loop until there is no carry
        while (b != 0) {
            // Calculate the sum without carry
            int sum = a ^ b; // Bitwise XOR to add without carrying

            // Calculate the carry
            int carry = (a & b) << 1; // Bitwise AND and shift left to calculate carry

            // Update a and b for the next iteration
            a = sum;
            b = carry;
        }

        return a; // Return the computed sum
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int a = 1;
        int b = 2;
        int result = solution.getSum(a, b);
        System.out.println("Sum: " + result); // Output: Sum: 3
    }
}
