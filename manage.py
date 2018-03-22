from app import create_app
from app.core.runner import sub_app


app = create_app()


if __name__ == '__main__':
    try:
        # TODO：如果同时有多个人访问
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        sub_app.stop()
