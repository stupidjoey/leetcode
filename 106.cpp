/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int n = inorder.size();
        int m = postorder.size();
        if (m !=n)
            return NULL;
        return buildTreeHelper(inorder, postorder, 0,  n-1,  0,  n-1);
    }
        
    TreeNode* buildTreeHelper(vector<int>& inorder, vector<int>& postorder, int is, int ie, int ps, int pe){
        
        if(is > ie || ps > pe)
            return NULL;
        
        int rootval = postorder[pe];
        
        int pos =0 ;
        for(int i = is; i <= ie; i++){
            if(inorder[i] == rootval){
                pos = i;
                break;
            }
            
        }
        
        
        TreeNode* root = new TreeNode(rootval);
        root->right = buildTreeHelper(inorder,postorder,pos+1,ie,ps+pos-is,pe-1);
        root->left = buildTreeHelper(inorder,postorder,is,pos-1,ps,ps+pos-is-1);
        
        
        return root;
    }
        
    
};