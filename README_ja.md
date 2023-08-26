# viz-kgrc-rdf-bbox-x3dom

## 使い方

### 前提
- GraphDB
  - このノートブックはOntoText社の[GraphDB](https://graphdb.ontotext.com/)を使うことを意図しています．
  - GraphDBを取得してあなたの環境でデータベースサーバを動かしてください．
  - リポジトリ名は，`KGRC4SI_20230714_r2`としてください．ノートブックの第3セルで変更可能です．
- Knowledge Graph
  - 「ナレッジグラフ推論チャレンジ【実社会版】提供データセット」が必要です．
  - [こちら]((https://github.com/KnowledgeGraphJapan/KGRC-RDF/tree/kgrc4si))をご参照ください．
- Python とパッケージたち
  - rdflib
  - sparqlwrapper

### 設定と実行
1. `graphdb_auth.txt`に必要な情報を入力します．
   1. 1行目にGraphDBのエンドポイントを入れてください．
   2. 2,3行目はあなたのクレデンシャル情報です．ユーザ名とパスワード．
2. ノートブックを動かすと，htmlファイルが手に入ります．
4. htmlファイルを開くと特定のシーンの3次元での可視化結果が得られます．

## 謝辞
素晴らしいノートブックを作ってくださった[YE-WIN-Unity](https://github.com/YE-WIN-Unity)に感謝します．  
また，「ナレッジグラフ推論チャレンジ【実社会版】」という素晴らしいプロジェクトにも感謝しています．このリポジトリは、プロジェクトの[データセット](https://github.com/KnowledgeGraphJapan/KGRC-RDF/tree/kgrc4si)を利用することを想定しています．  
可視化部分は[x3dom tech](https://www.x3dom.org/)を使って実装しています．本プロジェクトにも感謝します．
