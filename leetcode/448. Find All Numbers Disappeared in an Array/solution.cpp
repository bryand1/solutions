class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> res;
        int i;
        for (i = 0; i < nums.size(); i++) {
            int ix = abs(nums[i]) - 1;
            nums[ix] = abs(nums[ix]) * -1;
        }
        for (i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) {
                res.push_back(i + 1);
            }
        }
        return res;
    }
};