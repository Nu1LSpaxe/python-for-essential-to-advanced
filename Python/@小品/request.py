import requests

response = requests.get('https://data.epa.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON')

data = response.json()['records']

for i in range(len(data)):
    data[i]['pm25'] = 0 if not data[i]['pm25'] else int(data[i]['pm25'])
data = sorted(data, key=lambda d: d['pm25'], reverse=True)

[print(i) for i in data[:5]]