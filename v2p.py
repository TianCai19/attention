import cv2
import os

# 定义视频文件夹和输出文件夹路径
video_dir = 'video'  # 存放视频文件的文件夹
output_dir = 'picture'  # 保存图片的文件夹

# 如果输出文件夹不存在则创建
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 获取视频文件夹中的所有视频文件
video_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4') or f.endswith('.avi') or f.endswith('.mov')]

# 定义每隔多少秒提取一张图片
extract_interval_seconds = 2  # 可以修改为需要的秒数

# 处理每个视频文件
for video_file in video_files:
    video_path = os.path.join(video_dir, video_file)
    video_name = os.path.splitext(video_file)[0]  # 获取视频名称（不包含扩展名）
    video_output_dir = os.path.join(output_dir, video_name)  # 针对每个视频创建同名的子文件夹

    # 如果该视频已经分割过了，则跳过
    if os.path.exists(video_output_dir):
        print(f"跳过 '{video_name}'，因为该视频已经处理过了。")
        continue

    # 创建输出子文件夹
    os.makedirs(video_output_dir)

    # 读取视频文件
    cap = cv2.VideoCapture(video_path)

    # 获取视频的帧率 (frames per second)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = 0

    # 计算保存每隔多少帧提取一张图片
    interval = fps * extract_interval_seconds

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 每隔interval帧保存一次图片
        if frame_count % interval == 0:
            img_path = os.path.join(video_output_dir, f'frame_{frame_count}.jpg')
            cv2.imwrite(img_path, frame)  # 保存图像
            print(f"保存 {img_path}")

        frame_count += 1

    # 释放视频资源
    cap.release()
    print(f"视频 '{video_name}' 的帧提取完成。")

print("所有视频的处理已完成。")
