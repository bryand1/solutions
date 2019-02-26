/**
 * 145. Binary Tree Postorder Traversal
 * 
 * The recursive solution is trivial. Can you do it iteratively?
 * 
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;

        if (root == NULL) return res;

        stack<TreeNode*> s1;
        stack<TreeNode*> s2;

        s1.push(root);

        TreeNode *curr;
        while (!s1.empty()) {
            curr = s1.top();
            s1.pop();
            s2.push(curr);
            if (curr->left != NULL) s1.push(curr->left);
            if (curr->right != NULL) s1.push(curr->right);
        }
        
        while (!s2.empty()) {
            curr = s2.top();
            res.push_back(curr->val);
            s2.pop();
        }
        return res;
    }
};
