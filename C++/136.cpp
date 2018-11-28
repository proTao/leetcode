#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for(const auto &i: nums){
            res xor_eq i;
        }
        return res;
    }
};

int main(){
    vector<int> a{4,1,2,1,2};
    Solution s;
    cout<<s.singleNumber(a)<<endl;
    return 0;
}