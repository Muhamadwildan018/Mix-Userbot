"""
RadioPlayerV3, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re
import ffmpeg
import asyncio
import subprocess
from config import Config
from signal import SIGINT
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from pyrogram import Client, filters, emoji
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR


msg={}
playlist=[]
durasi_musik