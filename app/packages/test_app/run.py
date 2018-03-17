def test_func(test_input):
    return 'HERE IS INPUT： {}'.format(str(test_input))


if __name__ == '__main__':
    print('hi!!')
    user_input = input('Please input something: ')
    feedback = test_func(user_input)
    print(feedback)
