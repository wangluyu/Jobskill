import uuid
import requests
import time
from fake_useragent import UserAgent

ua_type = 'random'

def get_uuid():
    return str(uuid.uuid4())

def get_lagou_header(job):
    cookie = "JSESSIONID=" + get_uuid() + ";" \
    "user_trace_token=" + get_uuid() + "; LGUID=" + get_uuid() + "; index_location_city=%E6%88%90%E9%83%BD; " \
    "SEARCH_ID=" + get_uuid() + '; _gid=GA1.2.717841549.1514043316; ' \
    '_ga=GA1.2.952298646.1514043316; ' \
    'LGSID=' + get_uuid() + "; " \
    "LGRID=" + get_uuid() + "; "
    ua = UserAgent(verify_ssl=False)
    ua = getattr(ua, ua_type)
    headers = {
        'cookie': cookie,
        'origin': "https://www.lagou.com",
        'x-anit-forge-code': "0",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'user-agent': ua,
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'accept': "application/json, text/javascript, */*; q=0.01",
        'referer': "https://www.lagou.com/jobs/list_PHP?px=default&city=%E6%B7%B1%E5%9C%B3",
        'x-requested-with': "XMLHttpRequest",
        'connection': "keep-alive",
        'x-anit-forge-token': "None",
        'cache-control': "no-cache"
    }
    return headers