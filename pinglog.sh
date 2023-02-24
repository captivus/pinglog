#!/bin/bash

ping google.com | while read pong; do echo "$(date): $pong"; done | tee -a output_pinglog.txt
