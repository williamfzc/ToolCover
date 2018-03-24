"""
HERE IS A EXAMPLE
"""

# as a user, all you need to do is nothing.
# edit your code as usual!
# you can add some introduction it in README.md


# try to input something?
introduction_of_normal_input = '''

## normal input

try to input something?

nothing different with terminal app.

```user_name = input('Please input something.\n')```

and it will become:

---

'''

print(introduction_of_normal_input)
user_name = input('Please input something.\n')


# special widget
introduction_of_special_widget = '''

## special widget

you can simply build special widget, with a string split with '|':  

1. type of widget
2. description
3. choice list, split with '%'

seems like:  

```choice = input('single-list|Select your type|choice1%choice2%choice3')```

and it will become:  

---

'''
print(introduction_of_special_widget)
choice = input('single-list|Select your type|choice1%choice2%choice3')


# of course, also you can use markdown to show your result
introduction_of_show_result = '''

At the end, of course, also you can use markdown to show your result.  

## Result report

Result comes from inner app, with markdown.

### result1

this is result1.

### result2

this is result2.

Tap [this](https://github.com/williamfzc/ToolCover/blob/master/app/packages/test_app/run.py) view the code.

'''
print(introduction_of_show_result)

# end of what you need
