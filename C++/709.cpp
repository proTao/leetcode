#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string toLowerCase(string str) {
        for(auto &c:str){
            c = tolower(c);
        }
        return str;
    }
};

int main(){
    Solution s;
    cout<<s.toLowerCase("ASDasd")<<endl;
}