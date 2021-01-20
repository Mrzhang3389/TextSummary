import json
import requests


def get_text_summary(text, max_len=512):
    upload_data = {"accept": "application/json"}
    upload_res = requests.get("http://192.168.31.220:8000/{}?max_len={}".format(text, max_len), upload_data)
    encoding = json.loads(upload_res.content, encoding="utf8")
    return encoding


if __name__ == '__main__':
    text = "Wiki软件由软件设计模式社群开发，用来书写与讨论模式语言。沃德·坎宁安于1995年3月25日成立了第一个Wiki网站：WikiWikiWeb，用来补充他自己经营的软件设计模式网站。他发明了Wiki这个名字以及相关概念，并且实现了第一个Wiki引擎。坎宁安说自己是根据檀香山的Weekee Weekee（意为“快点快点”）公车取名的。这是他到檀香山学会的第一个夏威夷语句子。坎宁安说，Wiki的构想来自他自己在1980年代晚期利用苹果电脑HyperCard程序作出的一个小功能[4]。HyperCard类似名片整理程序，可用来纪录人物与相关事物。HyperCard管理许多称为“卡片”的数据，每张卡片上都可划分字段、加上图片、有样式的文字或按钮等等，而且这些内容都可在查阅卡片的同时修改编辑。HyperCard类似于后来的网页，但是缺乏一些重要特征。坎宁安认为原来的HyperCard程序十分有用，但创造卡片与卡片之间的链接却很困难。于是他不用HyperCard程序原本的创造链接功能，而改用“随选搜索”的方式自己增添了一个新的链接功能。用户只要将链接输入卡片上的一个特殊字段，而这个字段每一行都有一个按钮。按下按钮时如果卡片已经存在，按钮就会带用户去那张卡片，否则就发出哔声，而继续压着按钮不放，程序就会为用户产生一张卡片。坎宁安向他的朋友展示了这个程序和他自己写的人事卡片，往往会有人指出卡片之中的内容不太对，他们就可当场利用HyperCard初始的功能修正内容，并利用坎宁安加入的新功能补充链接。坎宁安后来在别处又写了这样的功能，而且这次他还增加了多用户写作功能。新功能之一是程序会在每一次任何一张卡片被更改时，自动在“最近更改”卡片上增加一个连往被更改卡片的链接。坎宁安自己常常看“最近更改”卡片，而且还会注意到空白的说明字段会让他想要描述一下更改的摘要"
    text_summary = get_text_summary(text)
    print(text_summary)
