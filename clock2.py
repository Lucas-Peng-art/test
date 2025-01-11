import time
import threading
import os

def focus_clock(duration):
    seconds = duration * 60  # 将时间转换为秒
    print(f"开始专注时钟，时长为{duration}分钟")
    while seconds > 0:
        minutes, seconds = divmod(seconds, 60)
        time.sleep(1)  # 暂停1秒
        print(f"{minutes}分{seconds}秒", end="\r")
    print("专注时钟结束！")

def main():
    # 这里可以设置专注时钟的时间长度
    duration = 25  # 默认专注时间为25分钟
    print("请输入专注时间长度（分钟）：")
    input_duration = input()
    if input_duration.isdigit():
        duration = int(input_duration)
    else:
        print("输入无效，使用默认时间25分钟。")

    # 启动专注时钟线程
    threading.Thread(target=focus_clock, args=(duration,)).start()

    # 专注结束后提示用户
    time.sleep(duration * 60)
    print("专注时间结束，请休息一下！")

if __name__ == "__main__":
    main()
