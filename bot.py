#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
import re
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot import on_message
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State

# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

nonebot.load_builtin_plugins("echo")

# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins
nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...


fkqq = on_message(priority=1, block=False)


@fkqq.handle()
async def fuck_tencent(bot: Bot, event: Event):
    if event.get_message().extract_plain_text() == "每日一问":
        pass
    else:
        await fkqq.finish()
    message = MessageSegment.text("腾讯今天死了吗？")
    print(event.get_session_id())
    user_id = event.get_user_id()
    if event.get_session_id().find("group") == 0:
        str1 = event.get_session_id()
        splited = str1.split('_')
        group_id = splited[1]
    await fkqq.finish(message=message)


if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
