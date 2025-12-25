import time

class LCG:
    def __init__(self, seed=None):
        if seed is None:
            seed = int(time.time())
        self.seed = seed
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def next_float(self):
        return self.next() / self.m


if __name__ == "__main__":
    rng = LCG()
    print("Generated random numbers:")
    for _ in range(10):
        print(rng.next_float())
