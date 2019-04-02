#include <sstream>
#include <iostream>

using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        istringstream sin(s);
        string word;        
        while(sin>>word);
        return word.size();
    }
};

int main() {
    Solution s;
    cout<<s.lengthOfLastWord("a sdf qweqa asd")<<endl;
    return 0;
}