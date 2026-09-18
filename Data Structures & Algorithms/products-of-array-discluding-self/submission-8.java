class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int prefix = 1, postfix = 1;
        int[] res = new int[n];
        Arrays.fill(res, 1);

        for(int i = 0; i < n; i++){
            res[i] = prefix;
            prefix *= nums[i];
        }

        for(int i = n - 1; i >= 0; i--){
            res[i] *= postfix;
            postfix *= nums[i];
        }
        return res;
    }
}  
