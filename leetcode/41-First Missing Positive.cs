public class Solution {
    public int FirstMissingPositive(int[] nums) {

        int n = nums.Length;
        int range = n+1;
        for(int i = 0; i<n; i++ ){
            if(nums[i]<0 || nums[i] > n){
                nums[i]=0;
            }
        }
        int s = 0;
        int index = 0;
        for(int i = 0; i<n; i++){
            if (0< nums[i] % range) {
                index = nums[i]%range;
                nums[index-1]+=range;
            }
        }
        for(int i = 0; i<n; i++){
            if (nums[i]<range){
                return i+1;
            }
        }
        return range;
    }
}