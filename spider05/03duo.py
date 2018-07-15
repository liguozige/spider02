"""

"""
import threading

t=threading.Thread(target="func",args='')
t.start()
#守护主线程
t.setDaemon()
#queue
from queue import Queue
Queue()
#插入元素 put()计数-1
#取出元素 get() 不会-1
#task_done()配合get使用 计数器-1
