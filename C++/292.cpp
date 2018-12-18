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
    std::cout.tie(nullptr);
    return nullptr;
}();

class Solution {
public:
    bool canWinNim(int n) {
        if (n<=3){return true;}
        return !((n+2)%3==0);
    }
};

int main(){
    Solution s;
    cout<<s.canWinNim(1)<<endl;
    return 0;
}