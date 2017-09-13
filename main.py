#!usr/bin/python
#coding: utf8

import sys
from jieba import cut
import re
from string import punctuation
import logging
import os
from gensim.models import word2vec, KeyedVectors
from gensim.models.word2vec import LineSentence
reload(sys)
sys.setdefaultencoding('utf8')

def current_path():
    current_path = os.path.dirname(__file__)
    if not current_path:
        current_path = os.getcwd()
    return current_path

def read_data(file_name):
    with open(file_name, 'rb') as r_fh:
        return (line.strip().decode('utf8') for line in r_fh.readlines())

def cut_word_str(line):
    ignore_str = u'！（）【】，。《》？、'+punctuation
    return ' '.join(each for each in cut(line) if each not in ignore_str)

if __name__ == '__main__':
    current_file = sys.argv[0]
    base_path = current_path()
    file_path = os.path.join(base_path, current_file)
    
    # logger = logging.getLogger(current_file)
    # logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.WARNING)

    cut_data_str = '\n'.join(cut_word_str(line) for line in read_data('data'))
    with open('cut_data', 'w') as w_fh:
        w_fh.write(cut_data_str)
    file_path = os.path.join(base_path, 'cut_data')

    # logging.basicConfig(format='%(asctime)s : %(levelname)s : %(messages)', level=logging.INFO)
    sentences = word2vec.Text8Corpus('text8')
    model = word2vec.Word2Vec(sentences, 200)
    # model = word2vec.Word2Vec(LineSentence(file_path), 200)
    model.save('model')
    # model.wv.save_word2vec_format('model.bin', binary=True)
    model.wv.save_word2vec_format('model.bin')

    # model_org = KeyedVectors.load_word2vec_format('model.bin', binary=True)
    # for xx in model_org.most_similar(u'公路局'):
    #     print xx[0], xx[1]
    # GX来宾公路局_GSM基站_H
    # GX来宾公路局_GSM1800基站_H
    # print cut_word_str(u'GX来宾公路局_GSM基站_H').split(' ')
    # print model_org.similarity(cut_word_str(u'GX来宾公路局_GSM基站_H').split(' '), cut_word_str(u'GX来宾城厢铁象_GSM基站_H').split(' '))
    pass

