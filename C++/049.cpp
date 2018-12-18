#include <iostream>
#include <vector>
#include <string>
#include <map>
//#include <array>
using namespace std;


class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, unsigned> hash2index;
        vector<int> hash; // use to conut 
        vector<vector<string>> res;
        vector<string> temp;
        map<vector<int>, unsigned>::const_iterator it;

        for(const auto &s : strs){
            hash.assign(26, 0);
            for(const auto &c : s){
                hash.at(c-'a') += 1;
            }
            if((it = hash2index.find(hash)) == hash2index.end()){
                hash2index.insert(make_pair(hash, hash2index.size()));
                temp = {s};
                res.push_back(temp);
            }
            else {
                res.at(it->second).push_back(s);
            }
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<string> strs{"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> res = s.groupAnagrams(strs);
    for(auto v:res){
        for(auto s: v){
            cout<<s<<" ";
        }
        cout<<endl;
    }
    return 0;
}