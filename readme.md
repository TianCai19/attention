# 视频帧提取脚本

本项目包含一个 Python 脚本，用于从视频中提取帧并保存为图片。

## 主要功能

- 遍历 `video` 文件夹中的所有视频文件。
- 为每个视频创建一个同名的子文件夹，并将提取的帧保存到该子文件夹中。
- 支持 `mp4`、`avi`、`mov` 等常见视频格式。
- 每隔设定的秒数提取一帧图片，默认每 2 秒提取一帧。

## 依赖项

在运行脚本之前，请确保已安装以下依赖项：

- Python 3.x
- OpenCV

可以通过以下命令安装 OpenCV：

```sh
pip install opencv-python
```

## 使用方法

1. 将要处理的视频文件放到 `video` 文件夹中。
2. 运行脚本 `video_frame_extraction.py`：

```sh
python video_frame_extraction.py
```

3. 提取的帧将保存到 `picture` 文件夹中，每个视频的帧会保存在同名的子文件夹中。

## 参数调整

- `extract_interval_seconds`：控制每隔多少秒提取一张图片，默认为 2 秒。可以根据需要修改该值。

## 注意事项

- 如果某个视频已经提取过帧，脚本会跳过该视频，并在终端输出相应提示。
- 请确保 `video` 和 `picture` 文件夹存在于脚本所在目录，或修改脚本中的路径。

## 示例输出

```
跳过 'example_video'，因为该视频已经处理过了。
保存 picture/example_video/frame_0.jpg
保存 picture/example_video/frame_60.jpg
...
视频 'example_video' 的帧提取完成。
所有视频的处理已完成。
```

