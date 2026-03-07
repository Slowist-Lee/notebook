> For HKUST Interview

# 实验记录
## 1. Set up the Env.

白嫖组里的服务器，输入 `nvidia-smi`：

| **硬件/系统信息**                | **详细内容**                                 |
| -------------------------- | ---------------------------------------- |
| **GPU Model (显卡型号)**       | 4x NVIDIA GeForce RTX 5090 (每张约 32GB 显存) |
| **Driver Version (驱动版本)**  | 580.126.09                               |
| **CUDA Version (CUDA 版本)** | 13.0                                     |

配相关环境：

```bash
conda create -n vllm_env python=3.10 -y
conda activate vllm

pip install vllm
pip show vllm | grep Version
```

得到 vllm 0.16.0

下载llama-3：
1. 下载ollama： 师兄发我了 https://github.com/ollama/ollama/issues/2111
后台跑
./bin/ollama serve& 

然后拉取用：
../ollama/bin/ollama pull llama3.1

需要设置一下镜像

```json
{
    "registry": {
        "mirrors": {
            "registry.ollama.ai": "https://ollama.zju.edu.cn"
        }
    }
}
```

## 2. Task1：完成一次推理

发现 llama3.1 8B还是得全拉下来，所以改用Google Cloud（还是不行，改用AutoDL了

先检查一下是否满足条件：

1. 充值几块钱，选好 **24G RTX40系** 和 **vLLM 镜像**，点击“立即部署”。
    
2. 开机后打开终端（Terminal），**不要急着去下载几十个 G 的模型**。
    
3. 第一时间输入以下命令测试是否有修改频率的权限：
    
    - 先开启持久模式：`sudo nvidia-smi -pm 1`
        
    - 随便锁一个频率试试：`sudo nvidia-smi -lgc 1000,1000`
        
4. **如果执行成功：** 恭喜你，今晚作业稳了！直接用 `sudo nvidia-smi -rgc` 恢复频率，然后开始下模型做 Task 1 吧。
    
5. **如果报错（Permission denied / Not supported）：** 说明容器环境锁了权限。这时候**立马关机并销毁实例**（最多扣你几毛钱）。然后回到图里这个界面，往下划，选择 **“系统镜像 -> Ubuntu”**。系统镜像通常是完整的虚拟机（VM），拥有绝对的底层硬件控制权，肯定能锁频率（只是你需要自己花十分钟 `pip install vllm` 配置一下环境）。