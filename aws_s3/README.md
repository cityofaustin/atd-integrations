# Security Note

**IMPORTANT: Do not push code with passwords, access keys, api tokens or any other sensitive information.**


# AWS S3 Integration (Effort Level: Low)

### Purpose

We need an integration that can take a key-value json document and inserts the values into a google sheet. 

Example Article:
https://medium.com/bilesanmiahmad/how-to-upload-a-file-to-amazon-s3-in-python-68757a1867c6

Sample Configuration:

```json
{
	"aws_s3_bucket": {
        "name": "Form Submissions Archive",
		"bucket_name": "valid-bucket-name",
        "bucket_path": "valid/path/in/bucket",
        "aws_region_name": "region_name",
		"aws_access_key_id": "xxxxxxxxxxxxxxxxxxxxxxx",
        "aws_secret_access_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	}
}
```

We can assume these details will be provided at runtime; however, you can use your own keys and your own bucket at this time, as well as your own access key id and secret access key to write objects to S3.

Integration Sample Code (from the link above)

```python
import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXX'
SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws('local_file', 'bucket_name', 's3_file_name')
```

The method they propose assumes that the file is somewhere in disk, where for us that is not the case. Here is an article ([how to write a file to s3](https://stackoverflow.com/questions/40336918/how-to-write-a-file-or-data-to-an-s3-object-using-boto3)) that describes how to save to file then upload, and a second method that saves straight from memory into s3 (code not tested or verified, provided as an example):

```python
import boto3

some_binary_data = b'Here we have some data'
more_binary_data = b'Here we have some more data'

# Method 1: Object.put()
s3 = boto3.resource('s3')
object = s3.Object('my_bucket_name', 'my/key/including/filename.txt')
object.put(Body=some_binary_data)

# Method 2: Client.put_object()
client = boto3.client('s3')
client.put_object(Body=more_binary_data, Bucket='my_bucket_name', Key='my/key/including/anotherfilename.txt')
```

# Assumptions

1. You can assume this function will provide the configuration as a python dictionary, feel free to modify as needed.

   ```python
   def get_config():
       """
       Returns a python dictionary object with the parsed config
       :return: dict - the parsed content of the file
       """
       return {
         "awss3bucket": {
           "name": "Form Submissions Archive",
           "bucket_name": "valid-bucket-name",
           "bucket_path": "valid/path/in/bucket"
           "aws_region_name": "region_name",
           "aws_access_key_id": "xxxxxxxxxxxxxxxxxxxxxxx",
           "aws_secret_access_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
         }
       }
   ```

   

2. You can assume this function will provide the payload as a python dictionary:

   ```python
   def get_payload():
       """
       Returns a python dictionary object with the parsed payload
       :return: dict - the parsed content of the file
       """
       return requests.get("https://raw.githubusercontent.com/cityofaustin/atd-integrations/master/sample.json").json()
   ```
   ** Please note that you are going to have to install the requests library for python: https://requests.readthedocs.io/en/master/

3. To report failures, you can assume you are going to use this function:

   ```python
   def report_error(message):
     	print(f"Error: {message}")
   ```

4. To report warnings, you can assume you are going to use this function:

   ```python
   def report_warning(message):
     	print(f"Warning: {message}")
   ```

# Tasks

1. Write a function called `write_google_sheet`. This function identifies each key against the header, and writes it's value in the proper order. Rewrite the function as needed, except for `write_google_sheet` or `client_secret, headers, payload`. 

  ```python
def write_s3_bucket(config, payload):
      """
      Updates the headers of a google sheet
      :param config: dict - the configuration as a python dictionary
      :param payload: dict - the entire payload as a python dictionary
      :return: bool - True if succeeds; otherwise False
      """
      return False
   ```
   
   Make sure that the file is saved to the correct bucket `bucket_name` and to the correct folder `bucket_path`
   
2. Write sample tests:

   1. A a couple tests that show how the payload is saved the correct s3 and folder
   3. Write a test that shows an error message being displayed for faulty configuration.

# Debugging

We prefer to use `web_pdb` as our debugger, but feel free to use any other debugger or tools you need to debug your code.

Web_pdb: https://github.com/romanvm/python-web-pdb