class Solution {
    List<List<Integer>> res;
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        res = new ArrayList<List<Integer>>();
        List<Integer> curr = new ArrayList();
        Backtrack(nums, target, curr, 0);
        return res;
    }
    public void Backtrack(int[] nums, int target, List<Integer> curr, int i){
        if(target == 0){
            res.add(new ArrayList(curr));
            return;
        }
        if(target < 0 || i >= nums.length){
            return;
        }
        curr.add(nums[i]);
        Backtrack(nums, target - nums[i], curr, i); // The element can be reused
        curr.remove(curr.size() - 1);
        Backtrack(nums, target, curr, i + 1);

    }
}
