class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int[][] pair = new int[position.length][2];

        for(int i = 0; i < position.length; i++){
            pair[i][0] = position[i];
            pair[i][1] = speed[i];
        }
        // Decending order -> close to the target[1st, 2nd...]
        Arrays.sort(pair, (a, b) -> b[0] - a[0]);
        Stack<Double> stack = new Stack<>();
        for(int[] p: pair){
            double curr_time = (double)(target - p[0]) / p[1];
            if(stack.isEmpty() || curr_time > stack.peek()){
                stack.push(curr_time);
            }
        }
        return stack.size();
    }
}
