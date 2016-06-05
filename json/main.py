# coding: utf-8
import json

import json

JSON_TXT = '''{
    "request": {
        "deadline": "2017-04-29 09:02:00",
        "title": "李方证你个傻逼",
        "description": "",
        "reminded": true,
        "type": "3",
        "scheduleId": 0
    },
    "token": "e3861d62-37c3-4fcd-961c-9058c2941259"
}'''
JSON_TXT2 = '''{
    "request": {
        "deadline": "2017-01-02 15:04:05",
        "title": "大傻子张亚兵",
        "description": "",
        "type": "",
        "reminded": false,
        "schoolId": 0 
    },
    "token": "e19568e5-9e8e-4ae6-b1f3-84d63a0f5b10"
}'''

JSON = json.loads(JSON_TXT)
JSON2 = json.loads(JSON_TXT2)

re = json.one(JSON)
re2 = json.one(JSON2)


print re
print re2
