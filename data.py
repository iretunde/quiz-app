import requests

response = requests.get(url='https://opentdb.com/api.php?amount=10&category=31&type=boolean')
question_data = response.json()['results']



