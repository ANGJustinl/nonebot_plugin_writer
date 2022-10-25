from statistics import mode
import httpx
from .config import wenxin_config
import asyncio
from multiprocessing import managers
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message, MessageSegment
from nonebot.params import CommandArg, RawCommand
import wenxin_api # 可以通过"pip install wenxin-api"命令安装

from wenxin_api.tasks.text_generation import TextGeneration


wenxin_api.ak = wenxin_config.wenxin_ak
wenxin_api.sk = wenxin_config.wenxin_sk


# 获取绘画的结果
async def get_rst(input_text,input_len_max,input_topp,input_len_min,input_penalty,input_mode):
    input_dict = {
        "text": input_text,
        "seq_len": 512,
        "topp": 0.8,
        "penalty_score": 1.2,
        "min_dec_len": 128,
        "is_unidirectional": 0,
        "task_prompt": input_mode,
        "logits_bias": "-5"
    }
    try:
        rst = TextGeneration.create(**input_dict)
        #print(rst)
    except:
        return None
    
    return str(rst)
