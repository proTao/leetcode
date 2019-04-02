#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        if(nums.size()<=1){
            return true;
        }
        if(nums.at(0) == 0){
            return false;
        }
        vector<bool> flag(nums.size(), false);
        *(flag.end()-1) = true;
        vector<bool>::iterator it{flag.end()-2};
        vector<bool>::iterator start{flag.begin()};
        vector<bool>::iterator max_step_it;
        vector<int>::iterator nums_it{nums.end()-2};
        while(it >= start){
            for(max_step_it = it+1;
                max_step_it-it<=*nums_it and max_step_it<flag.end();
                ++max_step_it){
                if(*max_step_it){
                    *it=true;
                    break;
                }
            }
            --it;
            --nums_it;
        }
        return flag.at(0);
    }
};

int main(){
    vector<int> nums{2,0,0};
    Solution s;
    cout<<s.canJump(nums)<<endl;
    return 0;
}