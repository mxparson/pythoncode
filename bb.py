import requests
import json

def open_url(url):
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    #Referer = "https://h.bilibili.com/d"
    res = requests.get(url,headers=headers)


    return res


def main():
    res = open_url("https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_num=0&page_size=20")#拿东西
    jg_json = json.loads(res.text)#解析
    a = jg_json["data"]
    b = a["items"]
    c = []
    for i in range(len(b)):
        c.append(b[i])

    d = []#放图片所在贴链接的容器
    e = []#放图片的容器
    for each in c:
        d.append(each["item"]["doc_id"])
        e.append(each["item"]["pictures"][0]["img_src"])

    res = res = open_url("https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_num=1&page_size=20")#抓第二页，我比较懒，勤奋的鱼油可以封装成一个函数，爱抓几页抓几页
    jg_json = json.loads(res.text)
    a = jg_json["data"]
    b = a["items"]
    c = []
    for i in range(len(b)):
        c.append(b[i])

    for each in c:
        d.append(each["item"]["doc_id"])
        e.append(each["item"]["pictures"][0]["img_src"])


    with open("cosplay.html","w") as f:#输出，不靠喊。
        for i in range(len(d)):
            f.write('<a href="https://h.bilibili.com/' + str(d[i]) + '" target="_black"><img src="' + e[i] + '" style="max-height:500;max-width:500;"/></a>')
            
    input("回车退出：")



if __name__ == "__main__":
    main()
