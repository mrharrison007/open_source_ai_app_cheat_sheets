# Text Gen Web UI LLMs for API

LLMs I found that work with the Text Generation Web UI "API" out of the box with no other tweaking.
LLMs that span one GPU, the API works, LLMs that span two GPUS, API does not work.

System:
Proxmox 8 Host
Ubuntu 22.04 Server VM Guest
	64GB RAM
	2 x 3090s 24Gb VRAM each (48 Total)

CUDA/Nvidia:
Cuda compilation tools, release 12.3, V12.3.107
Nvidia Driver Version: 545.23.08    CUDA Version: 12.3



## API Does Work (GUI Chat Also):

1. TheBloke_Llama-2-7B-Chat-GPTQ
2. ehartford_dolphin-2.0-mistral-7b
3. MaziyarPanahi_dolphin-2.1-mistral-7b-GPTQ
4. TheBloke_Wizard-Vicuna-7B-Uncensored-GPTQ
5. TheBloke_Wizard-Vicuna-30B-Uncensored-GPTQ
6. TheBloke_vicuna-7B-v1.3-GPTQ
7. TheBloke_Nous-Hermes-2-SOLAR-10.7B-GPTQ
8. TheBloke_SOLAR-10.7B-Instruct-v1.0-GPTQ
9. TheBloke_Llama-2-13B-chat-GPTQ
10. TheBloke_vicuna-33B-GPTQ



## API Does NOT Work (GUI Chat DOES Work):

1. TheBloke_llama2_70b_chat_uncensored-GPTQ
2. TheBloke_guanaco-65B-GPTQ
3. TheBloke_MoMo-70B-V1.1-GPTQ
4. TheBloke_CodeLlama-70B-hf-GPTQ
5. TheBloke_CodeLlama-70B-Python-GPTQ
6. TheBloke_Mixtral-8x7B-Instruct-v0.1-GPTQ

