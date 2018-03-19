from app import create_app
from app.core.runner import sub_app


app = create_app()


if __name__ == '__main__':
    try:
        app.run()
    except KeyboardInterrupt:
        sub_app.kill()
