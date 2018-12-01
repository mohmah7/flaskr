activate_this = '/home/ubuntu/flask_tutorial/myproject/flaskr/venv/bin/activate.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, '/home/ubuntu/flask_tutorial/myproject/flaskr/')

from testing import app as application 
