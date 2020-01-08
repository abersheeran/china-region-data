# 中国行政区域数据

根据[中国政府网站](http://www.mca.gov.cn/article/sj/xzqh/2019/2019/201912251506.html)中的数据处理而成。

## install

```bash
pip3 install china-region-data
```

## example

```python
from china_region_data import 省级行政区域, 市级行政区域, 县级行政区域


for 省级行政地区 in 省级行政区域:
    print(省级行政地区)
    for 市级行政地区 in 省级行政地区.下级行政区域:
        print("  ", 市级行政地区)
        for 县级行政地区 in 市级行政地区.下级行政区域:
            print("    ", 县级行政地区)
```
