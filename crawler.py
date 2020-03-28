import json
from typing import List, Dict

import requests
from requests import Response
from bs4 import BeautifulSoup


def fetch(url: str) -> str:
    resp: Response = requests.get(url)
    return resp.text


def parse(text: str) -> List[Dict[str, str]]:
    html = BeautifulSoup(text, "html.parser")
    return [
        dict(
            zip(
                ("code", "name"),
                map(lambda el: el.text.strip(), tr.find_all("td")[1:3]),
            )
        )
        for tr in html.find_all("tr", {"height": "19"})
    ]


if __name__ == "__main__":
    with open("china_region_data/data.json", "w+") as file:
        json.dump(
            parse(
                fetch(
                    "http://www.mca.gov.cn/article/sj/xzqh/2019/2019/201912251506.html"
                )
            ),
            file,
            indent=4,
        )
