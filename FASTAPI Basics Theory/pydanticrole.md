What is Pydantic's role in FastAPI.?



1\. Data validation:

It checks the data coming from:

* Body (JSON)
* Query parameters
* Path parameters

FastAPI uses Pydantic to make sure the data is correct type, format, and structure.



Example:

If you expect price: float and the user sends a string, Pydantic will automatically give an error.



2\. Data parsing:

Pydantic converts data into proper Python types.



Example:

If "10" (string) is received, Pydantic converts it to 10 (integer).



3\. Request body models:

You create Pydantic models using BaseModel to define the structure of the input data.



4\. Response models

FastAPI can send responses in a controlled format using Pydantic.



Example: only return selected fields or rename fields.



5\. Automatic documentation

Because of Pydantic models, FastAPI automatically generates:

* JSON schema
* Example structure
* API docs at /docs
