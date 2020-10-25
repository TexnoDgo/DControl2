import requests

file_name = "Hi!"

url = "http://127.0.0.1:8000/project/upload"

file_path = "C:/PP/DControl2/DC2Api/TESTFOLDER/plus.png"

file2 = open(file_path)

print(file2.read(5))

files = {'file': (open(file_path, 'rb'), 'multipart/form-data'), 'title': "kek"}
print(files)


r = requests.post(url, files=files)

print(r.status_code)
print(r.text)
