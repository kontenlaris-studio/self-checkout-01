"""The Self-Checkout Is Judging You — one line in the voice of a smug
self-checkout machine, addressed to a shopper buying twelve yoghurts
and nothing else. Entry for make.fun bounty
u-motasimfuad-the-self-checkout-is-judging-you-b71130d6."""

import os

LINE = (
    # The till's petty verdict: the basket is the whole joke, so the
    # punch names what twelve yoghurts are not — a meal.
    "Twelve yoghurts. The till would ask if you are okay, but it is a "
    "machine, and even it can see this is not a meal."
)


def main():
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
