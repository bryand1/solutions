class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for(int i = 0; i < nums.size(); i++) {
            if(m.find(target - nums[i]) != m.end()){
                vector<int> v;
                v.push_back(m[target - nums[i]]);
                v.push_back(i);
                return v;
            }
            m[nums[i]] = i;
        }
    }
};
