import json
import requests
sess = requests.get('https://api.ownthink.com/bot?spoken=中国')
answer = sess.text
answer = json.loads(answer)
print(answer)