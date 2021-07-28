import threading
import requests
import time

def kupon_request():
    global toplam_req
    x = requests.get("http://127.0.0.1:8000/kupon_kullan", verify=False)
    print(x.text)
    toplam_req += 1

toplam_req = 0
num = 500
for i in range(num):
    threading.Thread(target=kupon_request).start()

time.sleep(2)
print(str(toplam_req))

