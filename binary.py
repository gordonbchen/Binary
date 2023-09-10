"""Exploring how ints are represented in binary."""


def binary_to_decimal(binary: str) -> int:
    """Convert binary str to decimal int."""
    decimal = 0
    for i, bit in enumerate(binary):
        if int(bit) == 1:
            bit_place = len(binary) - i - 1
            val = 2 ** bit_place

            if i == 0:
                val *= -1

            decimal += val

    return decimal


def decimal_to_binary(decimal: int, bits: int = 8) -> str:
    """Convert decimal int into binary str."""
    binary = ""
    for i in range(bits):
        val = 2 ** (bits - i - 1)

        if i == 0 and decimal < 0:
            binary += "1"
            val *= -1
            decimal -= val
        elif val <= decimal:
            binary += "1"
            decimal -= val
        else:
            binary += "0"

    return binary


print(binary_to_decimal("1010"))
print(decimal_to_binary(-6, bits=4))
