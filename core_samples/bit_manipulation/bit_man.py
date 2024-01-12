class BitManipulation:
    def __init__(self) -> None:
        pass

    @staticmethod
    def bitwise_and(lhs: int, rhs: int) -> int:
        return lhs & rhs

    @staticmethod
    def bitwise_or(lhs: int, rhs: int) -> int:
        return lhs | rhs

    @staticmethod
    def bitwise_xor(lhs: int, rhs: int) -> int:
        return lhs ^ rhs

    @staticmethod
    def bitwise_not(operand: int) -> int:
        return ~operand

    @staticmethod
    def bitwise_shift_left(operand: int, count: int) -> int:
        return operand << count

    @staticmethod
    def bitwise_shift_right(operand: int, count: int) -> int:
        return operand >> count

if __name__ == "__main__":
    pass