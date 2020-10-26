import http.client
import mimetypes
conn = http.client.HTTPSConnection("127.0.0.1", 8000)
payload = "C:/Users/User/Desktop/МК2.02.02.02.001 Втулка.PDF"
headers = {
  'title': 'kekker',
  'Content-Type': 'image/jpeg'
}
conn.request("PUT", 'http://127.0.0.1:8000/project/upload/МК2.02.02.02.001 Втулка.PDF', payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))