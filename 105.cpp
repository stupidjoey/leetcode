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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int m = preorder.size();
        int n = inorder.size();
        if(m!=n)
            return NULL;
        
        return buildTreeHelper(preorder,inorder,0,n-1,0,n-1);
    }
    
    
    TreeNode* buildTreeHelper(vector<int>& preorder, vector<int>& inorder,int ps,int pe, int is, int ie){
        
        if (ps>pe||is>ie)
            return NULL;
        
        int rootval = preorder[ps];
        TreeNode* root = new TreeNode(rootval);
        int pos = 0;
        for(int i = is; i <=ie; i++){
            if(inorder[i]==rootval){
                pos = i;
                break;
            }
        }
        
        root->left = buildTreeHelper(preorder,inorder,ps+1,ps+pos-is,is,pos-1);
        root->right = buildTreeHelper(preorder,inorder,ps+pos-is+1,pe,pos+1,ie);
        return root;
        
    }
    
};