# Auth code flow which includes both auth token and refresh token with lower expiry time

# Add correct client_id and click this link for your authorization code
# https://id.twitch.tv/oauth2/authorize?response_type=code&client_id=<your client id>&redirect_uri=http://localhost:3000&scope=chat%3Aread+chat&3Aedit&state=c3ab8aa609ea11e793ae92361f002671

curl -X POST 'https://id.twitch.tv/oauth2/token' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d "client_id=${client_id}&client_secret=${client_secret}&code=${authorization_code}&grant_type=authorization_code&redirect_uri=http://localhost:3000"