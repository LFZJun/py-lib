####作用
解析html中的table
返回对应视觉图的阵列，阵列中的每个节点包含三个属性`text,col,row`分别表示td的`文本内容,列位置，行位置`

#### 例子
运行main.py

```python
# !/bin/python3
# coding: utf-8
from lhtml.table import parse


html = '''<html>
<body>

<table width="100%" border="1">
    <tr>
        <td rowspan="2">one</td>
        <td>two</td>
        <td>three</td>
    </tr>
    <tr>
        <td colspan="2">February</td>
    </tr>
</table>

</body>
</html>'''

table = parse(html)
for i in table:
    print(i)
```

结果
```python3
[{"row": 0, "col":  0, "text": one, "rowspan": 2, "colspan": 1}, {"row": 0, "col":  1, "text": two, "rowspan": 1, "colspan": 1}, {"row": 0, "col":  2, "text": three, "rowspan": 1, "colspan": 1}]
[{"row": 1, "col":  0, "text": one, "rowspan": 1, "colspan": 1}, {"row": 1, "col":  1, "text": February, "rowspan": 1, "colspan": 2}, {"row": 1, "col":  2, "text": February, "rowspan": 1, "colspan": 1}]
```
在当前目录打开 terminal 运行

```shell
pip3 install .
```
