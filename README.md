# 中国行政区域数据

根据[中国政府网站](http://www.mca.gov.cn/article/sj/xzqh/2019/2019/201912251506.html)中的数据处理而成。

## install

```bash
pip3 install china-region-data
```

## example

```python
from china_region_data import provinces, cities, counties, Region


广东 = Region("广东省")
深圳 = Region("深圳市")
南山 = Region("南山区")
assert 广东.name == "广东省"
assert 广东.level == 1

for 广东城市 in 广东.subordinate:
    assert 广东城市.level == 2

assert 深圳.superior == 广东
assert 南山.superior.superior == 广东
assert 南山 in 南山.superior
assert 南山 in 南山.superior.superior
assert not Region("合肥市") in 广东
```
