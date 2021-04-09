from typing import Optional
import requests
import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
import urllib
import urllib.parse
import json
import sys
import os
import platform
from googletrans import Translator

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
url="http://127.0.0.1:5700/send_group_msg"
version="1.0"

app = FastAPI()

class GroupItem(BaseModel):
    message: str
    group_id: int
class FriendMessage(BaseModel):
    message: str
    friend_id: int
translator = Translator(service_urls=['translate.google.cn']) #将翻译服务URL替换为国内区域名
lang = ['de','en','ja','da','fr','ny','uk','gl','ht','es','zh-cn'] #翻译次数及语言
@app.post("/")
async def create_item(item: dict):
    msg1=item.get("message")
    group=item.get("group_id")
    if msg1 and (msg1.startswith("生草")):
        print("收到了请求。")
        juzi = msg1[2:]
        count = 0
        for mubiao in lang:
            count = count + 1 #翻译计次
            juzi = translator.translate(juzi,dest=mubiao).text
            print(str(count)+"次翻译结果："+juzi)
        print("最终翻译结果："+juzi)
        requests.post(url,json={"group_id":group,"message":"翻译结果："+juzi})
        print("完成了请求。")
        del juzi
    if msg1=="ver":
        requests.post(url,json={"group_id":group,"message":"GoogleGM_qqbot（https://github.com/Asankilp/Google-Grass-Machine） ver"+version+"\n本机器人基于uvicorn及go-cqhttp（github.com/Mrs4s/go-cqhttp）。Google Translate核心模块为googletrans（https://pypi.org/project/googletrans/）。\n运行环境：\nPython "+sys.version+"\n操作系统：\n"+platform.platform()+" "+platform.version()})
    if msg1=="目力":
        requests.post(url,json={"group_id":group,"message":"[CQ:record,file=https://asankilp.github.io/muli.mp3]"})
    return {}

