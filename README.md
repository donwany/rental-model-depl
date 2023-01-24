### USAGE
```python
python app.py
```
### Build Docker Image
   - CHANGE DOCKER USERNAME TO YOUR OWN <worldbosskafka>
   - CHOOSE ANY PORT YOU WANT
```shell
# build image
docker build -t worldbosskafka/rent-model-app:1.0.0 .

# run image
docker run -p 1957:1957 worldbosskafka/rent-model-app:1.0.0

# do not push if you don't have dockerhub setup
docker push worldbosskafka/rent-model-app:1.0.0
```

### HOW TO TEST ENDPOINT
```python
import requests
import json

# REPLACE THIS URL TO YOURS
url = "http://0.0.0.0:1957/predict"

payload = json.dumps({"postcode":35037,
                      "sqm": 20,
                      "rooms": 1,
                      "has_balcony": 0,
                      "has_kitchen": 1,
                      "has_garden": 1})
headers = {
    'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```
### RUN THIS FROM TERMINAL
   - REPLACE THIS URL TO YOURS:
   - http://0.0.0.0:1957/predict
```shell
curl --request POST 'http://0.0.0.0:1957/predict' \
 --header 'Content-Type: application/json' \
 --data-raw '{
    "postcode":35037,
    "sqm": 20,
    "rooms": 1,
    "has_balcony": 0,
    "has_kitchen": 1,
    "has_garden": 1
}'
```