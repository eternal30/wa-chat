from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)
chat_data = []

@app.route('/')
def index():
    return render_template('chat.html', chats=chat_data)

@app.route('/kirim', methods=['POST'])
def kirim():
    pesan = request.form['message']
    pengirim = request.form['sender']
    waktu = datetime.now().strftime('%H:%M')
    chat_data.append({'message': pesan, 'sender': pengirim, 'timestamp': waktu})
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
