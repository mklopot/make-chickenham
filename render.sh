#!/bin/bash

DPI=300
BORDERPX=40

inkscape -z $1 -d$DPI -e ${1%.*}.png
convert -colorspace Gray -channel RGB -negate -bordercolor white -border 0x$BORDERPX -flop ${1%.*}.png ${1%.*}-rendered.png 
