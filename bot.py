#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mastodon import Mastodon, StreamListener
import os
import creds
import datetime
import time

if not os.path.exists("clientcred"):
    Mastodon.create_app(
     "sandmannbot",
     api_base_url = creds.instance,
     to_file = "clientcred"
    )

mastodon = Mastodon(
    client_id = "clientcred",
    api_base_url = creds.instance
)

mastodon.log_in(
    creds.username,
    creds.password,
    to_file = "usercred"
)

os.system("bash kikadump.sh")

mastodon.status_post("", media_ids=mastodon.media_post("comp.mp4"))
