import timeit


def main(f_read):
    data = tuple((c, int(d)) for c, d in [line.split(" ") for line in f_read.splitlines()])

    horiz = sum(d[1] for d in tuple(filter(lambda x: x[0] == "forward", data)))

    depth = 0
    aim = 0

    for d in data:
        if d[0] == "up":
            aim -= d[1]
        elif d[0] == "down":
            aim += d[1]
        else:
            depth += d[1] * aim

    return depth, horiz, horiz * depth


if __name__ == "__main__":
    loops = 1000

    with open("data/data-day-02.txt", "r") as f:
        f_read = f.read()
        print(main(f_read))

    time_taken = timeit.timeit(lambda: main(f_read), number=loops)
    print(f"{time_taken=}")
