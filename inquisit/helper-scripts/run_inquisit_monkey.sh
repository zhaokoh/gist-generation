#!/bin/bash

# Simple script to run Inquisit in Monkey Mode 
# See https://www.millisecond.com/support/docs/v5/html/howto/howtocommandline.htm for more details.

INQUISIT_PATH="/Applications/Inquisit 5.app/Contents/MacOS/Inquisit 5"
INQUISIT_SCRIPT="batch_V1_imgset_1_1_lb.iqx"

# Run in monkey mode (30 times - to match exactly the group required.)
for group in {1..30}
do
    "$INQUISIT_PATH" $INQUISIT_SCRIPT -s $group -g $group -m monkey
done