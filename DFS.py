from random import sample
from selenium import webdriver as wd
import time, re, pymysql, requests, random
import pandas as pd
from datetime import datetime, timedelta
# from seleniumrequests import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('__file__'))))

from db_info import db_info

def compute_density(nodes ,visited = []):
    TagNumber = 1
    CharNumber = 0
    TagName = ""
    Char_txt = ""
    if "childGenerator" in dir(nodes):
        for child in nodes.childGenerator():
            char_no_blank = nodes.text.replace(" ", "")
            CharNumber = len(char_no_blank)
            Char_txt = nodes.text
            TagNumber = len(nodes.find_all())
            TagName = nodes.name
            compute_density(child)
    else:
        if nodes.name == None:
            pass
        elif not nodes.isspace(): # Just to avoid \n
            char_no_blank = nodes.text.replace(" ", "")
            CharNumber = len(char_no_blank)
            Char_txt = nodes.text
            TagNumber = 0
            TagName = nodes.name
            pass
    if TagNumber == 0:
       TagNumber = 1
    Density = CharNumber / TagNumber
    visited.append([CharNumber ,TagNumber ,Density, TagName ,Char_txt])

    return visited

url = "https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=100&oid=015&aid=0004611313"
header = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36"}
req = requests.get(url, headers=header)

soup = BeautifulSoup(req.content, "html.parser")

for script in soup("script"):
    script.decompose()
for comment in soup("comment"):
    comment.decompose()
for style in soup("style"):
    style.decompose()

# "childGenerator" in dir(test[0])
# print(len(test[2].find_all()))


cd = compute_density(soup)
# len(cd)
# plt.plot(cd)
# plt.show()
bd = pd.DataFrame(cd,columns=["char",'tag','den','Tag_name','Char'])
plt.plot(bd['den'])
plt.show()

bd2 = bd.loc[(bd['den'] > 90)]
bd2





#############################


def dfs(graph, start, visited=[]):
    # 현재 노드를 방문처리
    visited.append(start) ## ★★★★★★★ 이해가 잘 안됨 우리예제에서는 start확인을 안해도 될지도?
    charnum = 0

    #visited 내용 [[tagname,charnum,tagnum,density],[a,b,c,d],---]
    for node in graph[start]:
        dfs_recursive(graph,node,visited)
    if N.TagNumver == 0
        N.TagNumber == 1
    density = nchar / ntag
    visited.append([tagnm,charnum,tagnum,density])
    return visited


    visited[n] = True
    print(n, end="")

    # 현재 노드와 인접한 노드를 확인
    for i in graph[n]:
        # 방문하지 않은 노드라면
        if not visited[n]:
            #재귀호출
            dfs(graph, i, visited)


############## dfs 사용
# 각 노드에 연결된 정보를 2차원 리스트로 표현
graph = [
    [],
    [2, 3, 8],  # 1번 노드와 인접한 노드 2,3,8
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보

visited = [False]*(8+1)
# dfs 호출
dfs(graph, 1, visited)