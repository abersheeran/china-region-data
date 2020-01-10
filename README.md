# 中国行政区域数据

根据[中国政府网站](http://www.mca.gov.cn/article/sj/xzqh/2019/2019/201912251506.html)中的数据处理而成。

## install

```bash
pip3 install china-region-data
```

## example

```python
from china_region_data import 省级行政区域, 市级行政区域, 县级行政区域, Region


for 省级行政地区 in 省级行政区域:
    print(省级行政地区)
    for 市级行政地区 in 省级行政地区.下级行政区域:
        print("  ", 市级行政地区)
        for 县级行政地区 in 市级行政地区.下级行政区域:
            print("    ", 县级行政地区)

北京 = Region("110000")
assert 北京 == Region("北京市")

广东 = Region("广东省")
深圳 = Region("深圳市")
南山 = Region("南山区")

assert 广东.name == "广东省"
assert 广东.fullname == "广东省"
assert 深圳.fullname == "广东省深圳市"
assert 南山.fullname == "广东省深圳市南山区"

assert 广东.行政级别 == 1

for 广东城市 in 广东.下级行政区域:
    assert 广东城市.行政级别 == 2

assert 深圳.上级行政地区 == 广东

assert 南山.上级行政地区.上级行政地区 == 广东

assert 南山 in 南山.上级行政地区

assert 南山 in 南山.上级行政地区.上级行政地区

assert not Region("合肥市") in 广东
```
