#!/usr/bin/python3
"""Log parsing script."""

import sys


VALID_CODES = ['200', '301', '400', '401', '403', '404', '405', '500']


def print_stats(total_size, status_counts):
    """Print accumulated metrics."""
    print("File size: {}".format(total_size))

    for code in VALID_CODES:
        if status_counts.get(code, 0) > 0:
            print("{}: {}".format(code, status_counts[code]))


def parse_line(line):
    """Extract status code and file size from a log line."""
    try:
        parts = line.split()
        status_code = parts[-2]
        file_size = int(parts[-1])
        return status_code, file_size
    except (IndexError, ValueError):
        return None


def main():
    """Read stdin line by line and compute metrics."""
    total_size = 0
    line_count = 0
    status_counts = {}

    try:
        for line in sys.stdin:
            result = parse_line(line)

            if result is not None:
                status_code, file_size = result
                total_size += file_size

                if status_code in VALID_CODES:
                    status_counts[status_code] = (
                        status_counts.get(status_code, 0) + 1
                    )

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
