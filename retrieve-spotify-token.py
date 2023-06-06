import requests, base64, json

#preparing request - replace clientID & clientSecret
api = "https://accounts.spotify.com/api/token"
headers = {}
data = {}
credentials = f"clientID:clientSecret"
credentialsBytes = credentials.encode('ascii')
credentialsBase64 = base64.b64encode(credentialsBytes)
finalCredentials = credentialsBase64.decode('ascii')
headers['Authorization'] = f"Basic {finalCredentials}"
data['grant_type'] = "client_credentials"

#getting the spotify API token
token_response = requests.post(api, headers=headers, data=data)
token = token_response.json()['access_token']