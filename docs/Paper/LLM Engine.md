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

发现 llama3.1 8B还是得全拉下来，所以改用Google Cloud



