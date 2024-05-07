exec in contianer and run

hydra create oauth2-client  --endpoint http://127.0.0.1:4445 --secret secret


client=$(hydra create client --endpoint http://127.0.0.1:4445/ --format json \ --grant-type client_credentials)

id = 55e0b756-2439-4fad-9ac7-f82f0d770f4b

secret = YJhe7Jeilp4eTIpetiemhMInnu


hydra perform client-credentials --endpoint http://127.0.0.1:4444/ --client-id 55e0b756-2439-4fad-9ac7-f82f0d770f4b --client-secret YJhe7Jeilp4eTIpetiemhMInnu

