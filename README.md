# url_shortner
Web service to shorten urls

## Instructions and Notes
Built on Ubuntu 21.04<br>
Python 3.9.5

### Requirements
1. Python 3.9.5
2. Flask (pip install flask)
3. Flask Restufl (pip install flask-restful)
4. If using a IDE like ATOM: pip install --no-binary=python-language-server 'python-language-server[all]'
5. Postman (or other API testing suite)

### Instructions
1. clone the respository. 
2. cd into repository.
3. execute python3 url_shortner.py
4. will deploy to 127.0.0.1:5001. If you would like to change the port please adjust the port parameter in the __main__ function of url_shortner.py
5. Once deployed use your favorite API testing suite to test both the shortening and retrieval features

### Endpoints:<br>
Post: /url_shorten/<br>
Get: /url/<id><br>

### Post Example:<br>
127.0.0.1:5001/url_shorten/<br>
key: url<br>
value: http:://www.test.com/this/is/a/test

### Get Example:<br>
127.0.0.1:5001/url/<id>
