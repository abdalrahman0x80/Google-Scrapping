import requests
import json
i = input("Search on : ")
r = requests.get(f"https://www.google.com/complete/search?q={i}&cp=7&client=gws-wiz&xssi=t&gs_pcrt=undefined&hl=en-EG&authuser=0&psi=KhUAZ7rXBfackdUPjJzfqAs.1728058662402&dpr=1")
for jsoner in json.loads(r.text[4:])[0]:
    print("result: ",jsoner[0])
