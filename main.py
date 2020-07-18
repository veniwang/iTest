#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time,socketserver,struct,os,json
from socket import *

def is_first_for_quesion(inLine) :
    # print('helo')
    rv = False
    q_line = inLine.split('.',1)
    if len(q_line)>1 :
        if q_line[0].isdigit():
            rv = True
    return rv

def fmt_quesion(inLine):
    newLine = ""
    #
    head = "\t],\n\
            \tK:''\n\
            },\n\
            {\n\
	        \tQ:'"
    #
    tail = "',\n\
	        \tC:["
    newLine = head + inLine.rstrip() + tail
    return newLine

def fmt_choice(inLine):
    head = "\t'"
    tail = "',\n"
    newLine = head + inLine.rstrip() + tail
    return newLine

def fmt_first_line(inLine):
    head = "{\n\
	        \tQ:'"
    tail = "',\n\
	        \tC:["
    newLine = head + inLine.rstrip() + tail
    return newLine

def fmt_last_line():
    line = "\n\t],\n\tK:''\n\t\t}"
    return line

if __name__ == "__main__":
    srcFile = input('please input src file path:')
    fldFile = os.path.dirname(__file__)
    if len(fldFile) > 0:
        srcFile = fldFile + "/" + srcFile
    # print(srcFile)
    tgtFile = srcFile + '.js'
    # print(tgtFile)
    with open(srcFile,encoding='utf-8') as fr, open(tgtFile,'w',encoding='utf-8') as fw:
        fw.write("var obj={\n\tTB:[\t\n\t")
        #spec handle in first line.
        fw.write(fmt_first_line(fr.readline()))
        #
        while 1:
            line = fr.readline()
            if not line:
                fw.write(fmt_last_line())
                break
            newLine = ""
            if is_first_for_quesion(line):
                newLine = fmt_quesion(line)
            else:
                newLine = fmt_choice(line)
            fw.write(newLine)
        fw.write("\n\t]\n}\n")
    print('done.')
        
