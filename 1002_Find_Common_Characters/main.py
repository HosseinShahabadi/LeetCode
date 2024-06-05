import copy

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        ans = dict.fromkeys(words[0], 0)
        for letter in words[0]:
            ans[letter] += 1

        n = len(words)
        for i in range(1, n):
            temp_dict = dict.fromkeys(words[i], 0)
            for letter in words[i]:
                temp_dict[letter] += 1
            
            ans_copy = copy.deepcopy(ans)
            for k, v in ans_copy.items():
                if not k in temp_dict:
                    ans.pop(k)
                elif temp_dict[k] < v:
                    ans[k] = temp_dict[k]

        result = []
        for k, v in ans.items():
            i = v
            while i > 0:
                result.append(k)
                i -= 1
        return result
