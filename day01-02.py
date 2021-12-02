def main():
    with open("data-day-01.txt") as f:
        data = [int(d) for d in f.read().splitlines()]
    c = 0
    for idx, line in enumerate(data):
        try:
            old_list, new_list = data[idx : idx + 3], data[idx + 1 : idx + 4]
            old, new = sum(old_list), sum(new_list)
        except:
            pass

        if old < new:
            c += 1
    return c


if __name__ == "__main__":
    c = main()
    print(c)
