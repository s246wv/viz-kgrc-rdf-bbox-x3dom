import xml.etree.ElementTree as ET

def transform_maker(state):
    # TODO
    pass

def shape_maker(objectType):
    # TODO appearanceとmaterialまでセットで
    pass

def box_maker(size):
    # TODO ここでsizeが必要だった．．
    pass

def timeSensor_maker():
    # TODO 決め打ちで．
    pass

def PositionInterpolator_maker(state):
    # TODO
    pass

def Route_maker():
    # TODO
    pass


html = ET.Element('html')
## headべた書き
head = ET.SubElement(html, 'head')
meta = ET.SubElement(head, 'meta', {'http-equiv':'X-UA-Compatible', 'content':'IE=edge'})
title = ET.SubElement(head, 'title')
title.text = "KGRC-RDFのbboxを描いてみた"
script = ET.SubElement(head, 'script', {'type':'text/javascript', 'src':'https://www.x3dom.org/download/x3dom.js'})
script.text = ' '
link = ET.SubElement(head, 'link', {'rel':'stylesheet', 'type':'text/css', 'href':'https://www.x3dom.org/download/x3dom.css'})
link.text = ' '

## bodyとhtml要素
body = ET.SubElement(html, 'body')
sectionLabel = ET.SubElement(body, 'h1')
sectionLabel.text = "virtualhome2kg-Admire_paintings.ttlのbboxを描いてみる"
descriptionLabel = ET.SubElement(body, 'p')
descriptionLabel.text = "ろーれむいぷさむどろーるしっとあめっと，こんせくてたーあでぃぴしんぐえりと，せどどあいうすもっどてむぽーるいんしでぃどぅんとうとらぼれえとどろーれまぐなありくあ。"

## ここから中身
x3d = ET.SubElement(body, 'x3d', {'width':'1920px','height':'1080px'})
scene = ET.SubElement(x3d, 'scene')


tree = ET.ElementTree(html)
tree.write('test.html', encoding='utf-8')