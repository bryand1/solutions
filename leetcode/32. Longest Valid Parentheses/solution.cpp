#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> st;
        st.push_back(-1);
        int r = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s.at(i) == '(') {
                st.push_back(i);
            } else {
                st.pop_back();
                if (st.size()) {
                    r = max(r, i - st.back());
                } else {
                    st.push_back(i);
                }
            }
        }  
        return r;
    }
};
