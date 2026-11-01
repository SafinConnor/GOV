"""Basic Python assignment program with core arithmetic functions."""

from __future__ import annotations


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def run(operation: str, a: float, b: float) -> float:
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")

    return operations[operation](a, b)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Simple calculator program for a basic software development assessment."
    )
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"])
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)

    args = parser.parse_args()

    result = run(args.operation, args.a, args.b)
    print(result)
