#include <string>
#include <vector>
#include <set>
#include <iostream>
#include <map>
using namespace std;

class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        set<string> mores;
        map<char, string> transfrom{{'a',".-"},{'b',"-..."},{'c',"-.-."},{'d',"-.."},
                                    {'e',"."},{'f',"..-."},{'g',"--."},{'h',"...."},
                                    {'i',".."},{'j',".---"},{'k',"-.-"},{'l',".-.."},
                                    {'m',"--"},{'n',"-."},{'o',"---"},{'p',".--."},
                                    {'q',"--.-"},{'r',".-."},{'s',"..."},{'t',"-"},
                                    {'u',"..-"},{'v',"...-"},{'w',".--"},{'x',"-..-"},
                                    {'y',"-.--"},{'z',"--.."}};
        string temp_code;
        for(const auto &word: words) {
            temp_code.clear();
            for(const auto &c: word) {
                temp_code.append(transfrom.at(c));
            }
            mores.insert(temp_code);
        }
        return mores.size();
    }
};