class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int[][] pairs = new int[position.length][2];
        for(int i = 0; i < position.length; i++){
            pairs[i][0] = position[i];
            pairs[i][1] = speed[i];
        }
        Arrays.sort(pairs, (a, b) -> b[0] - a[0]);
        int carFleet = 0;
        double latestTime = 0;
        for(int[] p: pairs){
            double curr_time = (double)(target - p[0]) / p[1];
            if(curr_time > latestTime){
                carFleet++;
                latestTime = curr_time;
            }
        }
        return carFleet;
    }
}