#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <deque>

using namespace std;


class Solution {
private:
    deque<string> path;
    void addPath(const string&);
public:
    string simplifyPath(string p) {
        string res;
        string::size_type slow = p.find("/");
        if(slow == string::npos or slow == p.size()-1){
            return p;
        }
        string::size_type fast = p.find("/", slow+1);
        while(slow != string::npos and slow != p.size()-1){
            addPath(p.substr(slow+1, fast-slow-1));
            slow = fast;
            if(slow < p.size()-1){
                fast = p.find("/", slow+1);
            }
        }

        for(auto s: path){
            res += "/";
            res += s;
        }
        if(res.empty()){
            return "/";
        }
        return res;

    }
};

void Solution::addPath(const string &p){
    if(p == "." or p.size() == 0){
        return;
    }
    if(path.size()){
        if(path.back() == ".." and p != ".."){
            path.pop_back();
            return;
        }
        if(path.back() != ".." and p == ".."){
            path.pop_back();
            return;
        }
    }
    else{
        if(p == ".."){
            return;
        }
    }
    path.push_back(p);
}

int main(){
    Solution s;
    cout<<s.simplifyPath("/..")<<endl;
    return 0;

}