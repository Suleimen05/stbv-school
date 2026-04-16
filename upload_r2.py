import os
import boto3
from botocore.config import Config

account_id = "c535b29f1097dc11acb3b8f84431705a"
access_key_id = "0dbbe19fa37e1dcf14fb04af0aedc4ab"
secret_access_key = "75262ef42bf7544b75f29bbb83d3e5226ac2498a58e8eb873d707e5ddeef9fbf"
bucket_name = "stbv-assets"

s3 = boto3.client(
    's3',
    endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    config=Config(signature_version='s3v4'),
    region_name='auto'
)

def upload_directory(path, bucketname):
    print(f"Starting upload for directory: {path}")
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            local_path = os.path.join(root, file)
            # The S3 key should use forward slashes and not include the leading './' if any
            # We want it to be stored inside the bucket under 'doc/...'
            relative_path = os.path.relpath(local_path, start=".")
            # Ensure forward slashes for S3 key
            s3_key = relative_path.replace(os.path.sep, '/')
            
            try:
                s3.upload_file(local_path, bucketname, s3_key)
                count += 1
                if count % 10 == 0:
                    print(f"Uploaded {count} files...")
            except Exception as e:
                print(f"Failed to upload {local_path}: {e}")

    print(f"Finished uploading {count} files from '{path}' to bucket '{bucketname}'")

if __name__ == "__main__":
    upload_directory("doc", bucket_name)
    upload_directory("assets", bucket_name)
