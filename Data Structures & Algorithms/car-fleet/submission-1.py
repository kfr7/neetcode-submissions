class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # need to sort the positins so they are descending order, and then
        # the speed array needs toshuffle according to it
        position_to_speed = dict()
        for i in range(len(speed)):
            position_to_speed[position[i]] = speed[i]
        position.sort(reverse=True)
        for i in range(len(position)):
            speed[i] = position_to_speed[position[i]]
        
        fleet = 0
        new_bottleneck = float('-inf')
        for i in range(len(position)):
            # how long will it take for the car to get there?
            seconds_to_reach_target = (target - position[i]) / speed[i]
            # if it takes less seconds to reach the target from a car positioned
            # farther back, then we know they will become a fleet
            # if something never reaches it, then this becomes a new bottleneck\
            if seconds_to_reach_target > new_bottleneck:
                fleet += 1
                new_bottleneck = seconds_to_reach_target
            else:
                continue

        return fleet


        