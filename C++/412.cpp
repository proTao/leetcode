#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> res(n, string(""));
        string temp;
        for(int i = 1; i!=n+1; ++i){
            temp.clear();
            if(i % 3 == 0){
                temp += "Fizz";
            }
            if(i % 5 == 0){
                temp += "Buzz";
            }
            if(temp.size() == 0){
                temp = to_string(i);
            }
            res.at(i-1) = temp;
        }
        return res;
    }
};

int main(){
    Solution s;
    vector<string> res = s.fizzBuzz(15);
    for(auto s:res){
        cout<<s<<endl;
    }
    return 0;
}