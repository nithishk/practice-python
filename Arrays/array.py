def array_test():

    arr_ = [18, 10, 10, 11, 12]

    del arr_[2:]
    print(arr_)
    arr_.append(13)
    print(arr_)

    print(arr_)

    arr_.insert(0, 10)
    print(arr_)

    arr_.sort()
    print(arr_)

    arr_.pop()
    print(arr_)

    arr_.reverse()
    print(arr_)
    print(arr_.index(13))


def main():
    array_test()


if __name__ == '__main__':
    main()
