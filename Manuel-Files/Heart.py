import http.client
import json
import re

headers = {'Host': 'live.radiance.thatgamecompany.com', 'User-Agent': 'Sky-Live-com.tgc.sky.android/0.13.3.165938 ('
                                                                      'Xiaomi MI 9; android 29.0.0; es)',
           'X-Session-ID': '3fcdb056-bed1-413d-aa89-ef15c829429a', 'Content-type': 'application/json'}
headers2 = {'Host': 'live.radiance.thatgamecompany.com', 'User-Agent': 'Sky-Live-com.tgc.sky.android/0.13.3.165938 ('
                                                                       'Xiaomi MI 9; android 29.0.0; es)',
            'X-Session-ID': '3fcdb056-bed1-413d-aa89-ef15c829429a', 'Content-type': 'application/json',
            'x-sky-install-source': 'com.google.android.packageinstaller'}
headers3 = {'Host': 'live.radiance.thatgamecompany.com', 'User-Agent': 'Sky-Live-com.tgc.sky.android/0.13.3.165938 ('
                                                                       'Xiaomi MI 9; android 29.0.0; es)',
            'X-Session-ID': '3fcdb056-bed1-413d-aa89-ef15c829429a', 'Content-type': 'application/json'}


def darlike(aut, fed, str1, str2):
    connec = http.client.HTTPSConnection('live.radiance.thatgamecompany.com')
    food = {
        "user": f"{str1}",
        "session": f"{str2}",
        "social_feed_id": f"{fed}",
        "author_id": f"{aut}",
        "liked": True
    }
    json_fo = json.dumps(food)
    connec.request('POST', '/account/social_feed/like', json_fo, headers3)
    responses = connec.getresponse()
    lines = responses.read().decode()
    print(lines)


conn = http.client.HTTPSConnection('live.radiance.thatgamecompany.com')
user = input('Ingrese el user\n')
user = '2e53a223-e2a9-4154-9e98-4e37e3ee38bb'
user = '3e783482-16a4-4165-b5e3-e17a01446f23'

sesion = input('Ingrese la sesion\n')
sesion = 'df3b47a4138d91798dad5c28e58636ff'
foo = {
    "user": f"{user}",
    "session": f"{sesion}",
    "pool_type": "MessageBoat",
    "pool_name": "CandleSpace",
    "message": "Loves",
    "extra_data": {
        "pos": "(14.378,0.000,-10.999)",
        "ori": "(0.000,0.644,0.000,0.765)",
        "scale": "(1.000,1.000,1.000)"
            }
        }
json_foo = json.dumps(foo)
conn.request('POST', '/account/social_feed/create', json_foo, headers)
response = conn.getresponse()
lin = response.read().decode()
print(lin)
socialfeed = re.search(r'(?<="social_feed_id":")[^"]*', lin).group()
print('Social feed obtenido :', socialfeed)
foo2 = {
    "type": "Local",
    "production": True,
    "tos_version": 4,
    "request_recovery_token": True,
    "hashes": [
        3858080788,
        3523589696,
        1911891653,
        209563627,
        2031507605,
        1246829562,
        2921836582,
        3062676827,
        2766223387,
        1121283940,
        1362183894,
        3585622646,
        3437882660,
        2771038325,
        3661381049,
        4158861284,
        140952443,
        2750508191
    ],
    "integrity": True
}
json_foo2 = json.dumps(foo2)
x = int(input('Ingrese numero de likes\n'))
conn2 = http.client.HTTPSConnection('live.radiance.thatgamecompany.com')
for i in range(1, x + 1):
    conn2.request('POST', '/account/auth/create', json_foo2, headers2)
    response = conn2.getresponse()
    line = response.read().decode()
    usere = re.search(r'(?<="user":")[^"]*', line).group()
    sesiones = re.search(r'(?<="session":")[^"]*', line).group()
    print(usere)
    print(sesiones)
    darlike(user, socialfeed, usere, sesiones)

conn3 = http.client.HTTPSConnection('live.radiance.thatgamecompany.com')
like = {
  "user": f"{user}",
  "session": f"{sesion}",
  "social_feed_id": f"{socialfeed}",
  "author_id": f"{user}"
}
json_like = json.dumps(like)
conn3.request('POST', '/account/social_feed/get_reactions', json_like, headers3)
response = conn3.getresponse()
print(response.read().decode())
