#!/bin/bash
echo "$(date) - Running /env_config.py"
/env_config.py

echo "$(date) - Starting rsyslog"
/etc/init.d/rsyslog start && tail -f /dev/null
