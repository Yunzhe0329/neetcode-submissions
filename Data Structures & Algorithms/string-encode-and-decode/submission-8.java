class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for(String s: strs){
            res.append(s.length()).append('#').append(s);
        }
        return res.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int l = 0;
        while(l < str.length()){
            int r = l;
            while(str.charAt(r) != '#'){
                r++;
            }
            // get the lenth of String
            int length = Integer.parseInt(str.substring(l, r));
            l = r + 1;
            r = l + length;
            res.add(str.substring(l, r));
            l = r;
        }
        return res;
    }
}
