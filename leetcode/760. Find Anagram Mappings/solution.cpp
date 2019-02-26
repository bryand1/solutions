class Solution {
public:
    vector<int> anagramMappings(vector<int>& A, vector<int>& B) {
        unordered_map<int, int> d;
        for (int i = 0; i < B.size(); i++) {
            d[B[i]] = i;
        }
        vector<int> res;
        for (int x : A) {
            res.push_back(d[x]);
        }
        return res;
    }
};