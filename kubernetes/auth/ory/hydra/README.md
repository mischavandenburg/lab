# Create Hydra DB

CREATE DATABASE hydra OWNER app;
GRANT ALL PRIVILEGES ON DATABASE hydra TO app;
\c hydra
ALTER ROLE app SET role 'app';

# Client

From https://github.com/shodgson/ory-kratos-hydra-integration-demo

Create a client

curl --request POST \
  --url http://hydra.admin.local.com/admin/clients \
  --header 'Content-Type: application/json' \
  --data '{
  "grant_types": [
    "authorization_code",
    "refresh_token"
  ],
  "redirect_uris": [
    "http://127.0.0.1:5555/callback"
  ],
  "response_types": [
    "code",
    "id_token"
  ],
  "scope": "openid offline",
  "token_endpoint_auth_method": "none"
}'


http://http://hydra.admin.local.com/oauth2/auth?client_id=$CLIENT_ID&redirect_uri=http%3A%2F%2F127.0.0.1%3A5555%2Fcallback&response_type=code&state=1102398157&scope=offline%20openid

http://hydra.public.local.com/oauth2/auth?client_id=a6863507-7693-4c20-a63a-57565e53bfe7&redirect_uri=http%3A%2F%2F127.0.0.1%3A5555%2Fcallback&response_type=code&state=1102398157&scope=offline%20openid
