import time
import requests
from common.config import APP_KEY, APP_SECRET, URL
import threading

# 获取当前时间
def get_now():
    now = int(time.time())
    # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    time_array = time.localtime(now)
    other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    print(other_style_time)
    return other_style_time


class TaskErr(Exception):
    def __init__(self, task_id, msg):
        self.task_id = task_id
        self.msg = msg

    def __str__(self):
        return f"HttpErr at {self.task_id}, msg:{self.msg}"


# 格式化sql的key,value值
def format_sql_values(data):
    sql_items = []
    sql_values = []

    for key in data:
        sql_items.append(key)
        if isinstance(data[key], str):  # 如果是字符串 加上引号
            sql_values.append("\'" + data[key] + "\'")
        else:
            sql_values.append(data[key])
    return sql_items, sql_values


# 获取access_token
def get_access_token():
    response = requests.get(
        url=URL + "/gettoken",
        params=dict(appkey=APP_KEY, appsecret=APP_SECRET)
    )
    access_token = response.json()["access_token"]
    return access_token


# 多线程
def threads_func(func, arr, n):
    threads = []
    mid = int(len(arr) / n)
    for i in range(mid):
        if i+1 == mid:
            temp_thread = threading.Thread(target=func, args=(i*n, len(arr)))
        else:
            temp_thread = threading.Thread(target=func, args=(i*n, (i+1)*n))
        threads.append(temp_thread)

    for t in threads:
        # t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
