import time
import os
class time_handler:
    def __init__(self,time,action,num):
        self.time=time
        self.action=action
        self.num=num
#The basic class whose list will serve as event handler_list
#time is a particular time instant may be start time or end time for a subtitle display
#action a boolean which is start time if true end time if false
#num is counter of subtitle
def time_giver(s):
    tstr=s.split()
    ststr=tstr[0]
    st=((3600 * int(ststr[0:2])) + (60 * int(ststr[3:5]) + int(ststr[6:8]) + (.001 * float(ststr[9:]))))
    enstr=tstr[2]
    et=((3600 * int(enstr[0:2])) + (60 * int(enstr[3:5]) + int(enstr[6:8]) + (.001 * float(enstr[9:]))))
    return (st,et)
#takes a string which is the timestamp and returns a Tuple --> (start time,end time)
def printer(l):
    for i in l:
        for j in i[2:]:
            print(str(j))
#take a list of list (here it will be used to print subtitles lines i.e. the third line onwards)
start=time.time()
with open("lyrics.srt","r") as file:
    data=file.readlines()
#-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
counter=0
l=[[]]
for i in data:
    if i != '\n':
        l[counter].append(i)
    else:
        l.append([])
        counter=counter+1
l=l[:counter]
#this snippet reads every line in srt filr and creates a superlist
#each sublist contains subtitle i.e. counter timestamp and subtitle
#-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
handler_list=[]
number=1
for i in l:
    time_tuple=time_giver(i[1])
    handler_list.append(time_handler(time_tuple[0],True,number))
    handler_list.append(time_handler(time_tuple[1],False,number))
    number+=1
handler_list.sort(key=lambda x: x.time, reverse=False)
#This snippet populates handler_list i.e. is a list of event triggers
#last line sorts time events in ascending order
#-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
printable=[]
for i in handler_list:
    if (time.time()-start)<i.time:
        time.sleep(i.time-(time.time()-start))
        os.system('clear')
    if i.action:
        printable.append(l[i.num-1])
    else:
        printable.remove(l[i.num-1])
    printer(printable)
#printable is a superlist which contains subtitle sublist that is to diplayed in that time duration
#if i.action is true it adds a subtitle while removes particular subtitle if false
#-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
