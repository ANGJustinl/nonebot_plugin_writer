<div align="center">

# nonebot_plugin_writer

✨ 基于 百度文心大模型 的 NoneBot2 promote索引文字生成插件 ✨

</div>

<p align="center">

<img src="https://img.shields.io/badge/python-3.10-blue.svg" alt="python">
<img src="https://img.shields.io/badge/Onebot-v11-lightgrey" alt="onebot11">
<img src="https://img.shields.io/badge/nonebot-2.0.0b4-orange" alt="nonebot2">
<img src="https://img.shields.io/github/last-commit/ANGJustinl/nonebot_plugin_writer.svg?label=Updated&logo=github&cacheSeconds=600" alt="AABT">   
<img src="https://github.com/ANGJustinl/nonebot_plugin_writer/total.svg?label=Downloads&logo=github&cacheSeconds=600" alt="nonebot_plugin_writer">  
</p>  
  
[修改自 nonebot-plugin-drawer](https://github.com/CrazyBoyM/nonebot-plugin-drawer) 同时给我提供了非常多的思路

[百度文心大模型] https://wenxin.baidu.com/moduleApi/ernie3



    一切开发旨在学习，请勿用于非法用途
    
    侵权联系angjustin@163.com
    
    
### 前提: nonebot2的部署

[nonebot2 官方] https://nb2.baka.icu/

[昂昂bot的安装流程] https://github.com/ANGJustinl/ANGANGBOT/edit/main/README.md

[带佬提供的教程] https://zhuanlan.zhihu.com/p/371264976

---

    | 使用未在其他环境编译的插件可能会遇到各种花里胡哨的麻烦，如果没有一些基础的话，前面可是困难重重啊少年
    
    | 本文内容请您自行判断是否可信可靠可用，若您根据本文内容建立和使用AABT时出了任何问题和不良结果，鄙人概不负责。
    
---

## | 安装流程 🚀

### Ⅰ.通过nb-cli安装（推荐）
```
nb plugin install nonebot-plugin-drawer
```
### Ⅱ.通过pip安装
```
1.pip install nonebot-plugin-writer 进行安装  
2.在bot.py添加nonebot.load_plugin('nonebot_plugin_writrer')
```
### Ⅲ.配置env.*
请在env.*配置文件中加入如下几行
```
wenxin_ak = "xxxxxxxxxxxxxxxx"
wenxin_sk = "xxxxxxxxxxxxxxxx"
wenxin_cd_time = 300 # 技能冷却时间，以秒为单位
wenxin_manager_list = ["123456789", "98765432"] # 管理员列表(不触发冷却时间限制)
```
文心的ak和sk申请链接：https://wenxin.baidu.com/younger/apiDetail?id=20008



## | 使用方法（仅支持群聊）
触发菜单命令：写作帮助

当前支持 作文zuowen, 文案adtext, 摘要Summarization, 对联couplet, 自由问答PARAGRAPH, 小说novel, 补全文本cloze
如: PARAGRAPH 疯狂星期四v我50




## | 非常重要的配置(动手能力强者自改)

详见插件安装目录

[nonebot_plugin_writer/writer.py]中20至30行

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

此段为文心模型input内容

具体命令及其用法详见 __https://wenxin.baidu.com/wenxin/docs#dl6tgxw5f__

可根据任务需求进行配置





## | 👥反馈与交流

Issue for sure

QQ:77139032

群聊:696748432

<a target="_blank" href="https://qm.qq.com/cgi-bin/qm/qr?k=v4YpojQK_Ginr8S3Ies_jwwKrU-ZzA_m&jump_from=webapi&authKey=wZ/DxqcHHPGuTfBSAhpqzOo3/oiX0iojBCLq9qFymK+daTfwfmZNAoQrKIH+o8N0"><img border="0" src="//pub.idqqimg.com/wpa/images/group.png" alt="ANGANGBOT研磨会" title="ANGANGBOT研磨会"></a>

mail:angjustin@163.com

bilibili:https://space.bilibili.com/213993950?spm_id_from=333.1007.0.0
