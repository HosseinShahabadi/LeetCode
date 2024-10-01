class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        ans = {0: 0}
        for num in arr:
            x = num % k
            if x in ans:
                ans[x] += 1
            else:
                ans[x] = 1

        if ans[0] % 2:
            return False
        
        for i in range(1, int(k/2) + 1):
            if i in ans and k-i in ans:
                if ans[i] != ans[k-i]:
                    return False
            else:
                if i not in ans and k-i not in ans:
                    continue
                else:
                    return False
        
        return True
