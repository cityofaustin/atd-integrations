# Security Note

**IMPORTANT: Do not push code with passwords, access keys, api tokens or any other sensitive information.**

# Knack Integration (Effort Level: Medium)

### Purpose

We need an integration that can take a key-value json document and inserts the values into a Knack application using the knackpy library.

Examples:
https://github.com/cityofaustin/knackpy

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
    "knack": {
        "name": "Knack Application",
        "object_id": "object_1",
        "app_id": "abc123",
        "api_key": "topsecretapikey",
        "field_map": {
            "company": "field_1",
            "first_name": "field_5",
            "last_name": "field_11",
            "email_address": "field_21",
            "title": "field_19",
            "phone": "field_7",
            "registered": "field_110",
            "registration_date": "field_100",
            "age": "field_99",
            "attachments": "field_2"
        }
    }
}
```

## Notes

You can assume the field map will always be provided.

Also, notice that the field numbers do not come in order or sequence, this is because in Knack the field number varies by the time of creation, meaning that as fields get deleted and are created, sequence gaps will be an ocurrance.

Feel free to change the configuration schema as needed.