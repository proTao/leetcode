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
    char findTheDifference(string s, string t) {
        vector<int> table(26,0);
        for(const char &c: s){
            table[c-'a'] += 1;
        }
        
        for(const char &c: t){
            if(table[c-'a'] == 0){
                return c;
            }
            else{
                table[c-'a'] -= 1;
            }
        }

    }
};

int main(){
    Solution s;
    cout<<s.findTheDifference("abbc","abbdc")<<endl;
}
