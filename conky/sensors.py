#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os, sys
import subprocess
 
# Empty dictionary
output = [] 
 
# ----------------------------------------------------------------------
 
cmd1= ['sensors']
cmd1_out = subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
cmd1_final = cmd1_out.strip().split('\n')
 
for line in cmd1_final:
    if 'Adapter' in line: 
        line = ''
        next
    if ':' in line:
        key = str(line.split('(', 1)[0].split(':')[0].strip().ljust(20))
        value = str(line.split('(', 1)[0].split(':')[1].strip())
        output.append( '%s %s' % ( key, value ))
 
# ----------------------------------------------------------------------
# 
output.append(str(' '))
#
# ----------------------------------------------------------------------
 
cmd2 = ['/usr/bin/nvidia-smi', '--query-gpu=temperature.gpu,fan.speed', '--format=csv,noheader']
cmd2_out = subprocess.Popen(cmd2, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
cmd2_final = cmd2_out.strip().replace(' ', '').split(',')
 
key = str('GPU Temperature').ljust(20)
value = str(cmd2_final[0])
output.append('%s %s°C' % ( key, value ))
 
key = str('GPU FAN Speed').ljust(20)
value = str(cmd2_final[1])
output.append('%s %s' % ( key, value ))
 
# ----------------------------------------------------------------------
# 
output.append(str(' '))
#
# ----------------------------------------------------------------------
for value in output:
    print('%(lang)s' % { 'lang': str(value) })
