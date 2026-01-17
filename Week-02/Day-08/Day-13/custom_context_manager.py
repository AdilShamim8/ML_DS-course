import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.perf_counter()
        print(f"Elapsed: {end - self.start:.4f} seconds")

# Usage:
with Timer():
    total = sum(range(1000000))