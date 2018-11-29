from flask import Flask
app = Flask(__name__)

@app.route('/picture')
def hello_world():
    return """
<html><head>
<title>Hello, World! From Egypt' </title>
</head>
<body>
<h1>  The numbers are  </h1>
<hr>
<FORM value="form" action="index" method="post">
   <P>
	 <INPUT type="submit" value="Return to index page">
   </P>
</FORM>
</body>
</html>
"""
