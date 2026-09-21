class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        frow, lrow = 0, len(matrix)-1
        i, j = 0, len(matrix[0])-1
        while frow <= lrow:
            mid = (frow+lrow) // 2
            if target < matrix[mid][i]:
                lrow = mid-1
            elif target > matrix[mid][j]:
                frow = mid+1
            else:
                while i <= j:
                    m = (i+j) // 2
                    if target < matrix[mid][m]:
                        j = m-1
                    elif target > matrix[mid][m]:
                        i = m+1
                    else:
                        return True
                return False
        return False