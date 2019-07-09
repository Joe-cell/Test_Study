# -*- coding: utf-8 -*-
"""
@author: Joe_xu
@time: 2019/7/9 19:17
"""
import requests


class TiebaSpider(object):
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = 'https://tieba.baidu.com/f?kw=' + tieba_name + '&ie=utf-8&pn={}'
        self.hearders = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}

    def get_url_list(self):
        # url_list = list()
        # for i in range(10):
        #     url_list.append(self.url_temp.format(i * 50))
        # return url_list
        return [self.url_temp.format(i*50) for i in range(10)]

    def parse_url(self, url):
        print(url)
        response = requests.get(url=url, headers=self.hearders)
        return response.content.decode()

    def save_html(self, html_str, page_num):
        file_path = "{}第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        # 构造URL列表
        url_list = self.get_url_list()
        # 遍历、发送请求、获取相应
        for url in url_list:
            html_str = self.parse_url(url=url)
            # 保存
            page_num = url_list.index(url)
            self.save_html(html_str, page_num)


if __name__ == "__main__":
    tieba_spider = TiebaSpider("李毅")
    tieba_spider.run()
