class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int i : nums){
            result ^= i;
        }return result;
    }
}

class singleNumber{
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.singleNumber(new int[]{1,2,2,1,4}));
    }
}