import jieba

news = "交通运输部规划研究院、交通运输部科学研究院联合高德地图等机构," \
       "近日联合发布了《2017年第三季度中国主要城市交通分析报告》(以下简称“报告”) 。"

#精确模式
words = jieba.cut(news,cut_all=False)
print('精确模式')
print('/'.join(words))
print('_'*80)

#全模式
words = jieba.cut(news,cut_all=True)
print('全模式')
print('/'.join(words))
print('_'*80)

#添加自定义词库
jieba.load_userdict("mydict.txt")

#cut_all 默认是精确模式
print('引入自定义词库后的默认精确模式')
words = jieba.cut(news)
print('/'.join(words))
print('_'*80)

#cut_for_search 该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细
words = jieba.cut_for_search(news)
print('引入自定义词库后的cut_for_search')
print('/'.join(words))
print('_'*80)
