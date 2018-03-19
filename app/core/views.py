from ..core import core_blueprint
from .utils import read_sub_app, write_sub_app, add_tag
from flask import render_template


# begin of route list

@core_blueprint.route('/', methods=['GET', 'POST'])
def index():
    # TODO: 处理用户交互的情况，目前只有数据展示
    # TODO: 当回到主页时需要reset所有状态
    # 初步想法是用wtforms直接构建表单
    try:
        from .utils import InputForm
        form = InputForm()
    except ImportError:
        from .utils import DefaultForm
        form = DefaultForm()

    if form.validate_on_submit():
        user_input = form.content.data
        write_sub_app(user_input)

    sub_output = add_tag(read_sub_app(), 'p')
    return render_template('index.html', content=sub_output, form=form)
