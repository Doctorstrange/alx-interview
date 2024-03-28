#!/usr/bin/python3
"""
script that reads stdin line by
line and computes metrics:
"""
import sys

full_size = 0
status_codes = {}
line_count = 0

try:
    for line in sys.stdin:
        try:
            ip, date, request, status_code, file_size = line.split(" ", 4)
            file_size = int(file_size)
            full_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1
        except ValueError:
            pass

        line_count += 1
        if line_count % 10 == 0:
            print("File size:", full_size)
            print(*[f"{code}: {count}"
                    for code, count in sorted(status_codes.items())], sep="\n")

except KeyboardInterrupt:
    print("File size:", full_size)
    print(*[f"{code}: {count}"
            for code, count in sorted(status_codes.items())], sep="\n")
