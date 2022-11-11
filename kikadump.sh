#!/bin/bash
ffmpeg -y -hide_banner -re -t 600 -i https://kikageohls.akamaized.net/hls/live/2022693/livetvkika_de/master.m3u8 -codec: copy kika.mp4
