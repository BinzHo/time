import time

def focus_timer(total_time, focus_interval, break_interval):
    while total_time > 0:
        print(f"专注倒计时: {total_time // 60} 分钟 {total_time % 60} 秒")
        time.sleep(1)
        total_time -= 1
        if total_time % focus_interval == 0:
            print("休息一下，放松一下眼睛和身体！")
            time.sleep(break_interval)

# 设置专注时长、专注间隔和休息时长（以秒为单位）
total_focus_time = 25 * 60  # 25分钟专注
focus_interval = 1500  # 1500秒（25分钟）
break_duration = 5 * 60  # 5分钟休息

focus_timer(total_focus_time, focus_interval, break_duration)
