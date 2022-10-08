import xml.etree.ElementTree as ET
import json
import pprint


def transform_maker(key, object):
    transform = ET.Element('transform', {'DEF': key})
    shape = shape_maker(object)
    transform.append(shape)

    return transform


def shape_maker(object):
    shape = ET.Element('shape')
    appearance = ET.SubElement(shape, 'appearance')
    material = ET.SubElement(appearance, 'material', {'diffuseColor': '1 0 0', 'transparency': '0.9'})
    material.text = ' '
    a = object["bboxSize"]
    size = str(float(a[0]))+","+str(float(a[1]))+","+str(float(a[2]))
    box = ET.SubElement(shape, 'box', {'size': size, 'solid': 'false'})

    return shape

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
# headべた書き
head = ET.SubElement(html, 'head')
meta = ET.SubElement(
    head, 'meta', {'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge'})
title = ET.SubElement(head, 'title')
title.text = "KGRC-RDFのbboxを描いてみた"
script = ET.SubElement(head, 'script', {
                       'type': 'text/javascript', 'src': 'https://www.x3dom.org/download/x3dom.js'})
script.text = ' '
link = ET.SubElement(head, 'link', {
                     'rel': 'stylesheet', 'type': 'text/css', 'href': 'https://www.x3dom.org/download/x3dom.css'})
link.text = ' '

# bodyとhtml要素
body = ET.SubElement(html, 'body')
sectionLabel = ET.SubElement(body, 'h1')
sectionLabel.text = "virtualhome2kg-Admire_paintings.ttlのbboxを描いてみる"
descriptionLabel = ET.SubElement(body, 'p')
descriptionLabel.text = "ろーれむいぷさむどろーるしっとあめっと，こんせくてたーあでぃぴしんぐえりと，せどどあいうすもっどてむぽーるいんしでぃどぅんとうとらぼれえとどろーれまぐなありくあ。"

# ここから中身
x3d = ET.SubElement(body, 'x3d', {'width': '1920px', 'height': '1080px'})
scene = ET.SubElement(x3d, 'scene')

# first situation
# sizeをもらわないといけない．
with open("situation_1.srj", "r") as f:
    firstSituation = json.load(f)

objectDict = {}

for row in firstSituation["results"]["bindings"]:
    objectDict[row["objectLabel"]["value"] + row["objectId"]["value"]] = {
        "bboxSize": (row["BSX"]["value"], row["BSY"]["value"], row["BSZ"]["value"]),
        "keyValue": [(row["BCX"]["value"], row["BCY"]["value"], row["BCZ"]["value"])],  # ここはappendで追加する．
        "key": [0],  # ここもappendでkeyのlengthを追加する．
        "objectType": row["objectLabel"]["value"],
    }


# 残りのsituation
# sizeは一個目そのまま．繰り返しで足していく．
fileList = ["situation_2.srj", "situation_3.srj", "situation_4.srj"]
for file in fileList:
    with open(file, "r") as f:
        nextSituation = json.load(f)
    for row in nextSituation["results"]["bindings"]:
        objectDict[row["objectLabel"]["value"] + row["objectId"]["value"]]["keyValue"].append((row["BCX"]["value"], row["BCY"]["value"], row["BCZ"]["value"]))
        objectDict[row["objectLabel"]["value"] + row["objectId"]["value"]]["key"].append(len(objectDict[row["objectLabel"]["value"] + row["objectId"]["value"]]["key"]))

# pprint.pprint(objectDict)

# nodeを作ります．
for o in objectDict:
    transform = transform_maker(o, objectDict[o])
    scene.append(transform)

tree = ET.ElementTree(html)
tree.write('test.html', encoding='utf-8')
