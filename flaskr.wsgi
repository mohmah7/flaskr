import sys
sys.path.insert(0, '/home/ubuntu/flask_tutorial/myproject/flaskr')

from flasker import app as application

activate_this = '/ubuntu/home/flask_tutorial/myproject/venv/bin/'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))


