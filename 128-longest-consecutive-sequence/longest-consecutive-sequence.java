class Solution {
    public int longestConsecutive(int[] arr) {
        if(arr.length ==0){
            return 0;
        }

        Set<Integer> set = new HashSet<>();

        for(int i = 0; i<arr.length; i++){
            set.add(arr[i]);
        }

        int count =1;
        int maxCount =1;
        for(int element : set){
            if(!set.contains(element-1)){
                count =1;
                while(set.contains(element+1)){
                    ++count;
                    ++element;
                }
            }

            if(count> maxCount){
                maxCount = count;
            }
        }


        return maxCount;
    }
}