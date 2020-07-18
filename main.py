# coding: utf-8

import urllib.request
import json
import pprint

# 天気予報取得クラス
class Weather(object):
  def __init__(self, data):
    self.date = data["date"]
    self.telop= data["telop"]
    self.temperature_max = None
    self.temperature_min = None
    if data["temperature"]["max"] is not None:
      self.temperature_max = data["temperature"]["max"]["celsius"]
    if data["temperature"]["min"] is not None:
      self.temperature_min = data["temperature"]["min"]["celsius"]

  def print(self):
    print(self.date)
    print("  " + self.telop)
    if self.temperature_max is not None:
      print("  最高気温：{0}".format(self.temperature_max))
    if self.temperature_min is not None:
      print("  最低気温：{0}".format(self.temperature_min))

# 初期処理
url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=140010"
# URL取得
req = urllib.request.Request(url)
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
