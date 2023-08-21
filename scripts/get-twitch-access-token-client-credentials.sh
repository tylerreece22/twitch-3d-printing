# Client credentials flow which only includes auth token with high ttl

# Warning: DO NOT share this token as it does not expire for a long time unless manually revoked

curl -X POST 'https://id.twitch.tv/oauth2/token' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d "client_id=${client_id}&client_secret=${client_secret}&grant_type=client_credentials"