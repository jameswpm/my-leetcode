class Solution {
    public int[] twoSum(int[] nums, int target) {
        int lenght = nums.length;
        int[] sol = new int[2];
        for (int i = 0; i <= lenght-1; i++) {
            for (int j = i+1; j <= lenght-1; j++) {
                int sum = nums[i] + nums[j];
                
                if (sum == target) {
                    
                    sol[0] = i;
                    sol[1] = j;
                    

                }
            }
        }
        return sol; 
    }
}