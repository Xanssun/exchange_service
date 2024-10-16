#!/bin/bash

alembic -c /opt/app/alembic.ini revision --autogenerate -m "add migrations" &&
alembic -c /opt/app/alembic.ini upgrade head &&
python3 /opt/app/main.py
