#!/bin/bash
ffmpeg -y -hide_banner -re -i https://kikageohls.akamaized.net/hls/live/2022693/livetvkika_de/master.m3u8 -codec: copy kika.mp4 &
sleep 630
killall ffmpeg
ffmpeg -y -i kika.mp4 -filter:v fps=23 -vf scale=240:-2 comp.mp4
