import sys


def test_func(test_input):
    return 'HERE IS INPUT： {}'.format(str(test_input))


if __name__ == '__main__':
    sys.stdout.write('hi!!!\n')
    user_input = sys.stdin.read()
    feedback = test_func(user_input)
    sys.stdout.write(feedback)
