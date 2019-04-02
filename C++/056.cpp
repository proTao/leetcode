#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};


class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        if(intervals.size() <= 1){
            return intervals;
        }
        sort(intervals.begin(), intervals.end(), 
            [](const Interval &a, const Interval &b) {
                return a.start < b.start;
            });

        vector<Interval> res;
        res.push_back(intervals.at(0));

        vector<Interval>::iterator it = intervals.begin()+1;
        while (it != intervals.end()){
            // if (it->start < (res.back.end) and it->end > (res.back.end))
            //     (res.back.end) = it->end;
            if (it->start <= res.back().end){
                if(it->end >= res.back().end)
                    res.back().end = it->end;
            }
            else
                res.push_back(*it);
            ++it;
        }
        for(const auto &i: res)
            cout<<i.start<<" "<<i.end<<endl;

        return res;
    }
};

int main(){
    Solution s;
    vector<Interval> intervals{{1,4},{4,5}};
    s.merge(intervals);
    return 0;
}