#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    string reverseOnlyLetters(string S) {
        string::iterator l = S.begin();
        string::iterator r = S.end()-1;

        while(l < r){
            while(l < r and not isalpha(*l)){
                ++l;
            }
            while(l < r and not isalpha(*r)){
                --r;
            }
            swap(*l, *r);
            if (l++ >= r--){
                break;
            }

        }
        return S;
    }
};

int main(){
    Solution s;
    cout<<s.reverseOnlyLetters("ab")<<endl;
    return 0;
}