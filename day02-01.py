"""the tuple comprehension is a bit much i'll admit"""

import timeit


def main(f_read):
    data = tuple(
        (c, int(d)) for c, d in [line.split(" ") for line in f_read.splitlines()]
    )

    horiz = sum(d[1] for d in list(filter(lambda x: x[0] == "forward", data)))
    vert = sum(
        tuple(
            -d[1] if d[0] == "up" else d[1]
            for d in list(filter(lambda x: x[0] != "forward", data))
        )
    )

    return horiz * vert


if __name__ == "__main__":
    loops = 5000

    with open("data/data-day-02.txt", "r") as f:
        f_read = f.read()

    print(main(f_read))
    time_taken = timeit.timeit(lambda: main(f_read), number=loops)
    print(f"{time_taken=}")
