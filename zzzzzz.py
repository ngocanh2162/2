from pyvi import ViTokenizer, ViPosTagger
from sklearn.base import TransformerMixin, BaseEstimator

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

import pandas as pd

class FeatureTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.tokenizer = ViTokenizer.ViTokenizer()
        self.pos_tagger = ViPosTagger.ViPosTagger()

    def fit(self, *_):
        return self

    def transform(self, X, y=None, **fit_params):
        result = X.apply(lambda text: self.tokenizer.tokenize(text))
        return result

class NaiveBayesModel(object):
    def __init__(self):
        self.clf = self._init_pipeline()

    @staticmethod
    def _init_pipeline():
        pipe_line = Pipeline([
            ("transformer", FeatureTransformer()),#sử dụng pyvi tiến hành word segmentation
            ("vect", CountVectorizer()),#bag-of-words
            ("tfidf", TfidfTransformer()),#tf-idf
            ("clf", MultinomialNB())#model naive bayes
        ])

        return pipe_line
class TextClassificationPredict(object):
    def __init__(self):
        self.test = None

    def get_train_data(self):
        # Tạo train data
        train_data = []
        train_data.append({"feature": u"Thành phố Hà Nội", "target": "thanh_pho"})
        train_data.append({"feature": u"Thành phố Vinh", "target": "thanh_pho"})
        train_data.append({"feature": u"Hà Nội", "target": "thanh_pho"})
        train_data.append({"feature": u"Vinh", "target": "thanh_pho"})
        train_data.append({"feature": u"Thành phố Sài Gòn", "target": "thanh_pho"})
        train_data.append({"feature": u"Huế", "target": "thanh_pho"})
        train_data.append({"feature": u"đường Hai Bà Trưng", "target": "duong"})
        train_data.append({"feature": u"55 Hai Bà Trưng", "target": "duong"})
        train_data.append({"feature": u"162 Trần Hưng Đạo", "target": "duong"})
        train_data.append({"feature": u"78 Tạ Quang Bửu", "target": "duong"})
        train_data.append({"feature": u"355 đường Tạ Quang Bửu", "target": "duong"})
        train_data.append({"feature": u"đường Lê Thanh Nghị", "target": "duong"})
        df_train = pd.DataFrame(train_data)
        # Tạo test data
        test_data = []
        test_data.append({"feature": u"25 Lê Thanh Nghị"})
        df_test = pd.DataFrame(test_data)
        
        # init model naive bayes
        model = NaiveBayesModel()

        clf = model.clf.fit(df_train["feature"], df_train.target)

        predicted = clf.predict(df_test["feature"])
        
        # Print predicted result
        print (predicted)
        print (clf.predict_proba(df_test["feature"]))


if __name__ == '__main__':
    tcp = TextClassificationPredict()
    tcp.get_train_data()