import logging
import requests
import random
import time
import os
import subprocess
try:
    os.remove("COSE.log")
except:
    pass
def cmd_test():
    print("main2")
    os.system("start cmd /K \"go-cqhttp.exe\" -faststart")
    print("main2")


print("main")
cmd_test()
time.sleep(10)
jsx=0
jsxz=0
c1=0
c2=0
#[CQ:image,file=1bb7511e67be9e1799447c7d6b0eb38e.image,subType=1,url=https://gchat.qpic.cn/gchatpic_new/3072659646/715792440-3066821844-1BB7511E67BE9E1799447C7D6B0EB38E/0?term=2&amp;is_origin=0]
logging.basicConfig(filename='COSE.log', level=logging.DEBUG)
logging.info('import ok!')
print('''
-----------------------------
| 0000   0000   00000   00000
|0      0      0     0  0
|0       0000  0     0  00000
|0           0 0     0  0
| 0000   0000   00000   00000
-----------------------------
''')
#547274764
#import os -updata 1.0.3
grty=""
inp=False
entries = os.listdir('.')
for i in entries:
    if i == "grt.txt":
        with open('grt.txt', 'r') as f:
            grty = f.read()
            grty = eval(grty)
            grt = grty['QQ']
            inp = True
            print("QQ群号文件读取成功!")
if inp == False:
    grt = input("群号输入>>")
    with open('grt.txt', 'w') as f:
        f.write("{\"QQ\":\""+grt+"\"}")
else:
    pass
print("验证成功!")
#传输类型 POST 127.0.0.1:5700/终结点?参数名=参数值&参数名=参数值......
'''
import requests
data = {"name": "Bing", "message": "Hello"}
response = requests.post("https://example.com/api", data=data)
print(response.text)
'''
#updata 1.0.2-"CSOERotTest-日志写入成功 服务启动by小凉[CQ:image,file=1bb7511e67be9e1799447c7d6b0eb38e.image,subType=1,url=https://gchat.qpic.cn/gchatpic_new/3072659646/715792440-3066821844-1BB7511E67BE9E1799447C7D6B0EB38E/0?term=2&amp;is_origin=0]"
#CSOE updata -requests updata pos.
#import requests -updata 1.0.2 beta!
def fs(message,group_id):
    #updata 1.0.2-add def:fs!
    data = {"group_id": group_id, "message": message}
    #需要http,否则不认
    response = requests.post("http://127.0.0.1:5700/send_group_msg", data=data)
    return response
if inp == True:
    fs("成功通过QQ群文件登录!",grt)
else:
    fs("成功通过手动获取QQ群号登录!",grt)
def qc(jt,data):
    response = requests.post("http://127.0.0.1:5700"+jt, data=data)
    return response
fs(qc("/get_version_info",{}),grt)
logging.debug(fs("CSOERotTest-日志写入成功 服务启动by小凉[CQ:image,file=1bb7511e67be9e1799447c7d6b0eb38e.image,subType=1,url=https://gchat.qpic.cn/gchatpic_new/3072659646/715792440-3066821844-1BB7511E67BE9E1799447C7D6B0EB38E/0?term=2&amp;is_origin=0]",grt).text+" -res end")
logging.debug("ret whlieing")
def jsxx(group_id):
    global jsx
    res_mes_post = {"instruction_message": "message_seq", "group_id": group_id, "message_id": ""}
    message_group_id = res_mes_post["group_id"]
    url = "http://127.0.0.1:5700/get_group_msg_history?group_id=" + message_group_id
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36"}
    res = requests.get(url=url, headers=headers).json()
    rese=res["data"]
    try:
        rese1=rese["messages"]
        rese2=rese1[-1]
        jsx = rese2['message_id']
        rese2_s=rese2['sender']
        rese3={"msg":rese2['message'],"card":rese2_s['card'],"name":rese2_s['nickname'],"QQ":rese2_s['user_id'],"role":rese2_s['role']}
    except:
        logging.error("[WARNING]: 获取群历史消息失败: Packet timed out")
    return rese3
def fz():
    re=random.randint(1,5)
    if re == 1:
        hfi="嘿嘿，腐竹不在"
    if re == 2:
        hfi="嘿嘿，蹦蹦炸弹"
    if re == 3:
        hfi="嘿嘿，快点tm和老子去炸鱼"
    if re == 4:
        hfi="嘿嘿，腐竹逝世了，啊哈哈哈哈"
    if re == 5:
        hfi="啊哈哈哈，只因汤来咯"
    print("回复:"+hfi)
    return hfi
