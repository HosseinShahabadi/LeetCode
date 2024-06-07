class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        def findRoot(string: str) -> str:
            for root in dictionary:
                if root == string[:len(root)]:
                    return root
            return string

        dictionary.sort()
        sentence = sentence.split()
        s = len(sentence)
        for i in range(s):
            sentence[i] = findRoot(sentence[i])
        return ' '.join(sentence)
