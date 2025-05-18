/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/



class Solution {
public:

    Node* dfs(Node* &root, unordered_map<Node*, Node*> &alreadyCloned) {

        // already cloned
        if (alreadyCloned[root]) {
            return alreadyCloned[root];
        }

        // neig are empty then just retrn node with val
        if (root->neighbors.empty()) return new Node(root->val);

        // valid
        // clone the curr node's val
        Node* clone = new Node(root->val);
        // mark cloned
        alreadyCloned[root] = clone;

        // clone neig of root
        for (auto neig : root->neighbors) {
            clone->neighbors.push_back(dfs(neig, alreadyCloned));
        }

        return clone;
    }

    Node* cloneGraph(Node* node) {
        
        // empty
        if (!node) return nullptr;

        unordered_map<Node*, Node*> alreadyCloned;

        return dfs(node, alreadyCloned);

    }
};