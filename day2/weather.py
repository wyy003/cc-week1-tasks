import sys
import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    print("错误: 请设置环境变量 OPENWEATHER_API_KEY")
    print("示例: export OPENWEATHER_API_KEY=your_api_key_here")
    sys.exit(1)

if len(sys.argv) < 2:
    print("用法：python weather.py 城市名")
    sys.exit(1)

city = sys.argv[1]
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=zh_cn"

try:
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        print(f"\n城市：{data['name']}")
        print(f"温度：{data['main']['temp']}°C")
        print(f"天气：{data['weather'][0]['description']}")
        print(f"湿度：{data['main']['humidity']}%\n")
    elif response.status_code == 404:
        print("找不到该城市，请检查城市名")
    else:
        print(f"查询失败：{data.get('message', '未知错误')}")
except Exception as e:
    print(f"请求出错：{e}")
