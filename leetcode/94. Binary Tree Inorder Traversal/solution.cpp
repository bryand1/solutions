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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        if (root == NULL) return res;

        stack<TreeNode*> s;

        while (1) {
            if (root != NULL) {
                s.push(root);
                root = root->left;
            } else {
                if (s.empty()) break;
                root = s.top();
                res.push_back(root->val);
                s.pop();
                root = root->right;
            }
        }

        return res;
    }
};