import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Regular expression pattern for matching IPv4 address
    pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    # Match the input IP address against the pattern
    match = re.search(pattern, ip)

    # Return True if the IP address is valid, False otherwise
    return match is not None


if __name__ == "__main__":
    main()
