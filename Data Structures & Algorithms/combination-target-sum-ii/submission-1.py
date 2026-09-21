class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        temp = []
        candidates.sort()
        def backtrack(t, i):
            if t == 0:
                ans.add(tuple(temp))
            elif i == len(candidates) or t < 0:
                return
            else:
                current = candidates[i]
                temp.append(current)
                backtrack(t-current, i+1)
                temp.pop()
                backtrack(t, i+1)
        backtrack(target, 0)
        return [list(a) for a in ans]