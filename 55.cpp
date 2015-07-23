class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int max_idx = 0;
        for(int idx = 0; idx < n-1 ;idx++){
            int step = nums[idx];
            if (step + idx > max_idx)
                max_idx = step + idx;
            if (idx == max_idx)
                return false;
        }
        
        return true;
    }
};