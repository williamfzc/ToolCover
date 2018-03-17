import sys


def test_func(test_input):
    return 'HERE IS INPUT： {}'.format(str(test_input))


if __name__ == '__main__':
    num_of_args = len(sys.argv - 1)
    if sys.argv == 1:
        test_func(sys.argv[1])
