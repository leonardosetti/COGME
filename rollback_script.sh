#!/bin/bash
# Restore from checkpoint
if [ -d "/lab/FATEC/202602/ger_proj/COGME/checkpoints/latest" ]; then
    cp -r /lab/FATEC/202602/ger_proj/COGME/checkpoints/latest/* /lab/FATEC/202602/ger_proj/COGME/artifacts/
fi
# Reset config
cp /lab/FATEC/202602/ger_proj/COGME/config_backup.json /lab/FATEC/202602/ger_proj/COGME/config.json