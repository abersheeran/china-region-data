# 中国行政区域数据

根据[中华人民共和国民政部](http://www.mca.gov.cn/article/sj/xzqh/)中的数据处理而成。

由于时间跨度过长（从 1980 年至今），故而部分地区的名称或行政级别已经发生改变，本仓库的存储原则为“编码唯一，以新换旧”。即同一个行政编码，认定为同一个地区，地区名称以民政部门最新公开的行政区域划分数据中的名称为准。且，为保持向前兼容，一些过去存在但后来去除的行政区域编码，本仓库仍然保留，以方便一些古旧的数据能正常使用。

## 安装

```bash
pip install china-region-data
```

## 样例

```python
from china_region_data import Region


广东 = Region("广东省")
深圳 = Region("广东省深圳市")
南山 = Region("广东省深圳市南山区")
assert 广东.name == "广东省"
assert 广东.level == 1

for 广东城市 in 广东.subordinate:
    assert 广东城市.level == 2

assert 深圳.superior == 广东
assert 南山.superior.superior == 广东
assert 南山 in 南山.superior
assert 南山 in 南山.superior.superior

北京 = Region("110000")
assert 北京.name == 北京.fullname == "北京市"
assert 北京 not in 广东
```
