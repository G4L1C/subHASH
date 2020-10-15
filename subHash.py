#!/usr/bin/python3

import itertools
import string
import argparse
import hashlib
import sys


def welcome_message():
    print(r'''
           _     _    _           _____ _    _ 
          | |   | |  | |   /\    / ____| |  | | {by G4L1C v1.0}
 ___ _   _| |__ | |__| |  /  \  | (___ | |__| |
/ __| | | | '_ \|  __  | / /\ \  \___ \|  __  |
\__ \ |_| | |_) | |  | |/ ____ \ ____) | |  | |
|___/\__,_|_.__/|_|  |_/_/    \_\_____/|_|  |_|

''')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find a collision to a given MD5 substring.')
    parser.add_argument('--subHash', '-sh', help='Hash substring to be collised.', required=True)
    parser.add_argument('--sChar', '-sc', type=int, help='Starting posistion of the hash substring (start=0).',default=0)
    args = parser.parse_args()

    length = 1
    trial = 1
    char_list = string.ascii_letters + string.digits + string.punctuation

    welcome_message()
    print(f'[+] Started collision for: {args.subHash}')
    print(f'[+] Starting hash substring position: {args.sChar}')
    print(f'[+] Substring length: {len(args.subHash)}')

    while length <= 16:
        for word in itertools.combinations(char_list, length):
            print(f'[+] Number of trials: {trial}', end='\r')
            if args.subHash == hashlib.md5(''.join(word).encode()).hexdigest()[args.sChar:len(args.subHash)]:
                print('\r')
                print(f'[+] Collision found: {"".join(word)}')
                print(f'[+] Hashed collision: {hashlib.md5("".join(word).encode()).hexdigest()}')
                sys.exit(0)
            trial += 1
        length += 1

    print('[+] Collision not found! Make sure the substring is not too long.')
