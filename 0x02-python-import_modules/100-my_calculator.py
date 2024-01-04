#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>'.format(argv[0]))
        exit(1)
    oper = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
            }
    if argv[2] in oper:
        calc1 = int(argv[1])
        calc2 = int(argv[3])
        ops = oper[argv[2]]
        res= ops(calc1, calc2)
        print('{:d} {:s} {:d} = {:d}'.format(calc1, argv[2], calc2, res))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    exit(0)
