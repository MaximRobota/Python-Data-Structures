from hash_map import HashMap

from time import time
from tqdm import tqdm

def time_it(a_func):
    start = time()
    a_func()
    return time() - start


def main():
    # x = [int(1.1 ** i) for i in range(1, 67)]
    x = [int(i) for i in range(10, 50000, 2000)]
    hash_map_time1 = []
    hash_map_time2 = []
    hash_map_time3 = []
    dict_time = []
    for el_count in tqdm(x):
        hash_map_time1.append(time_it(lambda: hash_map_test(el_count, load=0.1))) # r
        hash_map_time2.append(time_it(lambda: hash_map_test(el_count, load=0.3))) # g
        hash_map_time3.append(time_it(lambda: hash_map_test(el_count, load=1))) # y
        dict_time.append(time_it(lambda: dict_test(el_count)))

    import matplotlib.pyplot as plt

    plt.plot(x, hash_map_time1, 'r')  # plotting t, a separately
    plt.plot(x, hash_map_time2, 'g')  # plotting t, a separately
    plt.plot(x, hash_map_time3, 'y')  # plotting t, a separately
    plt.plot(x, dict_time, 'b')  # plotting t, b separately
    plt.show()


def hash_map_test(el_count, load):
    hash_map = HashMap(load_factor=load)
    for x in range(el_count):
        hash_map.put(str(x), str(x))
    # for x in range(el_count):
    #     assert hash_map.get(str(x)) == str(x)


def dict_test(el_count):
    hash_map = dict()
    for x in range(el_count):
        hash_map[str(x)] = str(x)

    # for x in range(el_count):
    #     assert hash_map.get(str(x)) == str(x)


if __name__ == '__main__':
    main()
