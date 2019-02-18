#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool wordBreak(const string& s, const vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.cbegin(), wordDict.cend());
        unordered_map<string, bool> memo;
        return wordBreak(s, wordSet, memo);
    }

    bool wordBreak(const string& s, const unordered_set<string> wordSet, unordered_map<string, bool> memo) {
        auto it = memo.find(s);
        if (it != memo.end())
            return it->second;
        if (wordSet.find(s) != wordSet.end())
            return memo[s] = true;
        for (int pos = 1; pos < s.size(); pos++) {
            const string right = s.substr(pos);
            if (wordSet.find(right) == wordSet.end())
                continue;
            const string left = s.substr(0, pos);
            if (wordBreak(left, wordSet, memo))
                return memo[s] = true;
        }
        return memo[s] = false;
    }
};
