import _signal
import time


def handler(signum, time):
    print(f"\nI got a SIGINT({signum}), but I am not stopping")


_signal.signal(_signal.SIGINT, handler)
i = 0
while True:
    time.sleep(.1)
    print(f"\r{i}", end="")
    i += 1
