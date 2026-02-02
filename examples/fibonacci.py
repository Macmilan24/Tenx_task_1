from typing import List
import argparse


def fibonacci(count: int) -> List[int]:
    """Return the first `count` numbers of the Fibonacci sequence.

    Args:
        count: Number of terms to generate (must be non-negative).

    Returns:
        A list of integers representing the sequence.
    """
    if count < 0:
        raise ValueError("count must be non-negative")

    sequence: List[int] = []
    a: int = 0
    b: int = 1

    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Fibonacci sequence")
    parser.add_argument(
        "--count",
        "-c",
        type=int,
        default=10,
        help="Number of terms to generate (default: 10)",
    )
    args = parser.parse_args()

    try:
        seq = fibonacci(args.count)
        print(" ".join(str(x) for x in seq))
    except ValueError as exc:
        print(f"Error: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
