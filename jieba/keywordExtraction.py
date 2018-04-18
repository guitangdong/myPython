import jieba.analyse

content = open('唐诗.txt', 'rb').read()
tags = jieba.analyse.extract_tags(content, topK=100)
print(",".join(tags))
#引入idf文件
print("_"*80)
jieba.analyse.set_idf_path("idf.txt");
tags = jieba.analyse.extract_tags(content, topK=100)
print(",".join(tags))