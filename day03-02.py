import timeit
from statistics import mode as mde


def anti_mode(lis):
    return mode_or_tie(lis, tie=1).replace("1", "2").replace("0", "1").replace("2", "0")


def mode_or_tie(lis, tie=1):
    """sort the list so that "1" or "0" comes first in the case of tie

    mode() function always returns the first element for a tie
    """
    if tie == 1:
        return mde(list(reversed(sorted(lis))))
    else:
        return mde(list(sorted(lis)))


def filter_to_position(lists, mode=None, position=0, tie=1, anti=False):
    # print(f"{lists=}, {mode=}, {position=}")
    if len(lists) == 1:
        return lists[0]
    if anti:
        mode = "".join(
            [
                anti_mode(
                    lis,
                )
                for lis in list(zip(*[lis[position] for lis in lists]))
            ]
        )
    else:
        mode = "".join(
            [
                mode_or_tie(
                    lis,
                )
                for lis in list(zip(*[lis[position] for lis in lists]))
            ]
        )
    # print(f"{mode=}")

    return filter_to_position(
        list(filter(lambda x: x[position] == mode, lists)),
        mode=mode,
        position=position + 1,
        tie=tie,
        anti=anti,
    )


def main(f_read):
    data = [[character for character in line] for line in f_read.splitlines()]

    mode = "".join([mode_or_tie(l) for l in list(zip(*[lis for lis in data]))])
    anti_mode_ = mode.replace("1", "2").replace("0", "1").replace("2", "0")

    oxygen = filter_to_position(lists=data, mode=mode, position=0, tie=1)
    co2 = filter_to_position(lists=data, mode=anti_mode_, position=0, tie=0, anti=True)

    return int("".join(oxygen), 2) * int("".join(co2), 2)


if __name__ == "__main__":
    loops = 1000

    with open("data/data-day-03.txt", "r") as f:
        f_read = f.read()
        print(main(f_read))

    time_taken = timeit.timeit(lambda: main(f_read), number=loops)
    print(f"{time_taken=}")
