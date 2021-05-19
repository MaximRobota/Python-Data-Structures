from hash_map import HashMap

from time import time
from tqdm import tqdm


def time_it(a_func):
    start = time()
    a_func()
    return time() - start


def filterrr(times):
    avg = sum(times) / len(times)
    new = []
    for t in times:
        if t < avg:
            new.append(t)
        else:
            new.append(0)
    return new


def window_smoother(times, window=40):
    new = []
    for i in range(len(times)):
        if i < window or i > len(times) - window:
            continue
        s = 0
        l = len(range(i - window, i + window))
        for j in range(i - window, i + window):
            s += times[j]
        new.append(s / l)
    return new


def main():
    el_count = 50000
    hash_map_time1 = window_smoother(filterrr(hash_map_test(el_count, load=0.01)))  # r
    hash_map_time2 = window_smoother(filterrr(hash_map_test(el_count, load=0.1)))  # g
    hash_map_time3 = window_smoother(filterrr(hash_map_test(el_count, load=0.75)))  # y
    dict_time = window_smoother(filterrr(dict_test(el_count)))

    import matplotlib.pyplot as plt

    plt.plot(hash_map_time1, 'r')  # plotting t, a separately
    plt.plot(hash_map_time2, 'g')  # plotting t, a separately
    plt.plot(hash_map_time3, 'y')  # plotting t, a separately
    plt.plot(dict_time, 'b')  # plotting t, b separately
    plt.show()


def hash_map_test(el_count, load):
    times = []
    hash_map = HashMap(load_factor=load)
    for x in range(el_count):
        times.append(time_it(lambda: hash_map.put(str(x), str(x))))
    return times
    # for x in range(el_count):
    #     assert hash_map.get(str(x)) == str(x)


def dict_test(el_count):
    hash_map = dict()
    times = []

    def asd():
        hash_map[str(x)] = str(x)

    for x in range(el_count):
        times.append(time_it(asd))
    return times
    # for x in range(el_count):
    #     assert hash_map.get(str(x)) == str(x)


if __name__ == '__main__':
    main()
