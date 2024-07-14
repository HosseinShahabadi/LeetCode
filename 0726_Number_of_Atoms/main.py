# This answer is from the "LeetCode" editorial.
from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        index = 0

        while index < len(formula):
            if formula[index] == "(":
                stack.append(defaultdict(int))
                index += 1

            elif formula[index] == ")":
                curr_map = stack.pop()
                index += 1
                multiplier = ""
                while index < len(formula) and formula[index].isdigit():
                    multiplier += formula[index]
                    index += 1
                if multiplier:
                    multiplier = int(multiplier)
                    for atom in curr_map:
                        curr_map[atom] *= multiplier

                for atom in curr_map:
                    stack[-1][atom] += curr_map[atom]

            else:
                curr_atom = formula[index]
                index += 1
                while index < len(formula) and formula[index].islower():
                    curr_atom += formula[index]
                    index += 1

                curr_count = ""
                while index < len(formula) and formula[index].isdigit():
                    curr_count += formula[index]
                    index += 1

                if curr_count == "":
                    stack[-1][curr_atom] += 1
                else:
                    stack[-1][curr_atom] += int(curr_count)

        final_map = dict(sorted(stack[0].items()))

        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans
