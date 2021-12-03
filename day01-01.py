from collections import Counter


def main():
    with open("data/data-day-01.txt") as f:
        data = f.readlines()
    c = Counter()
    for idx, line in enumerate(data):
        try:
            old = int(data[idx - 1].strip())
            new = int(line.strip())
            if old < new:
                print(old, new)
                c["up"] += 1
        except:
            pass
    return c


if __name__ == "__main__":
    c = main()
    print(c)
