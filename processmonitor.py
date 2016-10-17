import sys
import psutil
import time


# This module requires psutil python package please run the below 
# command to install the package
#
#     pip install psutil
#
# This can be used as a module as show below
#
# import processmonitor
#
# processmonitor.timeProcess(process_id, process_threshold)
#
# or as a command line tool as below
#
# python processmonitor.py process_id, process_threshold


def filterProc(interval, proc_id):
    '''
    filter and return the proc object for the specific process id
        :Parameters:
            interval: time gap to query the process, usually 1 sec is a
                       good one

            proc_id: Process ID
    '''
    time.sleep(interval)
    procs = []
    procs_status = {}
    for p in psutil.process_iter():
        if p.pid == proc_id:
            procs.append(p)

    return procs

def timeProcess(proc_id, procTreshold):
    '''
    Given a process id and process threshold this will give a time 
    used by the process
        :Parameters:
            proc_id: Process ID

            procTreshold: percentage of cpu usage, time will be calculated
                          only if the cpu percentage is above threshold
    '''
    startTime= time.time()
    timeElapsed = None
    while psutil.pid_exists(proc_id):
        try:
            process = filterProc(1, proc_id)[0]
            if process.cpu_percent() > procTreshold:
                end = time.time()
                timeElapsed = (time.time() - startTime)
        except IndexError:
            return timeElapsed

    return timeElapsed



if __name__=='__main__':
    procid = int(sys.argv[1])
    tresh = float(sys.argv[2])
    print timeProcess(procid, tresh)
