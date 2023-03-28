import requests
import base64

filename = "C:\\Users\\Fatihi\\Desktop\\python\\snippets\\pand_as.py"
with open(filename, "r") as f:
    file_content = f.read()

# Encode the file content as base64
encoded_content = base64.b64encode(
    file_content.encode('utf-8')).decode('utf-8')

print(encoded_content)

# Set up the necessary information for the API request
repo_url = "https://api.github.com/repos/ZakWrench/Python_Unbounded/contents/random_python_snippets/pand_as.py"
commit_msg = "Added a new code snippet for working with Pandas"
file_content = encoded_content

# Encode the file content as base64
encoded_content = base64.b64encode(
    file_content.encode('utf-8')).decode('utf-8')

token = "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"
# Make the API request to create a new file with the given content
response = requests.put(repo_url, headers={"Authorization": f"token {token}"}, json={
    "message": commit_msg,
    "content": encoded_content,
})

# Print the response from the API
print(response.json())

# DECODE BASE64
'''
import requests
import base64

filename = "C:\\Users\\Fatihi\\Desktop\\python\\snippets\\pand_as.py"
with open(filename, "r") as f:
    file_content = f.read()

# Encode the file content as base64
encoded_content = base64.b64encode(
    file_content.encode('utf-8')).decode('utf-8')

print(encoded_content)

# Set up the necessary information for the API request
repo_url = "https://api.github.com/repos/ZakWrench/Python_Unbounded/contents/random_python_snippets/pand_as.py"
commit_msg = "Added a new code snippet for working with Pandas"
file_content = encoded_content

# Encode the file content as base64
encoded_content = base64.b64encode(
    file_content.encode('utf-8')).decode('utf-8')

token = "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"
# Make the API request to create a new file with the given content
response = requests.put(repo_url, headers={"Authorization": f"token {token}"}, json={
    "message": commit_msg,
    "content": encoded_content,
})

# Print the response from the API
print(response.json())

'''
