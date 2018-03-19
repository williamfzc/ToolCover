from app.core.api import need_value


def test_func(test_input):
    return 'HERE IS INPUT： {}'.format(str(test_input))


if __name__ == '__main__':
    print('hello from inside!')
    print('hello from inside again!!')
    # TODO: 需要处理input
    user_input = need_value('need a input to inside')
    feedback = test_func(user_input)
    # sys.stdout.write(feedback)
