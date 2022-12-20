from client import Client
client = Client()
status = 1
while status:
  print("querying")
  status = client.query()


