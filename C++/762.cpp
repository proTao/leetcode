#include <iostream>
#include <unordered_set>

using namespace std;
const static unordered_set<int> PRIME{2,3,5,7,11,13,17,19,23,29,31};

int getBits(int n){
    int bits{0};
    while(n){
        if((n bitand 1)==1){
            bits += 1;
        }
        n >>= 1;
    }
    return bits;
}

class Solution {
public:
    int countPrimeSetBits(int L, int R) {
        int cnt{0};
        for(int i=L; i<=R; ++i){
            if(PRIME.find(getBits(i)) != PRIME.end()){
                ++cnt;
            }
        }
        return cnt;
    }
};

int main(){
    Solution s;
    cout<<s.countPrimeSetBits(6,10)<<endl;
    // cout<<getBits(5)<<endl;
    return 0;
}