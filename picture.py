from flask import Flask
app = Flask(__name__)

@app.route('/picture')
def hello_world():
    return """
<html><head>
<title>Hello, World! From Egypt' </title>
</head>
<body>
<h1> Hello, World! From Egypt </h1>
<hr>
</body>
</html>
"""
