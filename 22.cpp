# include <iostream>
# include <vector>
using namespace std;


class Solution {

public:
    vector<string> result;

    vector<string> generateParenthesis(int n) {
        string curStr;
        helper(curStr,0,0,n);
        return result;
    }

    void helper(string curStr, int leftCount, int rightCount,int n){
        if (leftCount == n){
            if(rightCount == n){
                result.push_back(curStr);
                return;
            }
            else{
                curStr += ')';
                helper(curStr,leftCount,++rightCount,n);
            }
        }
        else{
            string curStr1 = curStr;
            curStr1 += '(';
            int cur_leftCount = leftCount;
            helper(curStr1,++cur_leftCount,rightCount,n);

            if(leftCount > rightCount){
                string curStr2 = curStr;
                curStr2 +=')';
                helper(curStr2,leftCount,++rightCount,n);
            }
        }

    }


};


int main(){

    Solution sol;
    vector<string>  result = sol.generateParenthesis(4);
    for(vector<string>::iterator it = result.begin(); it != result.end(); ++it)
        cout<< *it<<endl;

}