#include <iostream>
#include <string>

using namespace std;

int symbol2value(char c){
    switch(c){
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
    }
}

string get_next_symble(int& n){
    if(n >= 1000) {
        n -= 1000;
        return "M";
    }
    else if(n >= 900) {
        n -= 900;
        return "CM";
    }
    else if(n >= 500) {
        n -= 500;
        return "D";
    }
    else if(n >= 400) {
        n -= 400;
        return "CD";
    }
    else if(n >= 100) {
        n -= 100;
        return "C";
    }
    else if(n >= 90) {
        n -= 90;
        return "XC";
    }
    else if(n >= 50) {
        n -= 50;
        return "L";
    }
    else if(n >= 40) {
        n -= 40;
        return "XL";
    }
    else if(n >= 10) {
        n -= 10;
        return "X";
    }
    else if(n >= 9) {
        n -= 9;
        return "IX";
    }
    else if(n >= 5) {
        n -= 5;
        return "V";
    }
    else if(n >= 4) {
        n -= 4;
        return "IV";
    }
    else{
        n -= 1;
        return "I";
    }
}

class Solution {
public:
    string intToRoman(int num) {
        string res;
        while(num){
            res += get_next_symble(num);
        }
        return res;
    }
};


int main(){
    Solution s;
    cout<<s.intToRoman(58)<<endl;
    cout<<s.intToRoman(1994)<<endl;
    return 0;
}