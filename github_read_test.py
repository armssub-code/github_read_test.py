# GitHub Read Test 2026-11-18
# Verification ID: K7M-4829-ZQ

def calculate_value(a, b):
    return (a * 17) + (b * 23) - 41


def main():
    values = [7, 13, 29, 43]
    results = [calculate_value(x, 5) for x in values]

    print("Verification ID: K7M-4829-ZQ")
    print("Results:", results)
    print("Checksum:", sum(results))


if __name__ == "__main__":
    main()