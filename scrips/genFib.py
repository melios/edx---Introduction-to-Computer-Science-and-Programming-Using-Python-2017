def genFib():
    fibn_1 = 1 # fib(n-1)
    fibn_2 = 0 # fib(n-2)

    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

if __name__ == "__main__":
    fib = genFib()
    print(fib.__next__())
    print(fib.__next__())
    print(fib.__next__())
    print(fib.__next__())
    print(fib.__next__())
    print(fib.__next__())
    print(fib.__next__())
    print(fib.__next__())
    print(fib.__next__())
    print(fib.__next__())
    print(fib.__next__())
    print(fib.__next__())

    # # evaluating all fubinacci number
    # # produce of all the fibonacci numbers as infinite sequence
    # for n in genFib():
    #     print(n)