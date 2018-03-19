import sys


def test_func(test_input):
    return 'HERE IS INPUT： {}'.format(str(test_input))


if __name__ == '__main__':
    # they are the same:
    user_input = input('need a input to inside')
    password = input('your password')

