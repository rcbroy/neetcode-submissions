import "cmp"
import "slices"

func carFleet(target int, position []int, speed []int) int {
	pos_speed := make(map[int]int, len(position))
	for i, p := range position {
		pos_speed[p] = speed[i]
	}
	slices.SortFunc(position, func(a, b int) int {
		return cmp.Compare(b, a)
	})
	fleets := 0
	var fleetTime float64
	for _, p := range position {
		thisCar := float64(target-p) / float64(pos_speed[p])
		if thisCar > fleetTime {
			fleets++
			fleetTime = thisCar
		}
	}
	return fleets
}
