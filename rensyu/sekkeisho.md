# 落としどころ
- アクティビティ一つ分のものの動きを描画してみる．
- bboxのサイズが変わる（多分姿勢とかだと思う）を反映するのはちょっと難しい．
- onlineで作れればいいけれど，staticに作るところからかしら．

# すること
1. 情報をもらう
   1. ~~ActivityからEvent一覧をもらう．~~
   2. ~~EventからSituationをもらう．~~
   3. SituationからStateをもらう．
      1. このStateたちは同じ時間を切り出したものなので同じ時間に描画してほしい．
   4. 次のSituationをもらう．
      1. 次のSituationがなくなるまで．
      2. ※全てのStateが全てのSituationに対応づいているかは不明なので，State単位でたどる方が賢いかもしれない．
   5. Stateの持ち主とbboxをセットでもらっておく．
      1. 持ち主は時間にindexedされている概念なので，オブジェクトとしての持ち主を探してラベルをもらう．->rdfs:label + identifierかしら．
2. nodeを作る
   1. Stateの持ち主分だけboxが必要．これはラベルをラベルにする．
   2. timeSensorは適当に作る．
   3. PositionInterpolatorもStateの持ち主分だけ必要．keyValueにbboxを並べる．
      1. keyはsituationの数分かしら？
   4. RouteはtimeSensorとPositionInterpolatorの組み合わせ分作る．
3. 終わり．


# 疑問
vh2kg:virutalHomeって何だ？Rangeがvh2kg:VirtualHomeとなっているけれど，それが何者なのか分からない．

# memo
ほしいもの
  Situationの系列がほしい．
    これは都度クエリするかしら．
  Situationごとにboxがほしい．

material diffuseColorにオブジェクトクラスごとの色を割り当てるかしら．

とりあえず，Situationを4つ分jsonでもらったのでそれをパースしてhtmlを作りましょう．