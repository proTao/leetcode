#include <iostream>
#include <string>
#include <vector>

using namespace std;

static const auto io_sync_off = []()
{
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    std::cin.tie(nullptr);
    return nullptr;
}();
class Solution {
public:
    int getSum(int a, int b) {
        // the leetcode playground is 32-bit env
        auto max_bits = 32;  
        auto carry = 0;
        auto _sum = 0;           
        for (auto i = 0; i < max_bits; i++) {
            auto a_bit = (a >> i) & 1;
            auto b_bit = (b >> i) & 1;
            auto tmp = (a_bit ^ b_bit ^ carry) << i;
            _sum |= tmp;
            carry = (a_bit & b_bit) || (a_bit & carry) || (b_bit & carry) ? 1 : 0;
        }
        return _sum;     
    }
};

int main() {
    int ret = Solution().getSum(1,2);
    cout<<ret<<endl;
    return 0;
}
