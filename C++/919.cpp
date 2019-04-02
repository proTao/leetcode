#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#include <memory>
#include <sstream>
#include <cmath>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}

vector<int> level_traversal(TreeNode *t){
    queue<TreeNode*> q1, q2;
    q1.push(t);
    queue<TreeNode*> *currentLevel = &q1;
    queue<TreeNode*> *nextLevel = &q2;
    TreeNode *node = nullptr;
    vector<int> res;

    while(not currentLevel->empty()){
        while(not currentLevel->empty()){
            node = currentLevel->front();
            res.push_back(node->val);
            cout<<node->val<<endl;
            if(node->left != nullptr) nextLevel->push(node->left);
            if(node->right != nullptr) nextLevel->push(node->right);
            currentLevel->pop();
        }
        swap(currentLevel, nextLevel);
    }
    return res;
}

TreeNode* stringToTreeNode(string input) {
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    if (!input.size()) {
        return nullptr;
    }

    string item;
    stringstream ss;
    ss.str(input);

    getline(ss, item, ',');
    TreeNode* root = new TreeNode(stoi(item));
    queue<TreeNode*> nodeQueue;
    nodeQueue.push(root);

    while (true) {
        TreeNode* node = nodeQueue.front();
        nodeQueue.pop();

        if (!getline(ss, item, ',')) {
            break;
        }

        trimLeftTrailingSpaces(item);
        if (item != "null") {
            int leftNumber = stoi(item);
            node->left = new TreeNode(leftNumber);
            nodeQueue.push(node->left);
        }

        if (!getline(ss, item, ',')) {
            break;
        }

        trimLeftTrailingSpaces(item);
        if (item != "null") {
            int rightNumber = stoi(item);
            node->right = new TreeNode(rightNumber);
            nodeQueue.push(node->right);
        }
    }
    return root;
}

class CBTInserter {
private:
    vector<int> data;
    TreeNode *root;

public:
    CBTInserter(TreeNode* _root) {
        data = level_traversal(_root);
        root = _root;
    }
    
    int insert(int v) {
        data.push_back(v);
        vector<int>::size_type index = data.size();
        unsigned insertPath = data.size();
        unsigned pathLength = log2(insertPath);
        TreeNode *node = root;

        while (pathLength > 1){
            if(((insertPath>>(pathLength-1)) bitand 1) == 0){
                cout<<"left"<<endl;
                node = node->left;
            }
            else {
                cout<<"right"<<endl;
                node = node->right;
            }
            --pathLength;
        }
        // shared_ptr<TreeNode> newnode = make_shared<TreeNode>(v);
        if(insertPath bitand 1 == 1){
            node->right = new TreeNode(v);
        }
        else{
            node->left = new TreeNode(v);
        }
        return data.at(data.size()/2-1);
    }
    
    TreeNode* get_root() {
        return root;
    }
};

void prettyPrintTree(TreeNode* node, string prefix = "", bool isLeft = true) {
    if (node == nullptr) {
        cout << "Empty tree";
        return;
    }

    if(node->right) {
        prettyPrintTree(node->right, prefix + (isLeft ? "│   " : "    "), false);
    }

    cout << prefix + (isLeft ? "└── " : "┌── ") + to_string(node->val) + "\n";

    if (node->left) {
        prettyPrintTree(node->left, prefix + (isLeft ? "    " : "│   "), true);
    }
}

int main(){
    TreeNode *tree = stringToTreeNode("[1]");
    CBTInserter cbt(tree);
    cout<<cbt.insert(2)<<endl;
    tree = cbt.get_root();
    prettyPrintTree(tree);
    return 0;
}