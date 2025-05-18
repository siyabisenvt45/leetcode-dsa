class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> obj = new Stack();
        obj.push(-1);
        int maxLength = 0;

        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) == '('){
                obj.push(i);
            }
            else{
                obj.pop();
                if(obj.isEmpty()){
                    obj.push(i);
                }
                else{
                    maxLength = Math.max(maxLength, i - obj.peek());
                }
            }
        }
        return maxLength;
    }
}