import logging
import requests
import math
import time
import header
from databass import *

def get_json(city,job,page):
    time.sleep(10)
    lagou_url = 'https://www.lagou.com/jobs/positionAjax.json'
    lagou_header = header.get_lagou_header(job)
    # 拼接在url的参数
    lagou_params = {
        "px": "new",
        "city": city,
        "needAddtionalResult": "false",
        "isSchoolJob": "0"
    }
    # post的参数
    lagou_data = {
        'first': 'true',
        'pn': page,
        'kd': job
    }
    try:
        res = requests.post(lagou_url, headers = lagou_header, data = lagou_data, params=lagou_params)
        res.raise_for_status()
        res.encoding = 'utf-8'
        data = res.json()
        return data
    except Exception as e:
        logging.error(e)

def get_total_page(city,job):
    data = get_json(city,job,1)
    try:
        count = data['content']['positionResult']['totalCount']
        res = math.ceil(count / 15)
        # 拉勾网最多显示30页结果
        if res > 30:
            return 30
        else:
            return res
    except KeyError:
        print(data)
        return 0

def get_position_id(city,job,page):
    data = get_json(city,job,page)
    ids = []
    try:
        result = data['content']['positionResult']['result']
        for i in result:
            ids.append(i['positionId'])
    except KeyError:
        print(data)
    return ids

def main():
    city = '深圳'
    job = 'PHP'
    total_page = 1
    total_page = get_total_page(city,job)
    print('页数:{}'.format(total_page))
    if total_page > 0:
        db = DBSession()
        for page in range(1, total_page+1):
            ids = [1, 2, 3, 4, 5]
            ids = get_position_id(city,job,page)
            for id in ids:
                db.add(positionIds(position_id=id, job=job, status=0))
            db.commit()
            print('已经抓取第{}页, 职位总数:{}'.format(page, len(ids)))
            print(ids)
        db.close()

if __name__== "__main__":
    main()