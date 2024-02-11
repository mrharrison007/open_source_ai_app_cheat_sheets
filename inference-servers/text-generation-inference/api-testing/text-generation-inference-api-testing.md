# Text Generation Inference - Testing

## System:

Proxmox 8 Host
Ubuntu 22.04 Server VM Guest
	64GB RAM
	2 x 3090s 24Gb VRAM each (48 Total)

## CUDA/Nvidia:

Cuda compilation tools, release 12.3, V12.3.107
Nvidia Driver Version: 545.23.08    CUDA Version: 12.3

## Startup Examples That Worked

```
docker run --gpus all --shm-size 1g -p 8080:80 -v /mnt/data1_iscsi/models/tgi:/data ghcr.io/huggingface/text-generation-inference:1.4 --model-id HuggingFaceH4/zephyr-7b-beta

docker run --gpus all --shm-size 1g -p 8080:80 -v /mnt/data1_iscsi/models/tgi:/data ghcr.io/huggingface/text-generation-inference:1.4 --model-id tiiuae/falcon-7b-instruct

docker run --gpus all --shm-size 1g -p 8080:80 -v /mnt/data1_iscsi/models/tgi:/data ghcr.io/huggingface/text-generation-inference:1.4 --model-id TheBloke/falcon-40b-instruct-GPTQ --quantize=gptq --sharded true --num-shard 2

docker run --gpus all --shm-size 1g -p 8080:80 -v /mnt/data1_iscsi/models/tgi:/data ghcr.io/huggingface/text-generation-inference:1.4 --model-id TheBloke/llama2_70b_chat_uncensored-GPTQ --quantize=gptq --sharded true --num-shard 2
```



### Successful API Testing with:

1. HuggingFaceH4/zephyr-7b-beta
2. models--tiiuae--falcon-7b-instruct
3. TheBloke/falcon-40b-instruct-GPTQ
4. TheBloke/llama2_70b_chat_uncensored-GPTQ

