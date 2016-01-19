# coding:utf-8


from Util.ExtractUtil import *
from Entity.GlobalValue import *

import json
import os
import sys
# default_encoding = 'utf-8'
# if sys.getdefaultencoding() != default_encoding:
#     reload(sys)
#     sys.setdefaultencoding(default_encoding)


class TimeWindow(object):
    """
    描述TimeWindow的基本属性
    _id,
    _starttime,
    _endtime,

    _useralive
    _numdanmaku
    _averagelength
    _userfeature
    """

    def __init__(self, id, starttime, endtime):
        self._id = id
        self._starttime = starttime
        self._endtime = endtime

        # 该窗口的user数量
        self._userAlive = 0

        # 这个窗口的user id列表
        # self._window_userIDList = []

        # 该窗口的弹幕数量
        self._numofDanmakulist = 0

        # 该窗口的弹幕平均长度
        self._averageLength = 0

        # userfeature：{ userid:{ "detail":{  } }, ......  }
        # userfeature：{ userid:{ "detail":str }, ......  }  用结巴之前
        # self._userFeature = {'ssb':{"detail":'这是我的测试'}}
        self._userFeature = {}


    def buildFormDamaku(self, danmakulist):
        """
        这个是给每个window.txt 所有属性赋值
        :param danmakulist: 这个window里面的所有弹幕的list：[Danmaku, Danmaku, Danmaku...]
        :return: no return
        """

        """
        public void buildFromDanmaku(List<Danmaku> danmakuList){
            // 这个是给每个window.txt开始的属性赋值
            // 参数是一个window里的Danmaku的list
            ExtractUtil extractUtil = new ExtractUtil(danmakuList);
            List<String> userIDList = extractUtil.extractUser();
            userAlive = userIDList.size();
            numOfDanmaku = danmakuList.size();
            averageLength = 0;
            for ( String s : userIDList ){
                Map<String,Object> userWords = extractUtil.extractWords(s);
                if ( userWords == null ) continue;
                Vector vector = new Vector(userWords);
                userFeature.put(s,vector);
                averageLength += vector.getSize();
            }
            this.averageLength = averageLength/numOfDanmaku;
        }
        """

        window_userIDList = ExtractUtil.ExtractUser(danmakulist)
        self._userAlive = len(window_userIDList)
        self._numofDanmakulist = len(danmakulist)

        for userid in window_userIDList:
            userwords = ExtractUtil.ExtractWords(userid, danmakulist)
            self._averageLength += len(userwords)
            dict_userid = {"detail": userwords}
            self._userFeature.update({userid: dict_userid})

        self._averageLength /= self._numofDanmakulist
        print self._userFeature



    def output(self):
        """
        把 timeWindowClipList 写入文件（多个window.txt）
        :return: no return
        """
        try:
            str_dictwindow = '{'  # 开始
            str_dictwindow += '"id":' + str(self._id) + ','
            str_dictwindow += '"startTime":' + str(self._starttime) + ','
            str_dictwindow += '"endTime":' + str(self._endtime) + ','
            str_dictwindow += '"userAlive":' + str(self._userAlive) + ','
            str_dictwindow += '"numOfDanmaku":' + str(self._numofDanmakulist) + ','
            str_dictwindow += '"averageLength":' + str(self._averageLength) + ','
            str_dictwindow += '"userFeature":' + json.dumps(self._userFeature, encoding="UTF-8", ensure_ascii=False)

            str_dictwindow += '}'  # 结束

            if not os.path.isdir(GLOBAL_windowsTxtpath):
                os.makedirs(GLOBAL_windowsTxtpath)

            fw = open(GLOBAL_windowsTxtpath + '\\Window' + str(self._id) + ".txt", 'w')
            fw.write(str_dictwindow.encode('utf-8'))
            fw.close()
        except Exception,e:
            print 'Window', str(self._id), 'Exception: ', e


if __name__ == '__main__':
    timewindow = TimeWindow(2, 0, 30)
    # timewindow.output()

    bb = '水电费'
    a = {'ssb': {"detail": "这是我的测试"}, "ss": {"detail": "这是我的测试"}}
    b = json.dumps(a, encoding="UTF-8", ensure_ascii=False)
    print b
    fw = open(GLOBAL_windowsTxtpath + '\\Window' + str(2) + ".txt", 'w')
    fw.write(b.encode('utf-8'))
    fw.close()