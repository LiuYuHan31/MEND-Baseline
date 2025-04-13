# LiveEdit

Source code for CVPR paper [Lifelong Knowledge Editing for Vision Language Models with Low-Rank Mixture-of-Experts](https://arxiv.org/abs/2411.15432)



# Setup
1. Please download the MMEdit datasets from the URL provided in [1] and place the related folders in the `data/easy-edit-mm` directory.
MMEdit的地址在 https://github.com/zjunlp/EasyEdit
这里面可以下载数据集和images

2. Please download the VLKEB dataset from the URL provided in [2] and place the related folders in the `data/VLKEB` directory.
VLKEB的地址在https://github.com/VLKEB/VLKEB
通过kaggle的api很容易下载到服务器

3. Please modify the `ROOT_PATH` in `utils/GLOBAL.py` to the absolute path of the current directory, and update `model_path_map` to the absolute paths of each backbone's weights.

这里需要下载LLAVA-1.5-7B的模型，在huggingface上很容易下载
https://huggingface.co/llava-hf/llava-1.5-7b-hf

# Train editors
Please follow the script below to train an editor that requires training:

`python train_vllm_editor.py -en liveedit -mn blip2 -dna EVQA -bs 8 -dvc "cuda:0" -edvc 0 -lkpt None -tnp EVQA -eps 50 -sci 500`

# Evaluate editors
Please follow the script below to evaluate the editors. If an editor does not require training, please set `-ckpt` to `None`."

`python test_vllm_edit.py -en "liveedit" -mn "blip2" -sen 1000 -dvc "cuda:0" -dn "EVQA" -ckpt "records/liveedit/blip2-opt-2.7b/EVQA/checkpoints/ckpt"`




# Reference
[1] Can We Edit Multimodal Large Language Models? EMNLP 2023

[2] VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark. NeurIPS 2024, Datasets and Benchmarks Track
