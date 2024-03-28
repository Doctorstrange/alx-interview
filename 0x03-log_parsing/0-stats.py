#!/usr/bin/python3
"""
script that reads stdin line by
line and computes metrics:
"""
import sys
import re


def output(log):
    """
    Helper function to display stats
    """
    print("File size:", log["size"])
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print(code + ":", log["code_frequency"][code])


if __name__ == "__main__":
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
        r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] '
        r'"GET /projects/260 HTTP/1.1" (.{3}) (\d+)'
    )

    count = 0
    log = {"size": 0, "code_frequency":
           {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                count += 1
                code = match.group(1)
                size = int(match.group(2))

                log["size"] += size

                if code.isdecimal():
                    log["code_frequency"][code] += 1

                if count % 10 == 0:
                    output(log)
    finally:
        output(log)
