#!/bin/bash

if [ ! -d "/venv" ]
then
    python3 -m venv venv
fi

venv/bin/pip install -r packages.txt

venv/bin/python game.py
