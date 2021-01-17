#include <unordered_map>
#include <list>

using namespace std;


struct DoubleLinkedListNode{     // struct才是默认public，怎么全都忘了我淦
    int key;
    int value;
    DoubleLinkedListNode* pre;
    DoubleLinkedListNode* next;
    DoubleLinkedListNode(): key(0), value(0), pre(nullptr), next(nullptr){}
    DoubleLinkedListNode(int key, int value): key(key),value(value), pre(nullptr), next(nullptr){}
};


class LRUCache {            // 哈希表加双向链表
private:
    int sum_capacity;
    int cur_size;
    unordered_map<int, DoubleLinkedListNode*> hash_map;
    // 使用伪头部和伪尾部节点方便操作
    DoubleLinkedListNode* head;     // 这样在双向链表的头部添加节点的复杂度就为O(1)了
    DoubleLinkedListNode* tail;     // 这样在双向链表的尾部删除节点的复杂度也为O(1)了
public:
    LRUCache(int capacity) {
        sum_capacity = capacity;
        cur_size = 0;
        head = new DoubleLinkedListNode();
        tail = new DoubleLinkedListNode();
        head->next = tail;      // 别忘了这里
        tail->pre = head;
    }

    int get(int key) {
        auto iterator = hash_map.find(key);     // 注意unordered_map里不是get是find
        if(iterator == hash_map.end())
            return -1;
        else{
            moveToHead(iterator->second);       // 把这个移到头部表明它被使用过了
            return iterator->second->value;
        }
    }

    void put(int key, int value) {
        auto iterator = hash_map.find(key);
        if(iterator == hash_map.end()){       // key不存在
            DoubleLinkedListNode* new_node = new DoubleLinkedListNode(key, value);
            hash_map[key] = new_node;
            // hash_map.insert(pair<int, DoubleLinkedListNode*>(key, new_node)); 这样太麻烦了，用上面那种
            addToHead(new_node);
            cur_size++;
            if(cur_size > sum_capacity){
                DoubleLinkedListNode* removed_node = removeTail();
                hash_map.erase(removed_node->key);      // 记得这里也要删
                cur_size--;
            }
        }
        else{
            DoubleLinkedListNode* node = iterator->second;
            node->value = value;
            moveToHead(node);
        }
    }

    // ********************辅助用的********************

    void moveToHead(DoubleLinkedListNode* node) {
        removeNode(node);
        addToHead(node);
    }

    DoubleLinkedListNode* removeTail() {
        DoubleLinkedListNode* node = tail->pre;
        removeNode(node);
        return node;
    }

    void removeNode(DoubleLinkedListNode* node) {           // 这样就实现了O(1)
        node->pre->next = node->next;
        node->next->pre = node->pre;
    }

    void addToHead(DoubleLinkedListNode* node) {            // 这样就实现了O(1)
        node->pre = head;
        node->next = head->next;
        head->next->pre = node;
        head->next = node;
    }
};

