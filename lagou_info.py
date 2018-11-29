import json
import re

import requests
import header
from bs4 import BeautifulSoup
import pandas
import time
import logging

def get_html(id,job):
    time.sleep(10)
    lagou_url = 'https://www.lagou.com/jobs/'+str(id)+'.html'
    lagou_header = header.get_lagou_header(job)
    html = requests.get(lagou_url, headers = lagou_header)
    return html.text

def parse_html(html):
    try:
        info = []
        html = BeautifulSoup(html,'html.parser')
        salary = html.select('.job_request .salary')[0].get_text()
        city = html.select('.job_request p')[0].find_all('span')[1].get_text()
        workYear = html.select('.job_request p')[0].find_all('span')[2].get_text()
        education = html.select('.job_request p')[0].find_all('span')[3].get_text()
        jobNature = html.select('.job_request p')[0].find_all('span')[4].get_text()
        jobDemandObj = html.select('.job_bt div')[0].find_all('p')
        print(len(jobDemandObj))
        jobDemand = []
        flag = False
        for obj in jobDemandObj:
            jobTxt = obj.get_text()
            jobTxt = re.sub('\s', '', jobTxt)
            if not jobTxt:
                continue
            if flag:
                match = re.match("([0-9]+|-)\s*[\.:：、]?\s*", jobTxt)
                if match:
                    jobTxt = jobTxt[match.end():]
                    jobTxtArr = jobTxt.split('；')
                    for txt in jobTxtArr:
                        subMatch = re.match("([0-9]+|-)\s*[\.:：、]?\s*", txt)
                        if subMatch:
                            print(txt[subMatch.end():])
                            jobDemand.append(txt[subMatch.end():])
                        else:
                            print(txt)
                            jobDemand.append(txt)
                else:
                    break
            elif re.match("\w?[\.、 :：]?(任职要求|任职资格|我们希望你|任职条件|岗位要求|要求：|职位要求|工作要求|职位需求)", jobTxt):
                flag = True
        jobDemand = json.dumps(jobDemand)
        industryField = html.select('.c_feature')[0].find_all('li')[0].get_text()
        financeStage = html.select('.c_feature')[0].find_all('li')[1].get_text()
        companySize = html.select('.c_feature')[0].find_all('li')[2].get_text()
        info.append(salary)
        info.append(city)
        info.append(workYear)
        info.append(education)
        info.append(jobNature)
        info.append(jobDemand)
        info.append(industryField)
        info.append(financeStage)
        info.append(companySize)
        return info
    except Exception as e:
        print(html)
        logging.error(e)

def main():
    data = []
    job = 'PHP'
    ids = [5185557,5227356]
    for id in ids:
        print(id)
        html = get_html(id,job)
        info = parse_html(html)
        data.append(info)
    # df = pandas.DataFrame(data = data,columns = ['薪资','城市','工作经验','学历要求','工作类型','职位要求','工作领域','发展阶段','公司规模'])
    # df.to_csv('lagou_jobs.csv',index = False)
    print('已保存为csv文件.')

if __name__== "__main__":
    main()


