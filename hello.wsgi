#activate_this = '/home/ubuntu/flask_tutorial/myproject/venv/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/home/ubuntu/flask_tutorial/myproject/flaskr/')

from testing import app as application 
