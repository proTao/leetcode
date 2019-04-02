
auto digitroot = [](int a) -> {return 1 + (a-1) % 9;};

class Solution {
public:
    int addDigits(int num) {
        return 1 + (num-1) % 9;
    }
};