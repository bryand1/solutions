class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0, maxprofit = 0;
        for (unsigned int i = 1; i < prices.size(); i++) {
            profit = prices[i] - prices[i - 1];
            if (profit > 0) maxprofit += profit;
        }
        return maxprofit;
    }
};
