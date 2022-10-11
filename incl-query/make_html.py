import xml.etree.ElementTree as ET
import json
import urllib.request
import urllib.parse

def transform_maker(key, object):
    transform = ET.Element('transform', {'DEF': key})
    shape = shape_maker(object)
    transform.append(shape)

    return transform


def shape_maker(object):
    shape = ET.Element('shape')
    appearance = ET.SubElement(shape, 'appearance')
    # characterの場合だけ赤色
    if object["objectType"] == "character":
        material = ET.SubElement(appearance, 'material', {'diffuseColor': '1 0 0', 'transparency': '0'})
    else: 
        material = ET.SubElement(appearance, 'material', {'diffuseColor': '0 1 0', 'transparency': '0.9'})
    material.text = ' '
    a = object["bboxSize"]
    size = str(float(a[0]))+","+str(float(a[1]))+","+str(float(a[2]))
    box = ET.SubElement(shape, 'box', {'size': size, 'solid': 'false'})
    box.text = " "

    return shape

def timeSensor_maker(num):
    timeSensor = ET.Element('timeSensor', {'DEF': 'time', 'cycleInterval': str(num), 'loop': 'true'})
    timeSensor.text = " "

    return timeSensor


def PositionInterpolator_maker(key, object):
    keys = ""
    for k in object["key"]:
        keys = keys + str(k) + " "
    keyValue = ""
    for kv in object["keyValue"]:
        keyValue = keyValue + str(float(kv[0]))+" "+str(float(kv[1]))+" "+str(float(kv[2])) + "  "
    positionInterpolator = ET.Element('PositionInterpolator', {'DEF': "move"+key, 'key': keys, 'keyValue': keyValue})
    positionInterpolator.text = " "

    return positionInterpolator


def Route_maker(key):
    route1 = ET.Element('Route', {'fromNode': 'time', 'fromField': 'fraction_changed', 'toNode': "move"+key, 'toField': 'set_fraction'})
    route1.text = " "
    route2 = ET.Element('Route', {'fromNode': "move"+key, 'fromField': 'value_changed', 'toNode': key, 'toField': 'translation'}) 
    route2.text = " "
    routes = [route1, route2]

    return routes

def header_maker(html):
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

def body_maker(html):
    # bodyとhtml要素
    body = ET.SubElement(html, 'body')
    sectionLabel = ET.SubElement(body, 'h1')
    sectionLabel.text = "virtualhome2kg-Admire_paintings.ttlのbboxを描いてみる"
    descriptionLabel = ET.SubElement(body, 'p')
    descriptionLabel.text = "操作方法は下の方にあります．マウスでくるくる回せます．キャラクターだけ赤色，他は透明な緑色です．動いてますが，動画と時間はあっていません．バウンディングボックスのサイズは初期値のままです．キャラクタがかがんだり方向転換していたりしても変わりません．"
    
    return body

def usage_maker(body):
    ## 操作方法の説明
    ET.SubElement(body, "h4").text = "操作方法"
    table = ET.SubElement(body, 'table')
    tr = ET.SubElement(table, 'tr')
    ET.SubElement(tr, 'th').text = "機能"
    ET.SubElement(tr, 'th').text = "マウスボタン"
    tbody = ET.SubElement(table, 'tbody')
    tr1 = ET.SubElement(tbody, 'tr')
    ET.SubElement(tr1, 'td').text = "回転"
    ET.SubElement(tr1, 'td').text = "左 / 左 + Shift"
    tr2 = ET.SubElement(tbody, 'tr')
    ET.SubElement(tr2, 'td').text = "パン"
    ET.SubElement(tr2, 'td').text = "真ん中 / 左 + Ctrl"
    tr3 = ET.SubElement(tbody, 'tr')
    ET.SubElement(tr3, 'td').text = "ズーム"
    ET.SubElement(tr3, 'td').text = "右 / ホイール / 左 + Alt"
    tr4 = ET.SubElement(tbody, 'tr')
    ET.SubElement(tr4, 'td').text = "描画対象が真ん中に来るようにする"
    ET.SubElement(tr4, 'td').text = "左をダブルクリック"
    tr5 = ET.SubElement(tbody, 'tr')
    ET.SubElement(tr5, 'td').text = "ビューを初期値に戻す"
    ET.SubElement(tr5, 'td').text = "キーボードのA"
    tr6 = ET.SubElement(tbody, 'tr')
    ET.SubElement(tr6, 'td').text = "小さいものも表示する"
    ET.SubElement(tr6, 'td').text = "キーボードのS"

def get_firstSituation(activity_url):
    with open("query_firstSituation.rq", "r") as f:
        query = f.read()
    query = query.replace("PLACE_HOLDER", activity_url)
    firstSituation = _query(query)

    return firstSituation

def get_nextSituation(previousSituation):
    with open("query_nextSituation.rq", "r") as f:
        query = f.read()
    query = query.replace("PLACE_HOLDER", previousSituation)
    nextSituation = _query(query)

    return nextSituation

def _query(query):
    url = "http://localhost:7200/repositories/kgrc2022"
    hoge = urllib.request.Request(url=url, data="query="+urllib.parse.urlencode(query), headers="Accept:application/x-trig")
    return hogehoge

def main():
    html = ET.Element('html')
    ## ヘッダとボディの最初
    header_maker(html)
    body = body_maker(html)

    # ここから中身
    x3d = ET.SubElement(body, 'x3d', {'width': '1920px', 'height': '1080px'})
    scene = ET.SubElement(x3d, 'scene')
    ET.SubElement(scene, 'environment', {'smallFeatureCulling': 'true'}).text = " "

    # first situation
    # sizeをもらわないといけない．
    firstSituation = get_firstSituation()

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
    # タイムセンサーが先
    timeSensor = timeSensor_maker(4)
    scene.append(timeSensor)
    # 物は後
    for o in objectDict:
        transform = transform_maker(o, objectDict[o])
        scene.append(transform)
        positionInterpolator = PositionInterpolator_maker(o, objectDict[o])
        scene.append(positionInterpolator)
        routes = Route_maker(o)
        for route in routes:
            scene.append(route)
    ## 操作方法の説明  
    usage_maker(body)

    tree = ET.ElementTree(html)
    tree.write('virtualhome2kg-Admire_paintings.html', encoding='utf-8')

if __name__ == "__main__":
    main()