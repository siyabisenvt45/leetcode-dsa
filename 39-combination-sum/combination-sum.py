class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, target, comb):
            if target == 0:
                result.append(list(comb))
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    comb.append(candidates[i])
                    backtrack(i, target - candidates[i], comb)
                    comb.pop()

        backtrack(0, target, [])
        return result