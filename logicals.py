# Note to self: you were trying to make a higher level logic system as seen in
# the average function


class Logical():
    def __init__(self, nums):
        self.nums = nums
        self.length = len(nums)
        self.__normalize()
        self.average = sum(self.nums) / self.length

    def __normalize(self):
        for i in range(self.length):
            if self.nums[i] != 0:
                self.nums[i] = 1

    def __str__(self):
        return str(self.nums)

    def __repr__(self):
        return repr(self.nums)

    def __add__(self, other):
        if self.length == other.length:
            result = []
            for i in range(self.length):
                result.append(self.nums[i] + other.nums[i])
            return Logical(result)
        else:
            raise ValueError('can only add Logicals of the same length')

    def __sub__(self, other):
        if self.length == other.length:
            result = []
            for i in range(self.length):
                result.append(self.nums[i] - other.nums[i])
            return Logical(result)
        else:
            raise ValueError('can only subtract Logicals of the same length')

    def __mul__(self, other):
        if self.length == other.length:
            result = []
            for i in range(self.length):
                result.append(self.nums[i] * other.nums[i])
            return Logical(result)
        else:
            raise ValueError('can only multiply Logicals of the same length')

    def __neg__(self):
        result = []
        for i in range(self.length):
            if self.nums[i] == 0:
                result.append(1)
            else:
                result.append(0)
        return Logical(result)

    def __eq__(self, other):
        if self.average == other.average:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.average != other.average:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.average < other.average:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.average > other.average:
            return True
        else:
            return False

    def __le__(self, other):
        if self < other or self == other:
            return True
        else:
            return False

    def __ge__(self, other):
        if self > other or self == other:
            return True
        else:
            return False

    # def average(self):
    #     result = sum(self.nums) / self.length
    #     if result > 0.5:
    #         return True
    #     else:
    #         return False

    def wave(self):
        result = 0
        for i in range(self.length):
            result += self.nums[i] ** 2
        return result ** (1 / 2)


def zeros(n):
    result = []
    for i in range(n):
        result.append(0)
    return Logical(result)


def ones(n):
    result = []
    for i in range(n):
        result.append(1)
    return Logical(result)


x = Logical([1, 0, 1, 1, 0, 1, 0, 0])
y = Logical([1, 1, 0, 0, 0, 1, 0, 1])
o = Logical([1, 0, 0, 0, 0, 1, 0, 1])
print(x == y)
