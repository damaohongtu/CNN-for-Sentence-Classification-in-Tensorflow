from gensim.models import KeyedVectors
import numpy as np
import util.data_helpers
from util.file_path import filepath
import pandas as pd


word_size=300
# 在train.py中判断doc2vec.pkl是否存在，不存在调用doc_to_vec()函数
def doc_to_vec():
	print ("-----------------doc2vec begin----------------")
	print ("loading pretrained word2vec model...")
	googlenews = KeyedVectors.load_word2vec_format (filepath.googlenews_vectors_negative300, binary=True)
	x_text, y = util.data_helpers.load_data_and_labels (filepath.positive_data_file, filepath.negative_data_file)
	x=[]
	max_sentence_size = max ([len (x.split (" ")) for x in x_text])
	print("finish load word2vec model...")

	for sentence in x_text:
		temp = np.zeros (shape=[max_sentence_size, word_size])
		count=0
		for word in sentence.split(" "):
			try:
				temp[count]=googlenews[word]
			except	KeyError:
				print("word not in vacaulary")
			count=count+1
		x.append(temp)
	x=np.asarray(x)
	x.dump(filepath.rt_polarity_pickle)
	#pickle.dump(x,filepath.rt_polarity_pickle)
	return x
