class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        
        for(int num: nums){
            numSet.add(num);
        }
        int longest = 0;

        for(int i = 0; i < nums.length; i++){
            if(!numSet.contains(nums[i] - 1)){
                int length = 0;
                while(numSet.contains(nums[i] + length)){
                    length += 1;
                }
                longest = Math.max(longest, length);
            }
        }
        return longest;
    }
}
