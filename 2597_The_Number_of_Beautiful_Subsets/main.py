# Initially, I had my own solution, but Hi-Malik's explanation and C++ solution
# were much better. With the assistance of ChatGPT, I used his approach to develop
# this optimized Python version.

from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums, k):
        mp = defaultdict(list)
        for el in nums:
            mp[el % k].append(el)
        
        ans = 1
        for mod_cal, v in mp.items():
            v.sort()
            mp2 = defaultdict(int)
            for el in v:
                mp2[el] += 1
            
            prev_el = float('-inf')
            prevNotTaken = 1
            prevTaken = 0
            nowNotTaken = 0
            nowTaken = 0
            
            for el, freq in sorted(mp2.items()):
                poss_subsets = int(2**freq - 1)
                if prev_el + k == el:
                    nowNotTaken = prevNotTaken + prevTaken
                    nowTaken = prevNotTaken * poss_subsets
                else:
                    nowNotTaken = prevNotTaken + prevTaken
                    nowTaken = (prevNotTaken + prevTaken) * poss_subsets
                
                prevNotTaken = nowNotTaken
                prevTaken = nowTaken
                prev_el = el
            
            ans *= (nowNotTaken + nowTaken)
        
        return ans - 1
