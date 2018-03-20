import os

DIR_PATH = os.path.dirname(__file__)


if __name__ == '__main__':

    with open(os.path.join(DIR_PATH, 'test.log'), 'w+') as f:
        try:
            print('welcome to login')
            user_input = input('your account')
            f.write(user_input)
            password = input('your password')
            f.write(password)
        except BaseException as e:
            f.write(e)


