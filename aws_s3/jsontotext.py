import boto3
from botocore.exceptions import NoCredentialsError
import requests

#ACCESS_KEY = AWS_ACCESS_KEY_ID
#SECRET_KEY = AWS_SECRET_ACCESS_KEY

# Should be environment variables

class jsontotext:

  #def get_config(self):
    #"""
    #Returns a python dictionary object with the parsed config
    #:return: dict - the parsed content of the file
    #"""
    #return {
      #"awss3bucket": {
        #"name": "Form Submissions Archive",
       #"bucket_name": "valid-bucket-name",
       #"bucket_path": "valid/path/in/bucket",
      #  "aws_region_name": "region_name",
      #  "aws_access_key_id": "xxxxxxxxxxxxxxxxxxxxxxx",
      #  "aws_secret_access_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      #}
    #}

  #def get_payload(self):
    #r =  requests.get("https://raw.githubusercontent.com/cityofaustin/atd-integrations/master/sample.json").json()
    #return r

  def report_error(self, message):
  	print(f"Error: {message}")

  def report_warning(self, message):
  	print(f"Warning: {message}")

  #def get_json(self, location):
    #Original idea here was to grab the JSON and do the 
    #conversion with this function. 
    #As it stands it goes unused but might be used again at some point.
    
    #converted = "blah"
    #return converted

  def write_json_to_text(self, payload, txtfilename):
    #print("In write to json method")
    payloadTxt = payload
    text_file = open(txtfilename, "w")
    text_file.write(payloadTxt)
    text_file.close()
    #return False



#print("In main")
testClass = jsontotext
payload = requests.get("https://raw.githubusercontent.com/cityofaustin/atd-integrations/master/sample.json").json()
payload = str(payload)

print (payload)
filename = "testfile.txt"
testClass.write_json_to_text(testClass, payload, filename)
