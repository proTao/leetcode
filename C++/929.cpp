#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        set<string> occurs;
        string::size_type pos{0};
        string::size_type pos_of_at{0};
        for(auto &s: emails){
            //delete str between "+" and "@"
            pos_of_at = s.find("@");
            pos = s.find("+");
            if(pos < pos_of_at){
                s.erase(s.begin() + pos, s.begin() + pos_of_at);
            }
            
            // delete "."
            pos = s.find(".", 0);
            pos_of_at = s.find("@");
            while(pos < pos_of_at){
                s.erase(s.begin() + pos);
                pos = s.find(".", pos);
            }
            
            if (occurs.count(s) == 0){
                cout<<s<<endl;
                occurs.insert(s);
            }
        }
        return occurs.size();
    }
};


int main() {
    vector<string> emails{"r.cyo.g+z+dr.k.u@tgsg.z.com","fg.r.u.uzj+o.pw@kziczvh.com",
        "r.cyo.g+d.h+b.ja@tgsg.z.com",
        "fg.r.u.uzj+o.f.d@kziczvh.com",
        "r.cyo.g+ng.r.iq@tgsg.z.com",
        "fg.r.u.uzj+lp.k@kziczvh.com",
        "r.cyo.g+n.h.e+n.g@tgsg.z.com",
        "fg.r.u.uzj+k+p.j@kziczvh.com",
        "fg.r.u.uzj+w.y+b@kziczvh.com",
        "r.cyo.g+x+d.c+f.t@tgsg.z.com",
        "r.cyo.g+x+t.y.l.i@tgsg.z.com",
        "r.cyo.g+brxxi@tgsg.z.com",
        "r.cyo.g+d+l.c.n+g@tgsg.z.com",
        "fg.r.u.uzj+vq.o@kziczvh.com",
        "fg.r.u.uzj+uzq@kziczvh.com",
        "fg.r.u.uzj+mvz@kziczvh.com",
        "fg.r.u.uzj+taj@kziczvh.com",
        "fg.r.u.uzj+fek@kziczvh.com"};
    Solution s;
    cout<<s.numUniqueEmails(emails)<<endl;
    return 0;
}
