from flask import Flask, request, session, make_response
from twilio.twiml.messaging_response import MessagingResponse
from s2bot import ask, append_interation_to_chat_log

app = Flask(__name__)
# if for some reason your conversation with the bot gets weird, change the secret key
app.config['SECRET_KEY']='89djhf9jhkd93'

@app.route('/')
def path_home():
    headers = {"Content-Type": "application/json"}
    return make_response(
        'Test worked!',
        200,
        headers=headers
    )

#@app.route('/s2bot', methods=['POST'])
@app.route('/s2bot', methods=['GET'])
def path_s2bot():
    incoming_msg = request.values['BODY']
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interation_to_chat_log(incoming_msg, answer, chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)

if __name__ == '__main__':
    app.run(debug=True)
