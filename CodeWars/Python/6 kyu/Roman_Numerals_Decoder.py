def solution(roman: str) -> int:
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_value = 0
    for ch in reversed(roman):
        value = roman_dict[ch]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total
