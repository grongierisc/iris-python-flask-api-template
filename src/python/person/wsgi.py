from app import app

# Dev:
# cd /irisdev/app/src/Python/flask
# $PYTHON_PATH -m gunicorn --bind "0.0.0.0:8081" wsgi:app

if __name__ == '__main__':
    app.run()