class Filepath:
	def __init__(self):
		# 将路径设置为绝对路径
		path="F:/WORKPLACE/CNN-for-Sentence-Classification-in-Tensorflow/data/"
		self.positive_data_file = path+"raw_data/rt-polaritydata/rt-polarity.pos"
		self.negative_data_file = path+"raw_data/rt-polaritydata/rt-polarity.neg"
		self.googlenews_vectors_negative300=path+"processed-data/GoogleNews-vectors-negative300.bin.gz"
		self.rt_polarity_pickle=path+"processed-data/rt_polarity.pkl"
filepath=Filepath()