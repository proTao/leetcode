#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        if(matrix.size() == 0 or matrix.at(0).size() == 0){
            return res;
        }

        int left_bound{0}, right_bound{matrix.at(0).size()-1};
        int up_bound{0}, down_bound{matrix.size()-1};
        int r{0};
        int c{0};

        while(true){
            // move right
            while(c < right_bound){
                res.push_back(matrix.at(r).at(c));
                ++c;
            }
            res.push_back(matrix.at(r).at(c));
            ++r;
            ++up_bound;
            if(left_bound > right_bound or up_bound > down_bound)
                break;

            // move down
            while(r < down_bound){
                res.push_back(matrix.at(r).at(c));
                ++r;
            }
            res.push_back(matrix.at(r).at(c));
            --c;
            --right_bound;
            if(left_bound > right_bound or up_bound > down_bound)
                break;

            // move left
            while(c > left_bound){
                res.push_back(matrix.at(r).at(c));
                --c;
            }
            res.push_back(matrix.at(r).at(c));
            --r;
            --down_bound;
            if(left_bound > right_bound or up_bound > down_bound)
                break;

            // move up
            while(r > up_bound){
                res.push_back(matrix.at(r).at(c));
                --r;
            }
            res.push_back(matrix.at(r).at(c));
            ++c;
            ++left_bound;
            if(left_bound > right_bound or up_bound > down_bound)
                break;
        }
        return res;
    }
};

int main() {
    vector<vector<int>> matrix{{1,2,3,4},{5,6,7,8},{9,10,11,12}};
    Solution s;
    vector<int> res = s.spiralOrder(matrix);
    for(const auto &i:res){
        cout<<i<<" ";
    }
    cout<<endl;
    return 0;
}