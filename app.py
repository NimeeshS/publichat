from flask import Flask, render_template, session, url_for
from flask_socketio import SocketIO, emit
from messages import message_store

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session handling
socketio = SocketIO(app)

@app.route('/')
def index():
    """Main chat page."""
    mode = session.get('mode', 'light')  # Default to light mode
    return render_template('index.html', mode=mode)

@socketio.on('send_message')
def handle_send_message(data):
    """Handle new messages sent by users."""
    message = data.get('message')
    if message:
        # Check for mode commands
        if message.strip().lower() == '/dark':
            session['mode'] = 'dark'
            emit('update_mode', 'dark', broadcast=True)  # Notify all clients of the mode change
        elif message.strip().lower() == '/light':
            session['mode'] = 'light'
            emit('update_mode', 'light', broadcast=True)  # Notify all clients of the mode change
        else:
            message_store.add_message(message)
            emit('receive_message', message, broadcast=True)

@socketio.on('request_messages')
def handle_request_messages():
    """Send the stored messages to the client."""
    emit('load_messages', message_store.get_messages())

if __name__ == '__main__':
    socketio.run(app, debug=True)
    