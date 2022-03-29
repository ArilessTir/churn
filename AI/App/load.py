import requests
import time


url = 'http://127.0.0.1:8000/prediction'

payload = "{\n \"CustomerId\": 15634602,\n    \"Surname\": \"Hargrave\",\n    \"CreditScore\": 619,\n    \"Geography\": \"France\",\n    \"Gender\": \"Female\",\n    \"Age\": 42,\n    \"Tenure\": 2,\n    \"Balance\": 0.0,\n    \"NumOfProducts\": 1,\n    \"HasCrCard\": 1,\n    \"IsActiveMember\": 1,\n    \"EstimatedSalary\": 101348.88}"
headers = {
    'Content-Type': 'application/json'
}


for i in range(10):
    time.sleep(0.5)
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
