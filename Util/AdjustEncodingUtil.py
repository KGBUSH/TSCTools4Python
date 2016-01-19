# encoding: utf-8

import os
import chardet
from os.path import join

class AdjustEncodingUtil(object):
    """
    调整编码
    """

    @staticmethod
    def change_encoding_folder(dest):
        """
        change the encoding type of the files which in the folder(dest) into target_encoding
        and, the files' type is file_type
        :param dest: the location of the folder
        :return:
        """
        target_encoding = 'utf-8'
        file_type = '.txt'

        for root, dirs, files in os.walk(dest):
            for OneFileName in files:
                if OneFileName.find(file_type) == -1:
                    continue
                OneFullFileName = join(root, OneFileName)
                fr = open(OneFullFileName, 'r')
                l = fr.read()
                sorce_encoding = chardet.detect(l)['encoding']  # 检测编码
                if sorce_encoding == target_encoding:
                    continue
                l = l.decode(sorce_encoding, 'ignore').encode(target_encoding)

                fr.close()
                fw = open(OneFullFileName, 'w')
                fw.write(l)
                fw.close()


if __name__ == "__main__":
    dest = 'C:\Users\KGBUS\PycharmProjects\gensim-test2\lzy_severalMovieDanmudata\TheTrumanShowTimeWindow'
    AdjustEncodingUtil.change_encoding_folder(dest)