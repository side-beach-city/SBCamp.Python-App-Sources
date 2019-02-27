# coding: utf-8

import urllib.request
import json

# 天気予報取得クラス
class Weather:
  def __init__(self, data):
    self.date = data["date"]
    self.telop= data["telop"]
    if data["temperature"]["max"] is not None:
      self.temperature_max = "{0}℃".format(data["temperature"]["max"]["celsius"])
    else:
      self.temperature_max = "--"
    if data["temperature"]["min"] is not None:
      self.temperature_min = "{0}℃".format(data["temperature"]["min"]["celsius"])
    else:
      self.temperature_min = "--"

  def print(self):
    print(self.date)
    print("  " + self.telop)
    print("  最低気温:{0}".format(self.temperature_min))
    print("  最高気温:{0}".format(self.temperature_max))

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
    item.print()
