import time


def start_timer():
    return time.perf_counter()


def stop_timer(start):
    elapsed = time.perf_counter() - start
    print(f"Execution Time : {elapsed:.6f} seconds")