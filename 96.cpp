#include <iostream>
#include <cstring> 
using namespace std;

class Solution {
public:
    int numTrees(int n) {
        int A[n+2][n+2];
        memset(A,0,sizeof(A));
        for(int j =1; j<=n;j++){
            A[j+1][j] = 1;
            A[j][j] = 1;
        }
        for(int i =1;i<=n;i++){
            A[i][i-1] = 1;
        }
        
        // for(int i =0;i<=n+1;i++){
        //     for(int j =0;j<=n+1;j++){
        //         cout<<i<<' '<<j<<' '<<A[i][j]<<endl;
        //     }
        // }

        int j = 0;
        for(int k=1;k<=n-1;k++)
        {
            for(int i=1;i<=n-k;i++)
            {
                j = i+k;
                for(int s = i; s<=j;s++)
                {
                    A[i][j] += A[i][s-1]*A[s+1][j];
                    cout<<s<<' '<<i<<' '<<j<<' '<<A[i][j]<<endl;
                }
                cout<<i<<' '<<j<<' '<<A[i][j]<<endl;
            }
        }
        
        return A[1][n];
        
    }

    // new solution

    int numTrees(int n) {
        int store[n+1];
        memset(store,0,sizeof(store));
        store[0] = 1;
        store[1] = 1;
        
        for(int i =2; i<=n;i++)
        {
            for(int j = 1; j<=i;j++)
            {
                store[i] += store[j-1]*store[i-j];
            }
            
        }
        
        return store[n];
        
    }

};

int main()
{
    Solution sol;
    sol.numTrees(3);
    return 0;
}