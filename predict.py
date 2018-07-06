import gensim
# 从控制台获取句子
print(gensim.__version__)
# 对句子进行预处理，转换为词向量

# 对句子的类别进行划分

positive_examples = list(open('./data/raw_data/rt-polaritydata/rt-polarity.pos', "r", encoding='utf-8').readlines())
print(len(positive_examples))
positive_examples = [s.strip() for s in positive_examples]
print(positive_examples)