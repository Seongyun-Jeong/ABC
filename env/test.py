import time

i = 0
while True:
    time.sleep(.1)
    print(f"\r{i}", end="")
    i += 1
