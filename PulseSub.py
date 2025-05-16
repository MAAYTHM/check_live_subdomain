#!/usr/bin/env python3
import sys
import argparse
from multiprocessing import Pool, cpu_count
from socket import gethostbyname
import requests as rq

BANNER = r"""
 /$$$$$$$            /$$                      /$$$$$$            /$$
| $$__  $$          | $$                     /$$__  $$          | $$
| $$  \ $$ /$$   /$$| $$  /$$$$$$$  /$$$$$$ | $$  \__/ /$$   /$$| $$$$$$$
| $$$$$$$/| $$  | $$| $$ /$$_____/ /$$__  $$|  $$$$$$ | $$  | $$| $$__  $$
| $$____/ | $$  | $$| $$|  $$$$$$ | $$$$$$$$ \____  $$| $$  | $$| $$  \ $$
| $$      | $$  | $$| $$ \____  $$| $$_____/ /$$  \ $$| $$  | $$| $$  | $$
| $$      |  $$$$$$/| $$ /$$$$$$$/|  $$$$$$$|  $$$$$$/|  $$$$$$/| $$$$$$$/
|__/       \______/ |__/|_______/  \_______/ \______/  \______/ |_______/


PulseSub - Live Subdomain Checker
(c) 2025 Aayush Samriya
https://github.com/MAAYTHM/PulseSub

Quickly checks which subdomains are live and reachable.
"""

class BannerArgumentParser(argparse.ArgumentParser):
    def print_help(self, file=None):
        print(BANNER)
        super().print_help(file)
    def print_usage(self, file=None):
        print(BANNER)
        super().print_usage(file)

def check_subdomain(domain):
    domain = domain.strip()
    if not domain:
        return None
    try:
        res = gethostbyname(domain)
    except Exception:
        return None
    try:
        code = rq.head(f'https://{domain}/', timeout=2).status_code
        return (res, domain, code)
    except Exception:
        return None

def read_targets(args):
    targets = []
    if args.target:
        targets.append(args.target)
    elif args.file:
        with open(args.file, 'r') as f:
            targets = [line.strip() for line in f if line.strip()]
    elif not sys.stdin.isatty():
        targets = [line.strip() for line in sys.stdin if line.strip()]
    else:
        print("No targets provided. Use -t, -f, or pipe input.")
        sys.exit(1)
    return sorted(set(targets))

def main():
    # Always print banner and info
    print(BANNER)
    parser = BannerArgumentParser(
        description="SubPulse: Quickly check which subdomains are live and reachable.",
        epilog="Example: python pulsesub.py -f subdomains.txt -o live.txt"
    )
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-t", "--target", help="Single domain or subdomain to check")
    group.add_argument("-f", "--file", help="File containing domains/subdomains (one per line)")
    parser.add_argument("-o", "--output", default="live.txt", help="Output file (default: live.txt)")
    parser.add_argument("-c", "--concurrency", type=int, default=cpu_count(), help="Number of concurrent processes (default: CPU count)")

    args = parser.parse_args()
    targets = read_targets(args)

    if not targets:
        print("No valid targets found.")
        sys.exit(1)

    pool = Pool(args.concurrency)
    results = pool.map(check_subdomain, targets)
    pool.close()
    pool.join()

    with open(args.output, 'w') as f:
        for result in results:
            if result:
                print(f"{result[1]} -> {result[0]} & code - {result[2]}")
                f.write(f"{result[0]},{result[1]},{result[2]}\n")

    print(f'Finished. Results saved to {args.output}')

if __name__ == "__main__":
    main()
