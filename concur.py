from threading import Thread


def add(a, b):
    print(a + b)


# START
thr = Thread(target=add, args=(1, 2), daemon=True)
thr.start()
# END

thr.join()
