# coding: utf-8
file = open("out.txt", "w")
for line in open("sample.txt", "r"):
    tmp = ""
    for word in line.split():
        tmp += word
    file.write(tmp + "\n")