#!/usr/local/bin/python
import psutil
from sys import argv

cputimes = psutil.cpu_times()
virtmem = psutil.virtual_memory()
swap = psutil.swap_memory()

if len(argv) < 2:
        print "Please enter one of the parameters 'mem' or 'cpu'"
	exit()
elif len(argv) > 2:
	print "Please enter only one parameter!"
        exit()

script, value = argv


if 'cpu' in value:
	print'CPU Metrics'
	print'Sammpe output:'
	print'cpu.idle =', cputimes.idle
	print'cpu.user =', cputimes.user
	print'cpu.guest =', cputimes.guest
	print'cpu.iowait =', cputimes.iowait
	print'cpu.stolen =', cputimes.steal
	print'cpu.system =', cputimes.system
elif 'mem' in  value:
        print'MEM metric'
	print 'Sample output:'
	print'virtual total =', virtmem.total
	print'vitrual used =', virtmem.used
	print'virtual free =', virtmem.free
	print'virtual shared =', virtmem.shared
	print'swap total =', swap.total
	print'swap used =', swap.used
	print'swap free =', swap.free	
else:
        print"Input error, please enter a valid argument, 'mem' or 'cpu'"
