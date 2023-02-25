#!/bin/bash

ping google.com | while read pong; do echo "$(date): $pong"; done | tee -a ./logs/output_pinglog.txt
