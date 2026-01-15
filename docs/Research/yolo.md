# 实验备忘

```bash
tmux new -s xinli 
```

- tmux 创建工作区，关掉电脑也会继续运行
- 返回：

```bash
tmux ls # 可以看到当前的目录
tmux attach -t lixin
# 在对话里面结束
tmux kill-session
```
## 创建虚拟环境

```bash
conda create -n yolov11_env python=3.9
conda activate yolov11_env
```

## 下载正确的pytorch

- 查看cuda版本：

```bash
nvidia-smi | less
```

这样就能停留在第一行，就有cuda版本了。

查阅官网 https://pytorch.org/get-started/locally/ 

```bash
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
```

## Yolo 环境配置

```bash
pip install ultralytics
conda install jupyter notebook
```

new file: train.ipynb

select kernel: 选择之前创建的环境：

![](Pasted%20image%2020250912232206.png)

## 命令行

```bash
# 1. 回到根目录
cd / 
# 2. 将 ~/mydocs 目录下的所有非隐藏文件和子目录移动到 ~/backup 目录 
mv ~/mydocs/* ~/backup/
# 3. 删掉yolov11目录
rmdir yolov11
```


## 查看目前卡的占用情况

```bash
pip install nvitop
```

输入nvitop查看当前服务器卡的占用情况，可以看到当前哪些卡是空的，然后调整你的device 或者 CUDA_VISIBLE_DEVICES=4 python main.py

## 上传文件

1. scp:
```bash
scp /path/to/image.jpg username@ip:/path/to/image.jpg
```

2. sftp

## 下载huggingface数据集

hfd下载可以看这篇，不过我是curl -o hfd.sh "https://gist.githubusercontent.com/padeoe/697678ab8e528b85a2a7bddafea1fa4f/raw/ee66e007ee84f479487c25a21715768884a426f5/hfd.sh" 直接结束

