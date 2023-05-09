class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity,int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity=capacity
        self.cookies=0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if self.cookies + n > self.capacity:
            raise ValueError("Capacity filled")
        self.cookies += n

    def withdraw(self, n):
        if n > self.cookies:
            raise ValueError("Not enough cookies in the jar")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies
