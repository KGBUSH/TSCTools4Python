# encoding: utf-8


from Entity.TimeWindow import *
from Entity.Danmaku import *

import math


class WindowBuilder(object):
    """
    window的构建
    """

    def __init__(self, window_size, window_slide_step):
        """
        初始化
        :param window_size:  一个窗口的大小，秒数
        :param window_slide_step:  窗口之间 滑动的时间
        :return:
        """
        self._windowsize = window_size
        self._window_slistep = window_slide_step


    def buildWindows(self, sortedList):
        """
        按照窗口大小和窗口之间的滑动时间构建 Windows的List
        :param sortedList: 已经按照出现时间排好序的 List<Danmaku>
        :return: List<TimeWindow>
        """

        """
        public List<TimeWindow> buildWindows(List<Danmaku> sortedList){
            long idCount = 0;
            double currentWindowStart = 0;
            double currentWindowEnd = Math.ceil(currentWindowStart + windowSize);
            List<TimeWindow> result = new ArrayList<TimeWindow>();
            while( sortedList.size() > 0 ){
                List<Danmaku> currentList = new ArrayList<Danmaku>();
                for ( Danmaku danmaku : sortedList ){
                    if ( danmaku.getVideoSecond() < currentWindowEnd ){
                        currentList.add(danmaku);
                    }
                    else break;
                }

                System.out.println("Building window " + idCount + "...");

                TimeWindow timeWindow = new TimeWindow(idCount,currentWindowStart,currentWindowEnd);
                idCount++;
                timeWindow.buildFromDanmaku(currentList);//currentList是当前这个window里的Danmaku
                result.add(timeWindow);

                currentWindowStart = Math.ceil(currentWindowStart + windSlideStep);
                currentWindowEnd = Math.ceil(currentWindowStart + windowSize);
                for ( Danmaku danmaku : currentList ){
                    if ( danmaku.getVideoSecond() < currentWindowStart ) sortedList.remove(danmaku);
                    else break;
                }
            }
            return result;
        }
        """
        idCount = 0
        currentWindowStart = 0
        currentWindowEnd = math.ceil(currentWindowStart + self._windowsize)
        result_WindowsList = []  # [TimeWindow1, TimeWindow2,.....]
        while len(sortedList) > 0:
            current_danmakulist = []  # List<Danmaku>

            for danmaku in sortedList:
                if danmaku.video_second < currentWindowEnd:
                    current_danmakulist.append(danmaku)
                else:
                    break

            print 'Building window' + str(idCount) + '...'
            timeWindow = TimeWindow(idCount, currentWindowStart, currentWindowEnd)
            idCount += 1
            timeWindow.buildFormDamaku(current_danmakulist)  # currentList是当前这个window里的List<Danmaku>
            result_WindowsList.append(timeWindow)

            currentWindowStart = math.ceil(currentWindowStart + self._window_slistep)  #改变start和end的时间（next window）
            currentWindowEnd = math.ceil(currentWindowStart + self._windowsize)

            for danmaku in current_danmakulist:
                if danmaku.video_second < currentWindowStart:
                    sortedList.remove(danmaku)
                else:
                    break

        return result_WindowsList