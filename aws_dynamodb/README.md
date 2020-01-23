# Security Note

**IMPORTANT: Do not push code with passwords, access keys, api tokens or any other sensitive information.**

# AWS DynamoDB Integration (Effort Level: Medium)

### Purpose

We need an integration that can take a key-value json document and inserts the values into an AWS DynamoDB database.

Example Article:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html

Sample Payload:

```json
{
	"company": "City of Austin",
	"first_name": "John",
	"last_name": "Doe",
	"email_address": "john.doe@example.com",
	"title": "developer",
	"phone": "(801)123-4567",
	"registered": true,
	"registration_date": "01/20/2020",
	"age": 28,
	"attachments": [
		"http://s3.amazonaws.com/bucket-name-here/file1.png",
		"http://s3.amazonaws.com/bucket-name-here/file2.png"
	]
}
```


Sample Configuration:

```json
{
	"aws_dynamodb": {
        "name": "DynamoDB Configuration",
		"table_name": "valid-table-name",
        "api_endpoint": "http://sample.dynamodb.com/endpoint",
        "aws_region_name": "region_name",
		"aws_access_key_id": "xxxxxxxxxxxxxxxxxxxxxxx",
        "aws_secret_access_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	}
}
```

You may use the json payload and the sample configuration any way you need to.