from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.flag = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_node(self, word):
        node = self.root
        for char in word:
            # node.children[char] = TrieNode
            node = node.children[char]
        node.flag = word


trie = Trie()
# a = Trie.add_node(trie, 'word')
# print(a)
trie.add_node('word')
print(trie)


def solution(words):
    trie = Trie()
    for word in words:
        trie.add_node(word)
        print(trie.root.flag)
    curr = trie.root
    while True:
        print(curr.children)
        curr = curr.children
        if curr == None:
            break
    answer = 0
    return answer

solution(["go","gone","guild"])