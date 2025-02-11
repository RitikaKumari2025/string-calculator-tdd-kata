class StringCalculator:
    def __init__(self):
        self.default_delimiter = ","

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = self.default_delimiter
        if numbers.startswith("//"):
            delimiter, numbers = numbers[2:].split("\n", 1)

        nums = list(map(int, numbers.replace("\n", delimiter).split(delimiter)))

        negatives = [num for num in nums if num < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

        return sum(nums)
