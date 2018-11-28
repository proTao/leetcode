#include <iostream>
using namespace std;

class Solution {
public:
    bool hasAlternatingBits(int n) {
        bool flag = n bitand 1;
        n >>= 1;
        while(n){
            if(flag xor (n bitand 1)){
                flag = n bitand 1;
                n >>= 1;
                continue;
            }
            return false;
        }
        return true;
    }
};

int main(){
    Solution s;
    cout<<s.hasAlternatingBits(5)<<endl;
    cout<<s.hasAlternatingBits(7)<<endl;
    cout<<s.hasAlternatingBits(11)<<endl;
    cout<<s.hasAlternatingBits(10)<<endl;
    return 0;
}
