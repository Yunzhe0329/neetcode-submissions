class Solution {
    List<List<Integer>> res;
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        res = new ArrayList<List<Integer>>();
        List<Integer> curr = new ArrayList<>();
        backTracking(nums, target, curr, 0);
        return res;
    }
    public void backTracking(int[] nums, int target, List<Integer> curr, int i){
        if(target == 0){
            res.add(new ArrayList(curr));
            return;
        }
        if(target < 0 || i >= nums.length) return;
        
        curr.add(nums[i]);
        backTracking(nums, target - nums[i], curr, i);
        curr.remove(curr.size() - 1);
        backTracking(nums, target, curr, i + 1);
    }
}
