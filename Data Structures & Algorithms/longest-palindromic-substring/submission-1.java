class Solution {
    public String longestPalindrome(String s) {
        int subLen= 0;
        int subStart = 0;
        for(int i = 0; i < s.length(); i++){
            // odd palindrome
            int l = i, r = i;
            while(l >=0 && r < s.length() && s.charAt(l) == s.charAt(r)){
                if(r - l + 1 > subLen){
                    subStart = l;
                    subLen = r - l + 1;
                }
                l--;
                r++;
            }

            l = i;
            r = i+1;
            while(l >=0 && r < s.length() && s.charAt(l) == s.charAt(r)){
                if(r - l + 1 > subLen){
                    subStart = l;
                    subLen = r - l + 1;
                }
                l--;
                r++;
            }
        }
        return s.substring(subStart, subStart + subLen);
        
    }
}
