### 例子

运行main.py
```python
# coding: utf-8
import oneJson
import json

JSON_TXT = '''{"name":"ljun", "version": 1.0, "data": [{"title": "test"},{"title": "test"}], "none": null}'''
JSON_TXT2 = '''{"name":"dc", "version": 2.0, "data": [{"title": "test"},{"title": "test", "info":"equal json"}], "none": null}'''

JSON = json.loads(JSON_TXT)
JSON2 = json.loads(JSON_TXT2)

re = oneJson.one(JSON)
re2 = oneJson.one(JSON2)


print re
print re2
```

结果
```json
{"none": "null", "version": "number", "data": [{"title": "string"}], "name": "string"}
```
```json
{"none": "null", "version": "number", "data": [{"info": "string", "title": "string"}, {"title": "string"}], "name": "string"}
```

## 安装方法
在当前目录打开 terminal 运行
```shell
python setup.py install
```