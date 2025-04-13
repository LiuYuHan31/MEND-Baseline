import datetime
import os
import threading

from huggingface_hub import hf_hub_url
from huggingface_hub.hf_api import HfApi
from huggingface_hub.utils import filter_repo_objects

# 执行命令
def execCmd(cmd):
    print("命令%s开始运行%s" % (cmd, datetime.datetime.now()))
    os.system(cmd)
    print("命令%s结束运行%s" % (cmd, datetime.datetime.now()))


if __name__ == '__main__':
    # 需下载的hf库名称
    repo_id = "Salesforce/blip2-opt-2.7b"
    # 本地存储路径
    save_path = './blip2-opt-2.7b'
    
    # 获取项目信息
    _api = HfApi()
    repo_info = _api.repo_info(
        repo_id=repo_id,
        repo_type="model",
        revision='main',
        token=None,
    )

    # 获取文件信息
    filtered_repo_files = list(
        filter_repo_objects(
            items=[f.rfilename for f in repo_info.siblings],
            allow_patterns=None,
            ignore_patterns=None,
        )
    )

    cmds = []
    threads = []

    # 需要执行的命令列表
    for file in filtered_repo_files:
        # 获取路径
        url = hf_hub_url(repo_id=repo_id, filename=file)
        # 断点下载指令
        cmds.append(f'wget -c {url} -P {save_path}')
    print(cmds)

    print("程序开始%s" % datetime.datetime.now())
    for cmd in cmds:
        th = threading.Thread(target=execCmd, args=(cmd,))
        th.start()
        threads.append(th)
    for th in threads:
        th.join()
    print("程序结束%s" % datetime.datetime.now())

