# from flask import Flask,request
# import json
# app=Flask(__name__)

# @app.route("/")
# def index():
#     return f"Hi this is Dinesh"

# @app.route('/post/', methods=['POST','GET'])
# def index1():
#     if request.method == 'POST':
#         return json.dumps(request)
#     else:
#         return f"Get method"    
# if __name__=="__main__":
#     app.run(debug=True)


from  flask import Flask
app=Flask(__name__)

@app.route("/")
def get():
    return f"this is get"

if __name__=="__main__":
    app.run()

