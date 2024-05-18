import json

# x = '{"name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y["age"])
# y_stringfy = json.dumps(y)
# with open("week_7\\file.json", "w") as f:
#     json.dump(y_stringfy, f)

# x = {
#     "name": "John",
#     "age": 18,
#     "merried": True,
#     "children": ("Ann", "Mary"),
#     "pets": None,
#     "cars": [{"model": "BMW 20"}, {"model": "Ford"}],
# }

# y = json.load(x)
# print(y)


# content = ""
# with open("week_7\\test.json", "r", encoding="utf-8") as f:
#     content = json.load(f)
#     print(type(content))
#     print(content["data"][1]["lastName"])

from urllib import request

# resp = request.urlopen("https://en.wikipedia.org/wiki/Main_Page")
# print(resp)
# print(type(resp))

# data = resp.read()
# print(data)

# html = data.decode("utf-8")
# print(html)


content = request.urlopen("http://jsonblob.com/1226219489053237248")
data = content.read()
json_content = data.decode("utf-8")
print(type(json_content))
print(type(json.loads(json_content)))
