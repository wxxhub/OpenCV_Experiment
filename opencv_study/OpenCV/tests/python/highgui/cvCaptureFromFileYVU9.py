#! /usr/bin/env python
"""
This script will test highgui's video reading functionality
for RAW YVU9 .avi files
"""

# pixel format to check
FORMAT   = "YVU9"

# import check routine
import cvCaptureFromFile

# check video file of format FORMAT,
# the function also exits and returns
# 0,1 or 77 accordingly.

cvCaptureFromFile.video_ok(FORMAT)
