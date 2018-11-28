#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
    public:
        string longestCommonPrefix(vector<string>& strs) {
            if (strs.size() == 0 ) return "";

            string::size_type cnt{0};
            bool start;
            char currentChr;
            bool stop{false};
            while (!stop) {
                start = true;
                for(auto &s: strs) {
                    if (cnt < s.size()) {
                        if (start) {
                            currentChr = s[cnt];
                            start=false;
                        }
                        else {
                            if(s[cnt] != currentChr){
                                stop = true;
                                break;
                            }
                            
                        }
                    }
                    else {
                        stop = true;
                        break;
                        
                    }
                }
                ++cnt;
            }
            //cout<<cnt<<endl;
            return strs[0].substr(0, --cnt);
        }
};




int main(){
    vector<string> strs;
    Solution s;
    // for(auto c : strs[0]){
    //     cout<<">>>"<<int(c)<<endl;
    // }
    cout<<s.longestCommonPrefix(strs);
    return 0;
}
