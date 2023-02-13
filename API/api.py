import requests

url = "https://api.spoonacular.com/recipes/complexSearch"
api_key = "2d8c74c3feeb4d0cb335c902d9e93b66"

params = {
    "query": "pasta",
    "number": 10
}

response = requests.get(url, params=params, headers={"apiKey": api_key})

if response.status_code == 200:
    data = response.json()
    # Parse and extract data as needed
else:
    print("Error retrieving data from API")