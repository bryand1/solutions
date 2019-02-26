#include <bits/stdc++.h>

using namespace std;

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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        if (root == NULL) return res;

        stack<TreeNode*> s { root };

        TreeNode *curr;
        while (!s.empty()) {
            curr = s.top();
            s.pop();
            res.push_back(curr->val);
            if (curr->right) s.push(curr->right);
            if (curr->left) s.push(curr->left);
        }
        return res;
    }
};