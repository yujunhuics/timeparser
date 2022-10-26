# timeparser
**文本时间抽取、解析、标准化工具**

### 安装方式

```shell
cd timeparser
python setup.py install
```

### 使用实例

```python
import timeparser as tp
import json

text = '''今年5月和6月腾讯和阿里的股票走势'''
res = tp.extract_time(text)
```

### 输出

```json
[
  {
    "text":"今年5月",
    "offset":[
      0,
      4
    ],
    "type":"time_span",
    "detail":{
      "type":"time_span",
      "definition":"accurate",
      "time":[
        "2022-05-01 00:00:00",
        "2022-05-31 23:59:59"
      ]
    }
  },
  {
    "text":"6月",
    "offset":[
      5,
      7
    ],
    "type":"time_point",
    "detail":{
      "type":"time_point",
      "definition":"accurate",
      "time":[
        "2022-06-01 00:00:00",
        "2022-06-30 23:59:59"
      ]
    }
  }
]

```

