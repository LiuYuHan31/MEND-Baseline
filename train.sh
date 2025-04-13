export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
python3 train_vllm_editor.py \
    -en mend_vl \
    -mn llava-v1.5-7b \
    -dna VLKEB \
    -bs 1 \
    -dvc "cuda:3" \
    -edvc 1 \
    -dn 1 \
    -lkpt None \
    -tnp VLKEB \
    -eps 100 \
    -sci 500 \
    -dbs 2
