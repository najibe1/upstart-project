from google.cloud import storage

client = storage.Client.from_service_account_json('/opt/spark/gcs/keyfile.json')
buckets = list(client.list_buckets())
print("Buckets acessíveis:", [b.name for b in buckets])