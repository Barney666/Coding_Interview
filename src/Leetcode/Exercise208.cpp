//
// Created by 苗轶轩 on 2020/10/23.
//

#include <iostream>
#include <string>

using namespace std;

class Trie {
private:
    bool isEnd;
    Trie* children[26];
public:
    Trie() {
        isEnd = false;
        memset(children, 0, sizeof(children));     // NULL
    }

    void insert(string word) {
        Trie* node = this;
        for(char c: word){
            int index = c - 'a';      // 重点
            if(node->children[index] == NULL)
                node->children[index] = new Trie();
            node = node->children[index];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        Trie* node = this;
        for(char c: word){
            node = node->children[c-'a'];      // 因为头节点没有值，所以可以这样，一个节点也不会错过。
            if(node == NULL)
                return false;
        }
        return node->isEnd;     // 因为可能下面还有，那就不是这个单词了。app与apple
    }

    bool startsWith(string prefix) {
        Trie* node = this;
        for(char c: prefix){
            node = node->children[c-'a'];
            if(node == NULL)
                return false;
        }
        return true;
    }
};

//int main(){
//    Trie* obj = new Trie();
//    string word = "apple";
//    obj->insert(word);
//    bool param_2 = obj->search(word);
//    cout << param_2 << endl;
//    bool param_3 = obj->startsWith("app");
//    cout << param_3 << endl;
//    return 0;
//}