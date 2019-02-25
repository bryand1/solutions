class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int x, y, i;
        int b = 0;
        for (i = 0; i < nums.size(); i++) {
            x = nums[i];
            if (s.find(x - 1) == s.end()) {
                y = x + 1;
                while (s.find(y) != s.end()) y++;
                b = max(b, y - x);
            }   
        }
        return b;
    }
};