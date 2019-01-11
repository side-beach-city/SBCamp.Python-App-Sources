# coding: utf-8

import urllib.request
import json

# 天気予報取得クラス
class Weather:
  def __init__(self, data):
    self.date = data["date"]
    self.telop= data["telop"]
    self.temperature_max = None
    self.temperature_min = None
    if data["temperature"]["max"] is not None:
      self.temperature_max = data["temperature"]["max"]["celsius"]
    if data["temperature"]["min"] is not None:
      self.temperature_min = data["temperature"]["min"]["celsius"]

# 初期処理
id = 140010
url = "http://weather.livedoor.com/forecast/webservice/json/v1?city={0}"
# URL取得
req = urllib.request.Request(url.format(id))
with urllib.request.urlopen(req) as res:
  data = json.load(res)
  # 処理
  print(data["title"])
  weathers = []
  for forecast in data["forecasts"]:
    weathers.append(Weather(forecast))
  # 表示
  for item in weathers:
    print(item.date)
    print("  " + item.telop)
    if item.temperature_min is not None:
      print("  最低気温:{0}".format(item.temperature_min)) 
    if item.temperature_max is not None:
      print("  最高気温:{0}".format(item.temperature_max))
