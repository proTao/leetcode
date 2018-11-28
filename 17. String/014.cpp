#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
    public:
        string longestCommonPrefix(vector<string>& strs) {
            string::size_type cnt{0};
            bool start;
            char currentChr;
            bool stop{false};
            while (!stop) {
                for(auto s: strs) {
                    start = true;
                    if (cnt < s.size()) {
                        if (start) {
                            currentChr = s[cnt];
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
            cout<<cnt<<endl;
            return strs[0].substr(0, cnt);
        }
};




int main(){
    vector<string> strs{"ac","abc","aaa"};
    Solution s;

    cout<<s.longestCommonPrefix(strs);
    return 0;
}
