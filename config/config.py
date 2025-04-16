
# Copyright (C) 2021-2022 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
Alexa is a Telegram Audio and video streaming bot 
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "29772838"))
API_HASH = getenv("API_HASH", "15ce514f4f3fcea70d7a49dc5064b839")

BOT_TOKEN = getenv("BOT_TOKEN", "7563580567:AAHdItwB78m3OBWJ8SdbfpiRv5TWQMO0h7k")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG = True  # veya False, loglama açıksa True olmalı
LOG_GROUP_ID = -1001234567890  # botun log mesajlarını atacağı grup ID'si

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "kumsal")

OWNER_ID = int(getenv("OWNER_ID", "7268753735"))

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

BOT_ID = getenv("BOT_ID", "7563580567")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/saymen930/Alexa")

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/the_team_kumsal")

SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/kumsalmuzikk")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "3400"))

AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "False")

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "False")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/kumsalfed6301/Kumsal-muzik-bot")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "2"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "7"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes


STRING1 = getenv("STRING_SESSION", "BAGuj-4AUE6oDTLC_i2xRwar1ErMg0wz6bSesAoiVWBfI9UeuoIxz87hWorVWExPlx_FIcoq5SNtSj45SNUFPzFZhAkplD1ABo7GjEAtv-Bfr3ffNc7NbNT_xHwc9tw5Zwwo9LcRYyugTxwWNKj7XRxLWjJL2Oc6MAMVN8PdEiDqayAJj6njYemWUZ0OIEMqHLt5b0zn9gBMSbdg1Obro6hnT7p8QT04KYzN8XnZ1sUjehPpdKC4apAWoT1P6l7vLdx51IvYfb3wDDefCJutWf-oWK8bujbIFjQFwrmlWYjjW-GC_Q69SWzyvP60d0tEteKvBkoOJRD-zCL4SVFYOd3ea3JtDgAAAAHNDSwcAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://ibb.co/YFD02YDY"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://ibb.co/YFD02YDY"
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", None
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL", "https://envs.sh/5hH.jpg"
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", None
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL", "https://envs.sh/5hH.jpg"
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL", "https://envs.sh/5hH.jpg"
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL", "https://envs.sh/5hH.jpg"
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL", "https://envs.sh/5hH.jpg"
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL", "https://envs.sh/5hH.jpg"
)


SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://envs.sh/5hH.jpg"
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://envs.sh/5hH.jpg"
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://envs.sh/5hH.jpg"
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )


if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
