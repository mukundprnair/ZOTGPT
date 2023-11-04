from parsing import *
from chat_gpt import *
from flask import Flask, render_template, request
from parsing import *
from chat_gpt import *

app = Flask(__name__)




@app.route('/submit', methods=['POST'])
def submit_form():
    # name of the professor
    input1 = request.form.get('input1')

    # Type of request like research or coffee chat
    input2 = request.form.get('input2')

    
    #input3 = request.form.get('input3')
    
    # Process the form data as needed
    print(input1)

    parser = Parser(input1)
    blurb = parser.return_blurb()
    #user_req = input("What do you want the email to the professor to request from them? This can be anything, such as "
                    # "'Request research opportunities', or 'Request a meeting for a particular date'")
    print("Loading...")
    response = chat_response(blurb, input2)
    print("This is your personalized email. Enjoy!")
    print(type(response))

    #return f'Input 1: {input1}, Input 2: {response}'
    return render_template('response.html', text_from_python=response)


@app.route('/')
def index():
    text_from_python = "Hello, this text comes from Python!"
    return render_template('index.html', text_from_python=text_from_python)

if __name__ == '__main__':
    app.run(debug=True)
