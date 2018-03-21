"""
HERE IS A EXAMPLE
"""

# support markdown
markdown_template = '''
## Result report

These result comes from inner app.

### Your Name

{user_name}

### Your Password

{password}

'''

if __name__ == '__main__':
    # as a user, all you need to do is nothing.
    # edit your code as usual!
    # you can add some introduction it in README.md

    user_name = input('Please input your account.')
    password = input('And what\'s your password?')

    # of course, also you can use markdown to show your result
    print(markdown_template.format(
        user_name=user_name, password=password
    ))
    # if not, string is ok
    print('This is what you have done.')

    # end of what you need


# ----- ONLY FOR DEBUG -----
def __debug():
    import os
    DIR_PATH = os.path.dirname(__file__)

    with open(os.path.join(DIR_PATH, 'test.log'), 'w+') as f:
        try:
            print('welcome to login')
            user_name = input('Please input your account.')
            f.write(user_name)
            password = input('And what\'s your password?')
            f.write(password)
            print('ok you have done.')
        except BaseException as e:
            f.write(e)
        finally:
            f.write('fucking done')
