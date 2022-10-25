import asyncio
from multiprocessing import managers
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message, MessageSegment
from nonebot.params import CommandArg, RawCommand
#from .drawer import get_token, get_taskId, get_img
from .writer import get_rst
from .limiter import limiter
from .config import wenxin_config
import wenxin_api

drawer = on_command("写作", aliases={'写作帮助', 'PARAGRAPH' , 'Summarization', 'zuowen', 'couplet', 'PARAGRAPH', 'novel', 'cloze'}, priority=5, block=True)

msgg = None

@drawer.handle()
async def _(matcher: Matcher, event: GroupMessageEvent, command = RawCommand(), args = CommandArg()):
    # 判断是否触发帮助 或 主题任务描述为空
    if  command == '写作帮助' or str(args).strip() == '': 
        help_msg = '当前支持 作文zuowen, 文案adtext, 摘要Summarization, 对联couplet, 自由问答PARAGRAPH, 小说novel, 补全文本cloze\n如: PARAGRAPH 疯狂星期四v我50'
        await matcher.finish(help_msg)
        return
    
    # 判断用户是否触发频率限制
    user_id = event.user_id
    managers = wenxin_config.wenxin_manager_list # 管理员列表(不触发冷却时间限制)
    if not limiter.check(user_id):
        left_time = limiter.left_time(user_id)
        await matcher.finish(f'别急是一种人生态度。再等待{left_time}秒再找我罢！冷却期间可临时到网页（https://wenxin.baidu.com/moduleApi/ernie3）进行体验哦')
        return 
    
    # 启动写作任务
    command_str = str(command)
    style = 'PARAGRAPH' # 写作时style默认为PARAGRAPH
    style_list = ['PARAGRAPH' , 'zuowen','adtext', 'Summarization', 'novel', 'couplet', 'novel', 'cloze']
    for keyword in style_list:
        if keyword in command_str:
            style = keyword
            break  
    text = str(args) # 绘画的任务描述文字
    await matcher.send(f'飞桨文心AI开始写作主题为“{text}”的{style}(预计2-5分钟)...')
    
    try:
        text_output = await get_rst(text,512,0.8,8,1.2,style)

        if not str(user_id) in managers: 
            limiter.start_cd(user_id) # 启动冷却时间限制
          
        
        await asyncio.sleep(30) # 模型画画大概要30秒，等待一会儿
        
        
        
        
        if text_output == None:
            await matcher.finish(f'无法写出主题为“{text}”的{style}!')
            return
        
        #image_count = wenxin_config.wenxin_image_count # 每次发送的图片数量
        ## 判断图片数量是否少于配置的图片数量
        #if len(images) < image_count:
        #    image_count = len(images)
            
        msg = Message(f'文心ERNIE 3.0：主题为“{text}”的{style}') 
        await matcher.send(msg)
        #msg += MessageSegment.image(images['image'])
        msg = Message(text_output)        
        await matcher.finish(msg)
        
    except Exception as e:
        print(e)