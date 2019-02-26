#include <iostream>

using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        int l = 0;
        int r = x;
        int m;
        while (l <= r) {
            m = l + (r - l) / 2;
            if ((m * m <= x) && (x < ((m + 1) * (m + 1)))) {
                cout << m << endl;
                return m;
            } else if (x < (m * m)) {
                cout << m << endl;
                r = m;
            } else {
                cout << m << endl;
                l = m + 1;
            }
        }
        return m;
    }
};

int main(void) {
    Solution s;
    s.mySqrt(8);
    return 0;
}
