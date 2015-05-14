from flask import Flask, render_template, request, session, render_template
app = Flask(__name__)
app.secret_key = 'luthercollege'
app.debug=True



@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/foo')
def goodbye():
    return "<h1>Have a good weekend</h1>"

@app.route('/calc/<float:firstNum>/<changer>/<float:secondNum>')
def calculate(firstNum, secondNum, changer):
    
    if changer=="add":

        return "<h1>"+str(firstNum+secondNum)+"</h1>"
    
    elif changer=="sub":
        
        return "<h1>"+str(firstNum-secondNum)+"</h1>"

    elif changer=="mul":

        return "<h1>"+str(firstNum*secondNum)+"</h1>"

    elif changer=="div":

        return "<h1>"+str(firstNum/secondNum)+"</h1>"

    else:

        return "<h1>Error...wrong input!</h1>"

@app.route('/todo')
def listtasks():
    f = open('todo.txt')
    todolist = f.readlines()
    f.close()
    return render_template('todo.html',todolist=todolist)





if __name__ == '__main__':#for debugging
    app.run()
