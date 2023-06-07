import base64, json
from requests import post

refresh_token="YOUR_REFRESH_TOKEN_HERE"

credentials = f"clientID:clientSecret"
credentialsBytes = credentials.encode('ascii')
credentialsBase64 = base64.b64encode(credentialsBytes)
finalCredentials = credentialsBase64.decode('ascii')
form_data = {
     'grant_type': 'refresh_token',
     'refresh_token': refresh_token
}
token_header = {
     'Authorization': f'Basic {finalCredentials}',
     'Content-Type': 'application/x-www-form-urlencoded'
}

response = post('https://accounts.spotify.com/api/token', data=form_data, headers=token_header)

access_token=response.json()['access_token']
print(access_token)