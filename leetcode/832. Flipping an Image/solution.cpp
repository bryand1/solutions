#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        vector<vector<int>> res;
        for (int i = 0; i < A.size(); i++) {
            vector<int> tmp;
            for (int j = A[i].size() - 1; j >= 0; j--) tmp.push_back(1 - A[i][j]);
            res.push_back(tmp);
        }
        return res;
    }
};
