#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;


bool isVowel(char c){
    return (c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U');
}



class Solution {
public:
    string toGoatLatin(string S) {
        istringstream sin(S);
        ostringstream sout;
        int cnt{2};
        string word;
        while(sin>>word){
            if(isVowel(word.at(0))){
                sout<<word;
            }
            else {
                sout<<word.substr(1);
                sout<<word.at(0);
            }
            sout<<"m"<<string(cnt++,'a')<<" ";

        }
        return sout.str();
    }

};

int main(){
    Solution s;
    cout<<s.toGoatLatin("The quick brown fox jumped over the lazy dog")<<endl;
    return 0;
}