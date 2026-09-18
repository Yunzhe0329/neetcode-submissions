class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        int longest = 0;
        for(int num: nums){
            numSet.add(num);
        }
        
        for(int i = 0; i < nums.length; i++){
            if(!numSet.contains(nums[i] - 1)){
                int length = 0;
                while(numSet.contains(nums[i] + length)){
                    length++;
                }
                longest = Math.max(longest, length);
            }
        }
        return longest;
    }
}
