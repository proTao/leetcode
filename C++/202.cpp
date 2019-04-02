#include <iostream>
#include <unordered_set>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    unordered_set<int> happy{1};
    unordered_set<int> unhappy{2,3,4,5,6,7,8,9};
    bool isHappy(int n) {
        unordered_set<int> seq;
        int cnt{0};
        while(true){
            ;
            if(happy.find(n) != happy.end()){
                cout<<"hit"<<cnt<<endl;
                happy.insert(seq.begin(), seq.end());
                return true;
            }
            if(unhappy.find(n) != unhappy.end() or seq.find(n) != seq.end()){
                cout<<"hit"<<cnt<<endl;
                unhappy.insert(seq.begin(), seq.end());
                return false;
            }
            seq.insert(n);
            n = f(n);
            ++cnt;
        }
    }

    int f(int n){
        int res{0};
        while (n>=10){
            res += pow(n%10, 2);
            n /= 10;
        }
        res += pow(n, 2);
        return res;
    }
};

int main(){
    Solution s;
    cout<<s.isHappy(19)<<endl;
    cout<<s.isHappy(89)<<endl;
    cout<<s.isHappy(145)<<endl;
    return 0;
}