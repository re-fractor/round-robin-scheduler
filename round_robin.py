from typing import List, NamedTuple


class Proc(NamedTuple):
    proc_id: int
    arrival_time: int
    burst_time: int


class CompletedProc(NamedTuple):
    proc_id: int
    arrival_time: int
    completion_time: int


time_slice = int(input("Enter Time Slice : "))
procs: List[Proc] = []
idx = 1
while True:
    command = input(
        "Enter 'q' or 'Q' to stop input of processes or 'a' or 'A' to add one : ").capitalize()
    if command == "Q":
        break
    elif command != "A":
        print("No Command Entered!")
        continue
    print("Adding Process...")
    arrival_time = input("Enter Arrival Time : ")
    burst_time = input("Enter Burst Time : ")
    if not (arrival_time.isdigit() and burst_time.isdigit()):
        print("Arrival Time or Burst time is not a digit!")
        continue
    print(
        f"Added Process {idx} to queue, with burst time = {burst_time} and arrival time {arrival_time}")
    procs.append(Proc(idx, int(arrival_time), int(burst_time)))
    idx += 1

print("sorting Procs by Arrival Time (Not Changing Their IDs)")
procs.sort(key=lambda x: x.arrival_time)
for proc in procs:
    print(proc)
completed_procs: List[CompletedProc] = []
last_end = 0
switch = True
while switch:
    new_procs: List[Proc] = []
    for proc in procs:
        # print(f"Processing {proc}")
        if proc.burst_time > time_slice:
            new_proc = Proc(proc.proc_id, proc.arrival_time,
                            burst_time=proc.burst_time-time_slice)
            last_end += time_slice
            new_procs.append(new_proc)
        else:
            last_end += proc.burst_time
            new_proc = CompletedProc(
                proc.proc_id, proc.arrival_time, completion_time=last_end)
            print(f"Completed Process {new_proc}")
            completed_procs.append(new_proc)
    if new_procs:
        procs = new_procs
    else:
        switch = False
        continue
print(f"All Processes Completed in {last_end} seconds!")
print("Order of Completion :")
for proc in completed_procs:
    print("\t", proc)
