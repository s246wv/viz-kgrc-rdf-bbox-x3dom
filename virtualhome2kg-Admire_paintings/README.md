# virtualhome2kg-Admire_paintings.ttlのbboxを描いてみる

## 概要
本作品は，[ナレッジグラフ推論チャレンジ【実社会版】のデータ](https://github.com/KnowledgeGraphJapan/KGRC-RDF/tree/kgrc4si)の内，ナレッジグラフ(Linked Open Data)の一部を3次元モデルとして可視化する試みです．  
ナレッジグラフ推論チャレンジは"人工知能技術による推論（推定）に関して、認識の共有と必要な技術の開発・促進を図ることを目的としたコンテスト"[1]とされています．特に，ナレッジグラフ推論チャレンジ【実社会版】では，高齢者の生活断片から作成されたナレッジグラフ[2]等が提供され，家庭内の生活における危険な状況の検出，生活行動ナレッジグラフの作成，定量的評価基準の作成がチャレンジタスクとして設定されています[3]．  
このナレッジグラフは，VirtualHome2KG[4, 5]に基づいたデータスキーマで提供されています．このデータスキーマは，`:Object`の`:State`を`:partOf`として持つ`:Situation`が前後(`:situationBeforeEvent`, `:situationAfterEvent`)につながっている`:Event`の系列として，生活行動を表現することを可能にしています．本作品では，そのナレッジグラフから`:Object`のバウンディングボックスを取り出し，x3dom[6]を用いて3次元モデルとして可視化を試みました．これにより，ナレッジグラフによる計算機による意味の取り扱いに，オブジェクトがどのように動いているのかを3次元モデルをくるくると回しながら人間が確認しやすくなるという特徴を追加することを意図しました．

### 参考文献
[1] ナレッジグラフ推論チャレンジ【実社会版】2022 〜生活行動における安心・安全を目指して〜, https://challenge.knowledge-graph.jp/2022/index.html Accessed 09 October 2022.  
[2] Shusaku Egami, Satoshi Nishimura, and Ken Fukuda. A Framework for Constructing and Augmenting Knowledge Graphs using Virtual Space: Towards Analysis of Daily Activities. Proceedings of the 33rd IEEE International Conference on Tools with Artificial Intelligence (ICTAI2021), pp. 1226–1230, 11 2021.  
[3] 応募要領 | ナレッジグラフ推論チャレンジ, https://challenge.knowledge-graph.jp/2022/application.html Accessed 09 October 2022.  
[4] Shusaku Egami, Satoshi Nishimura, and Ken Fukuda. VirtualHome2KG: Constructing and Augmenting Knowledge Graphs of Daily Activities Using Virtual Space. Proceedings of the ISWC 2021 Posters, Demos and Industry Tracks: From Novel Ideas to Industrial Practice co-located with 20th International Semantic Web Conference (ISWC 2021), Vol. 2980, No. 381, 10 2021.  
[5] VirtualHome2KG/Ontology, https://github.com/aistairc/VirtualHome2KG/tree/main/ontology Accessed 09 October 2022.  
[6] x3dom.org, https://www.x3dom.org/ Accessed 09 October 2022.  

## デモ
![demo](demo.gif)
![元の動画](https://github.com/KnowledgeGraphJapan/KGRC-RDF/blob/kgrc4si/Movie/Admire_paintings1.mp4?raw=true)

## 必要なもの
- 新しいウェブブラウザ
  - 詳しくは，[x3domのBrowser support](https://www.x3dom.org/contact/)をご参照ください．
- インターネット
  - 静的なhtmlファイルに見えますが，x3domにあるjavascriptを使っているので，インターネットアクセスが必要です．

## 使い方
- virtualhome2kg-Admire_paintings.htmlをウェブブラウザで開いてください．  
- 操作方法は下記の通りです．より詳細な情報は[x3domのNavigationページ](https://doc.x3dom.org/tutorials/animationInteraction/navigation/index.html)をご参照ください．

|機能|	マウスボタン|
|----|----|
|回転|	左 / 左 + Shift|
|パン|	真ん中 / 左 + Ctrl|
|ズーム|	右 / ホイール / 左 + Alt|
|描画対象が真ん中に来るようにする|	左をダブルクリック|
|ビューを初期値に戻す|	キーボードのA|
|小さいものも表示する|	キーボードのS|

## virtualhome2kg-Admire_paintings.htmlの作り方
1. `query_firstSituation.rq`と`query_nextSituation.rq`で必要な情報をjson形式で取得します．
   - `query_nextSituation.rq`では，filterで一つ前の`:Situation`を指定してください．
2. `make_html.py`を動かす．
   - 特別なパッケージは必要ないはずです．
   - 1で取得したjsonはvirtualhome2kg-Admire_paintings向けにハードコーディングしてしまっています．他のアクティビティに適用する際には，適宜修正してください．
   