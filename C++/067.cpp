#include <string>
#include <iostream>
#include <algorithm>


using namespace std;

/*
        1-11 1-10 1-01 1-00
val     
carry
*/

class Solution {
public:
    string addBinary(string a, string b) {
        unsigned carry = 0;
        string res;
        string::const_reverse_iterator it1{a.crbegin()};
        string::const_reverse_iterator it2{b.crbegin()};

        while(it1 != a.crend() and it2 != b.crend()){
            res.push_back(48 + (*it1 xor *it2 xor carry bitand 1));
            carry = (carry bitand (*it1 bitor *it2) bitand 1) bitor (*it1 bitand *it2 bitand 1);
            ++it1;
            ++it2;
        }

        while(it1 != a.crend()){
            res.push_back(48 + ((*it1 xor carry) bitand 1));
            carry = carry bitand *it1 bitand 1;
            ++it1;
        }
        while(it2 != b.crend()){
            res.push_back(48 + ((*it2 xor carry) bitand 1));
            carry = carry bitand *it2 bitand 1;
            ++it2;
        }

        if(carry == 1){
            res.push_back('1');
        }

        reverse(res.begin(), res.end());
        return res;
    }
};

int main() {
    Solution s;
    cout<<s.addBinary("1", "111")<<endl;
    return 0;
}
