#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<vector<string> > result ;
    vector<vector<string> > solveNQueens(int n){
        vector<int> board(n,0) ;
        solve(board,0,n);
        return result;
    }


    void solve(vector<int> board, int row,int n){

        if (row == n){
            vector<string> str_board = transfer(board);
            result.push_back(str_board);
            return;
        }
        for(int col = 0 ; col < n; col++){
            if(isValid(board,row,col)){
                board[row] = col;
                solve(board,row+1,n);
            }
        }

        return;
    }



    vector<string>  transfer(vector<int> board){
        int n = board.size();
        vector<string> str_board;
        int col = 0;
        for(int row =0; row<n;row++)
        {
            string s(n,'.');
            col = board[row];
            s[col] = 'Q';
            str_board.push_back(s);
        }

        return str_board;
    }


    bool isValid(vector<int> board,int row,int col){

        for(int r = row-1; r>=0 ;r--)
        {
            if (board[r] == col || abs(r-row) == abs(board[r] - col) )
                return false;
        }
        return true;

    }

};


int main(){

    Solution sol;
    vector<vector<string> > result = sol.solveNQueens(4);
    int m = result.size();
    int n = result[0].size();
    for(int i =0; i<m;i++)
        for(int j =0 ; j<n;j++)
            cout << result[i][j]<<endl;
    return 0;
}