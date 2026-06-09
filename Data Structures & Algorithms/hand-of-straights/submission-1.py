from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False    # not possible at all no matter what

        freq = defaultdict(int)
        for i in range(len(hand)):
            freq[hand[i]] += 1
        
        hand.sort()
        for i in range(len(hand)):
            if hand[i]-1 not in freq or freq[hand[i]-1] == 0 and freq[hand[i]] > 0:   # then this is a good start 
                hand_value = hand[i]
                count = 0
                while count < groupSize and freq[hand_value] > 0:
                    freq[hand_value] -= 1
                    count += 1
                    hand_value += 1
                
                if count < groupSize:
                    return False # (did not complete the group)
        return True
                
        