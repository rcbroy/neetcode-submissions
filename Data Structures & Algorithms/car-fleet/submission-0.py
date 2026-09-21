class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target-p)/s for p, s in sorted(zip(position, speed), key=lambda x: x[0], reverse=True)]
        fleets = 0
        fleet_time = 0
        for t in times:
            if t > fleet_time:
                fleets += 1
                fleet_time = t
        return fleets