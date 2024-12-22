import sys


def main(*args: None) -> int:
    for n in range(1 << 20):
        sys.stdout.write(f"{n}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
