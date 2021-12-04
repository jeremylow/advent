import timeit
from statistics import mode as mde


def main(f_read):
    data = [[character for character in line] for line in f_read.splitlines()]
    mode = "".join([mde(l) for l in list(zip(*[lis for lis in data]))])
    anti_mode = mode.replace("1", "2").replace("0", "1").replace("2", "0")

    return int(mode, 2) * int(anti_mode, 2)


if __name__ == "__main__":
    loops = 1000

    with open("data/data-day-03.txt", "r") as f:
        f_read = f.read()
        print(main(f_read))

    time_taken = timeit.timeit(lambda: main(f_read), number=loops)
    print(f"{time_taken=}")
