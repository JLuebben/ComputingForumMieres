import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

from sys import argv
# argv = ['-h']
# args = parser.parse_args(argv)
# print(args.accumulate(args.integers))


argv = ['1', '2', '5', '3']
args = parser.parse_args(argv)
print(args.accumulate(args.integers))


argv = ['1', '2', '5', '3', '--sum']
args = parser.parse_args(argv)
print(args.accumulate(args.integers))