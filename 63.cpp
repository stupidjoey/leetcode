class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<int> mat(n,0);
        mat[0] = 1;
        
        for(int i = 0 ; i < m ; i++)
            for(int j = 0; j<n; j++){
                if(obstacleGrid[i][j]==1)
                    mat[j] = 0;
                else if (j > 0)
                    mat[j] = mat[j] + mat[j-1];
           
            }
        
        
        return mat[n-1];
        
    }
};