while True:
    time.sleep(0.1)
    a=jsxx(grt)
    if a['msg']=="腐竹在吗" and jsx != jsxz:
        fs(fz(),grt)
        jsxz = jsx
    elif a['msg']=="服主在吗" and jsx != jsxz:
        fs(fz(),grt)
        jsxz = jsx
    elif a["msg"]=="功能菜单" and jsx != jsxz:
        fs("━━━━━━━━功能菜单━━━━━━━━━━\n1.腐竹在吗\n2.用s-b骂机器人\n3.压数\n重点解释:<压数> <功能>功能有 1.随机压池 2.c1 or c2池\n━━━━━━━━by  小凉━━━━━━━━━━",grt)
    elif "机器人" in a['msg'] and jsx != jsxz and "傻逼" in a["msg"]:
        fs("我不是,你才是[CQ:image,file=1bb7511e67be9e1799447c7d6b0eb38e.image,subType=1,url=https://gchat.qpic.cn/gchatpic_new/3072659646/715792440-3066821844-1BB7511E67BE9E1799447C7D6B0EB38E/0?term=2&amp;is_origin=0]",grt)
        jsxz = jsx
        print("关键词触发:机器人,傻逼 回复:我不是，你才是[gif-少鹿大傻掰]")
    elif "机器人" in a['msg'] and jsx != jsxz and "sb" in a["msg"]:
        fs("我不是,你才是[CQ:image,file=1bb7511e67be9e1799447c7d6b0eb38e.image,subType=1,url=https://gchat.qpic.cn/gchatpic_new/3072659646/715792440-3066821844-1BB7511E67BE9E1799447C7D6B0EB38E/0?term=2&amp;is_origin=0]",grt)
        jsxz = jsx
        print("关键词触发:机器人,sb 回复:我不是，你才是[gif-少鹿大傻掰]")
    elif "压数" in a['msg'] and jsx != jsxz:
        print("test")
        if "压数 c1池" in a['msg']:
            c1y = a["msg"].split()
            print(c1y)
            try:
                if c1 == 0:
                    fs("请输入:压数 随机压池",grt)
                elif int(c1y[2]) == c1:
                    fs("压池c1 完美!",grt)
                    c1=0
                elif int(c1y[2]) > c1:
                    fs("压池c1 大了!",grt)
                elif int(c1y[2]) < c1:
                    fs("压池c1 小了!",grt)
            except:
                fs("压池c1 压数缺少!",grt)
                print("ERCODE 1002")
            jsxz = jsx
        elif "压数 c2池" in a['msg']:
            c2y = a["msg"].split()
            try:
                if c2 == 0:
                    fs("请输入:压数 随机压池",grt)
                elif int(c2y[2]) == c2:
                    fs("压池c2 完美!",grt)
                    c2 = 0
                elif int(c2y[2]) > c2:
                    fs("压池c2 大了!",grt)
                elif int(c2y[2]) < c2:
                    fs("压池c2 小了!",grt)
            except:
                fs("压池c2 压数缺少!",grt)
                print("ERCODE 1002")
            jsxz = jsx
        elif a['msg']=="压数 随机压池" and jsx != jsxz:
            yc = random.randint(1,2)
            if yc == 1:
                c1 = random.randint(1,50)
                print("c1压池准备完成 1-50")
                fs("c1压池准备完成 1-50",grt)
            if yc == 2:
                c2 = random.randint(1,50)
                print("c2压池准备完成 1-50")
                fs("c2压池准备完成 1-50",grt)
            jsxz = jsx
        jsxz = jsx
    elif "sudo" in a['msg'] and jsx != jsxz:   #sudo -updata 1.0.3 bate
        if a["msg"] == "sudo 机器人重启" and a["role"]=="admin":
            fs("机器人正在重启-将在控制台显示进程",grt)
            time.sleep(5)
            fs("机器人重新启动成功!",grt)
            pass
        elif a["msg"] == "sudo sh池查看" and a["role"]=="admin":
            fs("#sudo>>压数:1池-"+str(c1)+" 2池-"+str(c2),grt)
        jsxz = jsx

