class Pointer:
    def __init__(self, x=0, y=-1):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Pointer(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Pointer(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return ((self.x << 32) | self.y).__hash__()
    
    def rotate(self):
        self.x, self.y = -self.y, self.x
    
    def __str__(self) -> str:
        match (self.x, self.y):
            case (1,0):
                return 'right'
            case (0,-1):
                return 'up'
            case (-1,0):
                return 'left'
            case (0,1):
                return 'down'
            case (0,0):
                return 'zero'