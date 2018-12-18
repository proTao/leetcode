#include <iostream>

#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0){
            return false;
        } else if(x < 10) {
            return true;
        }
        string s = to_string(x);
        auto l = s.cbegin();
        auto r = s.cend();
        --r;
        bool flag = true;
        while( l<r ){
            if(*l++ != *r--){
                flag = false;
                break;
            }
        }
        return flag;
    }
};

int main(){
    Solution s;
    cout<<s.isPalindrome(12201)<<endl;
    return 0;
}


