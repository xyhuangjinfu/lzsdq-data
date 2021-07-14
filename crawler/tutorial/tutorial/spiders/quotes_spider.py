import re
import scrapy

HEADERS = {
    "authority": "www.kepuchina.cn",
    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    "sec-ch-ua-mobile": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-dest": "document",
    "referer": "https://www.kepuchina.cn/",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": "Hm_lvt_9535c3ea6eb286566c2c14dc19269572=1621929364,1622458550,1624427248; Hm_lpvt_9535c3ea6eb286566c2c14dc19269572=1624427922; cc_7_visited_site_username=2",
}


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.kepuchina.cn/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        u = response.url
        if u.endswith("/"):
            u = u[:len(u) - 1]
        u = u.replace("http://", "")
        u = u.replace("https://", "")
        seg = u.split("/")
        filename = "-".join(seg)
        filename = f'./pages/{filename}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        page_urls = self._get_urls(response.body.decode("utf-8"))
        for u in page_urls:
            next_page = response.urljoin(u)
            yield scrapy.Request(next_page, self.parse, headers=HEADERS)

        # for i in range(1,3):
        #     next_page = response.urljoin("https://www.kepuchina.cn/zykp/")
        #     yield scrapy.Request(next_page, self.parse)

    def _get_urls(self, content):
        pattern_href = re.compile("href=\"(.+?)\"")
        urls = re.findall(pattern_href, content)
        page_urls = []
        for u in urls:
            if not u.startswith("http"):
                continue
            if u.endswith("css") or u.endswith("js"):
                continue
            page_urls.append(u)
        return page_urls