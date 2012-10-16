#!/usr/bin/python
def mil(mm):
	return int(mm*1000/25.4)
connector = {
1 : ["O", "Fuel pump relay control"],
2 : ["O", "Idle speed control valve"],
3 : ["O", "Fuel injector control, cyl. 1"],
4 : ["O", "Fuel injector control, cyl. 3"],
5 : ["O", "Fuel injector control, cyl. 2"],
6 : ["P", "Ground"],
7 : ["vacant", "-"],
8 : ["O", "Check engine"],
9 : ["vacant", "-"],
10 : ["vacant", "-"],
11 : ["O", "Throttle valve position (load signal to transmission control module)"],
12 : ["I", "Throttle position sensor"],
13 : ["O", "Mass air flow sensor"],
14 : ["P", "Mass air flow sensor"],
15 : ["vacant", "-"],
16 : ["I", "Cylinder identification sensor"],
17 : ["O", "Fuel consumption (ti)"],
18 : ["vacant", "-"],
19 : ["vacant", "-"],
20 : ["vacant", "-"],
21 : ["vacant", "-"],
22 : ["vacant", "-"],
23 : ["O", "Ignition control (terminal 1), cyl. no. 2"],
24 : ["O", "Ignition control (terminal 1), cyl. no. 3"],
25 : ["O", "Ignition control (terminal 1), cyl. no. 1"],
26 : ["I", "Power supply (terminal 30)"],
27 : ["O", "Main relay control"],
28 : ["P", "Ground"],
29 : ["O", "Idle speed control valve"],
30 : ["vacant", "-"],
31 : ["O", "Fuel injector, cyl. no. 5"],
32 : ["O", "Fuel injector, cyl. no. 6"],
33 : ["O", "Fuel injector, cyl. no. 4"],
34 : ["P", "Ground"],
35 : ["vacant", "-"],
36 : ["O", "Evaporative purge valve control"],
37 : ["O", "Oxygen sensor heater relay control"],
38 : ["vacant", "-"],
39 : ["vacant", "-"],
40 : ["vacant", "-"],
41 : ["I", "Mass air flow sensor"],
42 : ["vacant", "-"],
43 : ["P", "Ground"],
44 : ["I", "Cylinder identification sensor"],
45 : ["vacant", "-"],
46 : ["vacant", "-"],
47 : ["vacant", "-"],
48 : ["O", "A/C compressor control"],
49 : ["vacant", "-"],
50 : ["O", "Ignition control (terminal 1), cyl. no. 4"],
51 : ["O", "Ignition control (terminal 1), cyl. no. 6"],
52 : ["O", "Ignition control (terminal 1), cyl. no. 5"],
53 : ["vacant", "-"],
54 : ["I", "Power supply"],
55 : ["P", "Ground"],
56 : ["I", "Power supply (terminal 15)"],
57 : ["vacant", "-"],
58 : ["vacant", "-"],
59 : ["O", "Throttle position sensor"],
60 : ["I", "Data link connector"],
61 : ["vacant", "-"],
62 : ["vacant", "-"],
63 : ["vacant", "-"],
64 : ["I", "Ignition timing intervention"],
65 : ["I", "Automatic transmission (A/T) range switch"],
66 : ["vacant", "-"],
67 : ["I", "Engine speed/crankshaft position sensor"],
68 : ["I", "Engine speed/crankshaft position sensor"],
69 : ["vacant", "-"],
70 : ["I", "Oxygen sensor"],
71 : ["P", "Oxygen sensor"],
72 : ["vacant", "-"],
73 : ["I", "Road speed"],
74 : ["O", "Engine speed (TD)"],
75 : ["vacant", "-"],
76 : ["vacant", "-"],
77 : ["I", "Intake air temperature (IAT) sensor"],
78 : ["I", "Engine coolant temperature (ECT) sensor"],
79 : ["vacant", "-"],
80 : ["vacant", "-"],
81 : ["I", "On-board computer"],
82 : ["vacant", "-"],
83 : ["vacant", "-"],
84 : ["vacant", "-"],
85 : ["I", "A/C pressure switch"],
86 : ["I", "A/C compressor on"],
87 : ["I", "Diagnostic connector (RxD)"],
88 : ["I", "Diagnostic connector (TxD)"]}

print "EESchema-LIBRARY Version 2.3  Date: Sun 14 Oct 2012 07:21:31 AM CEST"
print "#encoding utf-8"
print "#"
print "# MOTRONIC88"
print "#"
print "DEF ~MOTRONIC88 J 0 30 Y Y 1 F N"
print "F0 \"J\" 80 0 40 H V L CNN"
print "F1 \"MOTRONIC88\" 0 55 30 H I C CNN"
print "DRAW"

for pin in range(88, 55, -1):
	if connector[pin][0]=="vacant":
		continue
	x = (88-pin)*50*2
	y = 0
	print "C %d %d 15 0 1 0 N" % (x, y)
	print "X %d %d %d %d 100 U 30 30 1 1 %s" % (pin, pin, x, y-115, connector[pin][0])
for pin in range(1, 7):
	if connector[pin][0]=="vacant":
		continue
	x = 3000 - (pin-1)*50*2
	y = 6*50
	print "C %d %d 15 0 1 0 N" % (x, y)
	print "X %d %d %d %d 100 U 30 30 1 1 %s" % (pin, pin, x, y-115, connector[pin][0])
for pin in range(29, 35):
	if connector[pin][0]=="vacant":
		continue
	x = 2950 - (pin-29)*50*2
	y = 6*50
	print "C %d %d 15 0 1 0 N" % (x, y)
	print "X %d %d %d %d 100 U 30 30 1 1 %s" % (pin, pin, x, y-115, connector[pin][0])
for pin in range(7, 22):
	if connector[pin][0]=="vacant":
		continue
	x = 2400 - (pin-7)*50*2
	y = 5*50
	print "C %d %d 15 0 1 0 N" % (x, y)
	print "X %d %d %d %d 100 U 30 30 1 1 %s" % (pin, pin, x, y-115, connector[pin][0])
for pin in range(35, 49):
	if connector[pin][0]=="vacant":
		continue
	x = 2350 - (pin-35)*50*2
	y = 7*50
	print "C %d %d 15 0 1 0 N" % (x, y)
	print "X %d %d %d %d 100 U 30 30 1 1 %s" % (pin, pin, x, y-115, connector[pin][0])
for pin in range(49, 56):
	if connector[pin][0]=="vacant":
		continue
	x = 950 - (pin-49)*50*2
	y = 6*50
	print "C %d %d 15 0 1 0 N" % (x, y)
	print "X %d %d %d %d 100 U 30 30 1 1 %s" % (pin, pin, x, y-115, connector[pin][0])
for pin in range(22, 29):
	if connector[pin][0]=="vacant":
		continue
	x = 900 - (pin-22)*50*2
	y = 6*50
	print "C %d %d 15 0 1 0 N" % (x, y)
	print "X %d %d %d %d 100 U 30 30 1 1 %s" % (pin, pin, x, y-115, connector[pin][0])
print "ENDDRAW"
print "ENDDEF"
print "#"
print "#End Library"

