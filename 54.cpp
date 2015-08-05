#include <vector>
#include <iostream>
using namespace std;



class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        int m = matrix.size();
        int n = matrix[0].size();
        if( m == 0 || n == 0)
            return result;
            
        int count = 1;
        int i = 0 ;
        int j = 0 ;
        int row = 0;
        int span = n;
        while (count <= m*n)
        {
            i = row;
            j = row;
            
            // left to right
            for(;j<=row+span-1;j++)
            {
 
                result.push_back(matrix[i][j]);
                count++;
            }
            j--;
            
            // down 

            for(++i;i<=row+span-1;i++)
            {
                result.push_back(matrix[i][j]);
                count++;
            }
            i--;
            
            // right to left
            for(--j;j>=row;j--)
            {
                result.push_back(matrix[i][j]);
                count++;
            }
            j++;
            
            // up
            for(--i;i>=row+1;i--)
            {
                result.push_back(matrix[i][j]);
                count++;
            }
            
            row++;
            span -= 2;
            
        }
        
        return result;
        
        
    }
};


int main()
{
    Solution sol = new Solution();
    vector<vector<int>> matrix;
    matrix = {};
    cout<< sol.spiralOrder(matrix)<<endl;
    return 0;
}