class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int count = 0;
        int max = 0;
        int nextmax = 0;
        for(int i = 0 ; i<n-1;i++){
            if (nums[i]+i >= nextmax)
                nextmax = nums[i]+i;
            if (i == max)
            {
                max = nextmax;
                nextmax = 0;
                count++;
            }
        }
        return count;
        
    }
};