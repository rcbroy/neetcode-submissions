class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        seen = set()
        for i, n in enumerate(nums):
            if n in seen:
                continue
            target = 0 - n
            tested = set()
            s = i + 1
            e = len(nums) - 1
            while s < e:
                maybe = nums[s] + nums[e]
                if target > maybe:
                    s += 1
                elif target < maybe:
                    e -= 1
                else:
                    if nums[s] not in tested:
                        ans.append([n, nums[s], nums[e]])
                        tested.add(nums[s])
                        seen.add(n)
                    s += 1
        return ans