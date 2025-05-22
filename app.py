from flask import Flask, request, make_response, jsonify

app = Flask(__name__, instance_relative_config=True)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a+b), 200) #HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST

#Endpoint /sub for subtraction which takes a and b as query parameters.

@app.route('/sub')
def sub():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a-b), 200) #HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST
#Endpoint /mul for multiplication which takes a and b as query parameters.

@app.route('/mul')
def mul():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a*b), 200) #HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST
#Endpoint /div for division which takes a and b as query parameters. Returns HTTP 400 BAD REQUEST also for division by zero.

@app.route('/div')
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a/b), 200) #HTTP 200 OK
    elif b == 0:
        # division by zero
       return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST
    else:
        return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST
#Endpoint /mod for modulo which takes a and b as query parameters. Returns HTTP 400 BAD REQUEST also for division by zero.
@app.route('/mod')
def modulo():
    a = request.args.get('a')
    b = request.args.get('b')

    if a is None or b is None:
        # missing parameters
        abort(400, description="'a' and 'b' query parameters are required")
    elif not is_number(a) or not is_number(b):
        # non-numeric input
        abort(400, description="'a' and 'b' must be valid numbers")
    elif float(b) == 0.0:
        # modulo (division) by zero
        abort(400, description="Modulo by zero is not allowed")
    else:
        result = float(a) % float(b)
        return jsonify({"result": result})
#Endpoint /random which takes a and b as query parameters and returns a random number between a and b included. Returns HTTP 400 BAD REQUEST if a is greater than b.

if __name__ == '__main__':
    app.run(debug=True)