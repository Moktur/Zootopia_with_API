import requests

API_KEY = 'j8gaPNl1DUxHIF/Yg5cRzQ==14bN2SROUuBYDzQN'

def fetch_data(animal_name):
  """
  Fetches animal data from API.
  Returns: list of animal dictionaries or empty list if not found
  """
  api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
  response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
  
  if response.status_code == requests.codes.ok:
      return response.json()
  else:
      raise Exception(f"API Error: {response.status_code} - {response.text}")