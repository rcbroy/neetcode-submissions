func searchMatrix(matrix [][]int, target int) bool {
	sr, er := 0, len(matrix)-1
	sc, ec := 0, len(matrix[0])-1

	for sr <= er {
		mr := (sr+er) / 2
		if matrix[mr][sc] > target {
			er = mr-1
		} else if matrix[mr][ec] < target {
			sr = mr+1
		} else {
			for sc <= ec {
				mc := (sc + ec) / 2
				if matrix[mr][mc] > target {
					ec = mc - 1
				} else if matrix[mr][mc] < target {
					sc = mc + 1
				} else {
					return true
				}
			}
			break
		}
	}
	return false
}
