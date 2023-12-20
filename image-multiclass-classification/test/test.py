import requests
import base64
import json

img_path = 'data/test.png'

with open(img_path, 'rb') as f:
    encoded_img = base64.b64encode(f.read()).decode('utf-8')
data = {'image': encoded_img}
response = requests.post('http://127.0.0.1:5000/predict', json=data)
response_dict = json.loads(response.text)
print(response_dict)