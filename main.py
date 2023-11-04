from parsing import *
from chat_gpt import *

if __name__ == "__main__":
    name = input("What's the name of the professor you're looking for?")
    parser = Parser(name)
    blurb = parser.return_blurb()
    user_req = input("What do you want the email to the professor to request from them? This can be anything, such as "
                     "'Request research opportunities', or 'Request a meeting for a particular date'")
    print("Loading...")
    response = chat_response(blurb, user_req)
    print("This is your personalized email. Enjoy!")
    print(response)
