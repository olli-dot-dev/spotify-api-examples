from requests import post
import base64

code="YOUR-CODE-HERE"
REDIRECT_URI="" #whatever you whitelistet on Spotify for your app

credentials = f"clientID:clientSecret"
credentialsBytes = credentials.encode('ascii')
credentialsBase64 = base64.b64encode(credentialsBytes)
finalCredentials = credentialsBase64.decode('ascii')
token_data = {
     'grant_type': 'authorization_code',
     'code': code,
     'redirect_uri': REDIRECT_URI 
}
token_header = {
     'Authorization': f'Basic {finalCredentials}',
     'Content-Type': 'application/x-www-form-urlencoded'
}

response = post('https://accounts.spotify.com/api/token', data=token_data, headers=token_header)
print(response)
access_token = response.json()['access_token']
refresh_token = response.json()['refresh_token']
#access-token is valid for 60 minutes
print("access_token:",access_token)
#use refreh-token to get a new access-token
print("refresh_token:",refresh_token)