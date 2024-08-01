class Solution:
    def countSeniors(self, details: list[str]) -> int:
        return sum([1 for passenger in details if int(passenger[-4:-2]) > 60])
