class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        int low = 0;
        int high = n - 1;
        int mid = 0;
        int index = -1;
        while (low <= high){
            mid = low + (high - low)/2;
            if(nums[mid] < target)
                low = mid+1;
            else if (nums[mid] == target)
            {
                index = mid;
                break;
            }
            else
                high = mid - 1;
        }
        
        if (index != -1){
            int startIndex = mid;
            while(startIndex>0 && nums[startIndex-1] == target)
                startIndex--;
            int endIndex = mid;
            while(endIndex<n-1 && nums[endIndex+1] == target)
                endIndex++;
            return vector<int>{startIndex,endIndex};
        }
        else
            return vector<int>{-1,-1};
    }
};