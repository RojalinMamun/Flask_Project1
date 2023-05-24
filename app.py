from flask import Flask

FAI=Flask(__name__)

@FAI.route('/wish')
def wish():
    return "Hello Good Evening"

@FAI.route('/second')
def second():
    return "How are you"

if __name__=='__main__':
    FAI.run(debug=True)