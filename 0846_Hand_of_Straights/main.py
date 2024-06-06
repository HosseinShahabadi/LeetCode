# Editorial solution: O(n) ----------------------------------------------------
from typing import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        def isConsecutive(group: list[int]):
            for i in range(1, groupSize):
                if group[i] - 1 != group[i-1]:
                    return False
            return True

        if len(hand) % groupSize:
            return False

        # Counter to store the count of each card value
        card_count = Counter(hand)

        for card in hand:
            start_card = card
            # Find the start of the potential straight sequence
            while card_count[start_card - 1]:
                start_card -= 1

            # Process the sequence starting from start_card
            while start_card <= card:
                while card_count[start_card]:
                    # Check if we can form a consecutive sequence
                    # of groupSize cards
                    for next_card in range(start_card, start_card + groupSize):
                        if not card_count[next_card]:
                            return False
                        card_count[next_card] -= 1
                start_card += 1

        return True


# My own solution: O(nlogn) ---------------------------------------------------
# class Solution:
#     def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
#         def isConsecutive(group: list[int]):
#             for i in range(1, groupSize):
#                 if group[i] - 1 != group[i-1]:
#                     return False
#             return True

#         n = len(hand)
#         if n % groupSize:
#             return False
        
#         hand.sort()
#         loop_size = int(n / groupSize)
#         group = []
#         for i in range(loop_size):
#             group.append([])

#         base = 0
#         pointer = 0
#         for i in range(n):
#             num = hand[i]
#             while len(group[pointer]) >= groupSize or num in group[pointer]:
#                 pointer += 1
#                 if pointer >= loop_size:
#                     return False
            
#             group[pointer].append(num)
#             pointer = base
#             if len(group[base]) >= groupSize:
#                 base += 1

#         for i in range(loop_size):
#             if not isConsecutive(group[i]):
#                 return False
        
#         return True
