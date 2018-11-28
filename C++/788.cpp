#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;

static const auto io_sync_off = []()
{
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    std::cin.tie(nullptr);
    return nullptr;
}();

const static set<int> GOODNUM{0,1,2,5,6,8,9};
const static set<int> CHANGE{2,5,6,9};

class Solution {
public:
    int rotatedDigits(int N) {
        int temp,copy_i,cnt{0};
        bool valid, change;

        for(int i=1; i<=N; ++i){
            copy_i = i;
            valid = true;
            change = false;
            do{
                if(GOODNUM.count(copy_i % 10) == 0){
                    valid = false;
                    break;                    
                } else {
                    if(CHANGE.count(copy_i % 10) > 0){
                        change = true;
                    }
                }
                copy_i = copy_i / 10;
            } while (copy_i);
            if(valid && change) ++cnt;
        }
        return cnt;
    }
};

int main(){
    Solution s;
    cout<<s.rotatedDigits(10)<<endl;
}
