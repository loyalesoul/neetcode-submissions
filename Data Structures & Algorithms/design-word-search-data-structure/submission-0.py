class TrieNode:

  def __init__(self):
    self.children = {}
    self.is_end_of_word = False


class WordDictionary:

  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word: str) -> None:
    curr = self.root
    for char in word:
      if char not in curr.children:
        curr.children[char] = TrieNode()
      curr = curr.children[char]
    curr.is_end_of_word = True

  def search(self, word: str) -> bool:
    def dfs(node, i):
      curr = node
      for j in range(i, len(word)):
        char = word[j]

        if char == ".":
          # Check all possible child branches 🌿
          for child in curr.children.values():
            if dfs(child, j + 1):
              return True
          return False
        else:
          if char not in curr.children:
            return False
          curr = curr.children[char]

      return curr.is_end_of_word

    return dfs(self.root, 0)