#!/usr/bin/env python

import sys
from openpyxl import load_workbook
wb = load_workbook(sys.argv[1], read_only=True);
import json

ws = wb['Modes A-F']

bl = dict()
header = 1
for row in ws.rows:
    axis = dict()
    if str(row[0].value) == 'Instrument':
        header = 0
        continue
    if header == 1: continue
    alias         = row[2].value
    if 'feslits' in alias: continue
    axis['PV']    = row[1].value
    axis['desc']  = row[3].value
    axis['A']     = row[4].value
    axis['A_REP'] = row[5].value
    axis['B']     = row[6].value
    axis['B_REP'] = row[7].value
    axis['C']     = row[8].value
    axis['C_REP'] = row[9].value
    axis['D']     = row[10].value
    axis['D_REP'] = row[11].value
    axis['E']     = row[12].value
    axis['E_REP'] = row[13].value
    axis['F']     = row[14].value
    axis['F_REP'] = row[15].value
    bl[alias] = axis
    
print json.dumps(bl, sort_keys=True,
                 indent=4, separators=(',', ': '))
