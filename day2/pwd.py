import random
import string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--length', type=int, default=16)
parser.add_argument('--count', type=int, default=1)
parser.add_argument('--no-upper', action='store_true')
parser.add_argument('--no-digits', action='store_true')
parser.add_argument('--no-special', action='store_true')
args = parser.parse_args()

chars = string.ascii_lowercase
if not args.no_upper:
    chars += string.ascii_uppercase
if not args.no_digits:
    chars += string.digits
if not args.no_special:
    chars += '!@#$%^&*()_+-=[]{}|;:,.<>?'

for _ in range(args.count):
    password = ''.join(random.choice(chars) for _ in range(args.length))
    print(password)
