#include <iostream>

using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        long l = 0, r = (long)x, t = (long)x, m;
        while (l <= r) {
            m = l + (r - l) / 2;
            if ((m * m <= t) && (t < ((m + 1) * (m + 1)))) {
                return (int) m;
            } else if (t < (m * m)) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return (int) m;
    }
};

int main(void) {
    Solution s;
    s.mySqrt(8);
    return 0;
}
