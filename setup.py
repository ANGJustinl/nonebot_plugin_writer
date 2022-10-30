import setuptools
import io
import os
import sys
from shutil import rmtree



with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

# Package meta-data.
NAME = 'nonebot_plugin_writer'
DESCRIPTION = '基于 百度文心大模型 的 NoneBot2 promote索引文字生成插件'
URL = 'https://github.com/ANGJustinl/nonebot_plugin_writer'
EMAIL = 'angjustin@126.com'
AUTHOR = 'ANGJustinl'
REQUIRES_PYTHON = '>=9.0.0'
VERSION = '0.2.1'

setuptools.setup(
    name="nonebot_plugin_writer",
    version="0.2.1",
    author="ANGJustinl",
    author_email="angjustin@126.com",
    keywords=["pip", "nonebot2", "nonebot", "nonebot_plugin"],
    description="""基于 百度文心大模型 的 NoneBot2 promote索引文字生成插件""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ANGJustinl/nonebot_plugin_writer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=[
        'httpx==0.23.0'
        'nonebot==1.9.1'
        'nb-cli>=0.6.7'
        'nonebot-plugin-apscheduler>=0.2.0'
        'nonebot-adapter-onebot>=2.1.4'
        'nonebot-plugin-apscheduler>=0.2.0'
        'nonebot-plugin-autohelp>=0.1.7'
        'nonebot-plugin-datastore>=0.4.0'
        'nonebot-plugin-heweather>=0.6.0'
        'nonebot-plugin-htmlrender>=0.1.1'
        'nonebot-plugin-localstore>=0.2.0'
        'pydantic==1.9.2'
        'setuptools==57.4.0'
        'wenxin_api==0.0.5.1'
        'toml>=0.10.2'
        'yarl>=1.8.1'
        'poetry>=1.2.2'
        'poetry-core>=1.3.2'
        'poetry-plugin-export>=1.1.2'
    ],
    python_requires=">=3.7.3"
)

'''如有报错使用如下
install_requires=[
        'nonebot-adapter-onebot>=2.0.0-beta.1',
        'nonebot2>=2.0.0-beta.1',
        'httpx>=0.23.0',
        'pillow>=8.2.0',
        'playwright>=1.22.0',
        'lxml>=4.8.0',
        'tencentcloud-sdk-python>=3.0.675',
        'aiofiles>=22.1.0'
        'async-timeout>=4.0.2'
        'syncio-dgram>=2.1.2'
        'APScheduler>=3.9.1'
        'aiocqhttp>=1.4.3'
        'aiocache>=0.11.1'
        'http-utils>=0.1.3'
        'httpcore>=0.15.0'
        'logger>=1.4'
        'Markdown>=3.4.1'
        'nb-cli>=0.6.7'
        'nonebot-plugin-apscheduler>=0.2.0'
        'nonebot-adapter-onebot>=2.1.4'
        'nonebot-plugin-apscheduler>=0.2.0'
        'nonebot-plugin-autohelp>=0.1.7'
        'nonebot-plugin-datastore>=0.4.0'
        'nonebot-plugin-heweather>=0.6.0'
        'nonebot-plugin-htmlrender>=0.1.1'
        'nonebot-plugin-localstore>=0.2.0'
        'nonebot2>=2.0.0rc1'
        'numpy>=1.23.4'
        'packaging>=21.3'
        'scipy>=1.9.2'
        'six>=1.16.0'
        'toml>=0.10.2'
        'tomlkit>=0.10.2'
        'tornado>=6.2'
        'tortoise-orm>=0.19.2'
        'utils>=1.0.1'
        'uvicorn>=0.18.3'
        'webencodings>=0.5.1'
        'websockets>=10.3'
        'wenxin-api>=0.0.5.1'
        'yarl>=1.8.1'
        'poetry>=1.2.2'
        'poetry-core>=1.3.2'
        'poetry-plugin-export>=1.1.2'
    ],
    '''