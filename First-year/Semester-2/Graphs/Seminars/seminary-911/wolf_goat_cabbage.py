class WolfGoatCabbageGraph:
    def parse_out(self, x):
        return x.parse_neighbors()

    def parse_in(self, y):
        return y.parse_neighbors()

    def initial_state(self):
        return WolfGoatCabbageState(0)

    def final_state(self):
        return WolfGoatCabbageState(0xF)

class WolfGoatCabbageState:
    def __init__(self, bitmask):
        # bit 0 (LSB) = wolf, 1=goat, 2=cabbage, 3=boat; value 0=left, 1=right
        self.__bitmask = bitmask

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        left = ""
        right = ""
        for i in range(4):
            what = "WGCB"[i]
            if ((self.__bitmask >> i) & 1) == 0:
                left += what
            else:
                right += what
        return f"{left}-{right}"

    def __eq__(self, other):
        if not isinstance(other, WolfGoatCabbageState):
            return False
        return self.__bitmask == other.__bitmask

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return self.__bitmask
        
    def parse_neighbors(self):
        for i in range(4):
            v = self.__bitmask
            if ((v>>3) & 1) == ((v>>i) & 1): # item i and boat are on the same side
                v ^= 8
                if i != 3:
                    v ^= (1 << i)
                next = WolfGoatCabbageState(v)
                if next.is_valid():
                    yield next

    def is_valid(self):
        v = self.__bitmask
        if ((v>>3) & 1) == ((v>>1) & 1): # goat and goat are on the same side
            return True
        if ((v>>0) & 1) == ((v>>1) & 1): # wolf and goat are on the same side
            return False
        if ((v>>2) & 1) == ((v>>1) & 1): # cabbage and goat are on the same side
            return False
        return True
