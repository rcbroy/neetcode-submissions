class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        sr, er = 0, len(matrix)-1
        sc, ec = 0, len(matrix[0])-1
        while sr <= er:
            mr = (sr + er) // 2
            s, e = matrix[mr][sc], matrix[mr][ec]
            if target < s:
                er = mr-1
            elif target > e:
                sr = mr+1
            else:
                while sc <= ec:
                    mc = (sc + ec) // 2
                    maybe = matrix[mr][mc]
                    if target < maybe:
                        ec = mc-1
                    elif target > maybe:
                        sc = mc+1
                    else:
                        return True
                break
        return False

