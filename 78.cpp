class Solution {
public:

    
    vector<vector<int>> subsets(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> result;
        result.push_back({});
        int n = nums.size();
        for (int i = 0 ;i < n; i++){
            
            vector<vector<int>> tempRes = result;
            int m = tempRes.size();
            
            for(int j =0; j< m;j++){
                
                tempRes[j].push_back(nums[i]);
                result.push_back(tempRes[j]);

            }
            
        }
        
        
        return result;
    }

    // bit manipulation
    vector<vector<int>> subsets(vector<int>& nums) {
        int numSize = nums.size();
        int allSize = pow(2, numSize);
        sort(nums.begin(),nums.end());
        
        vector<vector<int>> result(allSize, vector<int>());
        
        for(int i = 0 ; i < numSize; i++)
            for(int j =0;j < allSize; j++){
                if ((j >>i)&1)
                    result[j].push_back(nums[i]);
            }
        
        return result;
        
    }


};