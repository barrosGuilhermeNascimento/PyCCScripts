class GPSError(Exception):
    def __init__(self, message="Something went terribly wrong."):
        super().__init__(message)

class Direction():
    _internalDirection: str = ''
    __internalOrder = ['+z', '-x', '-z', '+x']

    def __init__(self, direction: str) -> None:
        if (direction not in ['+z', '-x', '-z', '+x']):
            raise ValueError(f'{direction} is not a valid Direction.')
        self._internalDirection = direction 
    
    def __add__(self, other) -> 'Direction':
        newOrder = self.__internalOrder[self.__internalOrder.index(self._internalDirection):] + self.__internalOrder[:self.__internalOrder.index(self._internalDirection)]
        return Direction(newOrder[other % len(self.__internalOrder)])

    def __radd__(self, other) -> 'Direction':
        return self.__add__(other)

    def __sub__(self, other) -> 'Direction':
        newOrder = self.__internalOrder[self.__internalOrder.index(self._internalDirection):] + self.__internalOrder[:self.__internalOrder.index(self._internalDirection)]
        return Direction(newOrder[(other % len(self.__internalOrder)) - len(self.__internalOrder)])

    def __rsub__(self, other) -> 'Direction':
        return self.__sub__(other)

    def __eq__(self, other):
        if isinstance(other, Direction):
            return self._internalDirection == other._internalDirection
        return False

    def __str__(self) -> str:
        return self._internalDirection

    def __repr__(self) -> str:
        return str(self)

    def axis(self) -> str:
        return self._internalDirection[1]

    def sign(self) -> str:
        return self._internalDirection[0]