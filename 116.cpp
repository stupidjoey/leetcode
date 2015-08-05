/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if(root == NULL)
            return ;
        TreeLinkNode *curnode = root;
        TreeLinkNode *crossnode = NULL;
        while(curnode->left)
        {
            crossnode = curnode;
            while(crossnode)
            {
                crossnode->left->next = crossnode->right;
                if(crossnode->next)
                    crossnode->right->next = crossnode->next->left;
                crossnode = crossnode->next;
            }
            curnode = curnode->left;
        }
        return;
}
};
