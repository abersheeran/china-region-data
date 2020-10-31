import json
import re
from typing import List, Dict

import requests
from requests import Response
from bs4 import BeautifulSoup


def fetch(url: str) -> str:
    resp: Response = requests.get(url)
    return resp.text


def parse(text: str) -> Dict[str, str]:
    html = BeautifulSoup(text, "html.parser")
    table = [
        [td.text.strip() for td in tr.find_all("td")] for tr in html.find_all("tr")
    ]
    # 通过查询 '110000' 与 '北京市' 两个数据进行定位
    for tr_i, tr in enumerate(table):
        for td_i, td in enumerate(tr):
            if td == "110000":
                code_index = td_i
            elif td == "北京市":
                name_index = td_i

    return {
        tr[code_index]: tr[name_index]
        for tr in table
        if code_index < len(tr) and re.match(r"^\d{6}", tr[code_index])
    }


if __name__ == "__main__":
    data: Dict[str, str] = {}

    for link in (
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708040959.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041004.html",
        "http://www.mca.gov.cn/article/sj/xzqh/1980/1980/201911180942.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708160821.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220856.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220858.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220859.html",
        "http://www.mca.gov.cn/article/sj/xzqh/1980/1980/201911180950.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220903.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041017.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041018.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041020.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220910.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041023.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220911.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220913.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220914.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220916.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220918.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220921.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220923.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220925.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220927.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220928.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220930.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220935.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220936.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220939.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220941.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220943.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220946.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201707271552.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201707271556.html",
        "http://files2.mca.gov.cn/cws/201404/20140404125552372.htm",
        "http://files2.mca.gov.cn/cws/201502/20150225163817214.html",
        "http://www.mca.gov.cn/article/sj/tjbz/a/2015/201706011127.html",
        "http://www.mca.gov.cn/article/sj/xzqh/1980/201705/201705311652.html",
        "http://www.mca.gov.cn/article/sj/xzqh/1980/201803/201803131454.html",
        "http://www.mca.gov.cn/article/sj/xzqh/1980/201903/201903011447.html",
        "http://www.mca.gov.cn/article/sj/xzqh/1980/2019/202002281436.html",
        # 以下为 2020 年各个月份的发布链接
        "http://www.mca.gov.cn/article/sj/xzqh/2020/2020/202003061536.html",
        "http://www.mca.gov.cn/article/sj/xzqh/2020/2020/202003301019.html",
        "http://www.mca.gov.cn///article/sj/xzqh/2020/2020/202007170301.html",
        "http://www.mca.gov.cn///article/sj/xzqh/2020/2020/2020072804001.html",
        "http://www.mca.gov.cn///article/sj/xzqh/2020/2020/2020072805001.html",
        "http://www.mca.gov.cn//article/sj/xzqh/2020/202006/202008310601.shtml",
        "http://www.mca.gov.cn//article/sj/xzqh/2020/2020/20200908007001.html",
        "http://www.mca.gov.cn//article/sj/xzqh/2020/2020/2020092500801.html",
    ):
        print("Fetching:", link)
        new_data = parse(fetch(link))
        data.update(new_data)

    with open("china_region_data/data.json", "w+", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False)
