#!/usr/bin/python
def mil(mm):
	return int(mm*1000/25.4)
def milX10(mm):
	return int(mm*1000*10/25.4)
def print_circular_pad(pinno, x, y, diameter, drill):
	print "$PAD"
	print "Sh \"%d\" C %d %d 0 0 0" % (pinno, diameter, diameter)
	print "Dr %d 0 0" % (drill)
	print "At STD N 00E0FFFF"
	print "Ne 0 \"\""
	print "Po %d %d" % (x, y)
	print "$EndPAD"

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

if 1:
	print "EESchema-LIBRARY Version 2.3  Date: Sun 14 Oct 2012 07:21:31 AM CEST"
	print "#encoding utf-8"
	print "#"
	print "# MOTRONIC88"
	print "#"
	print "DEF ~MOTRONIC88 J 0 30 Y Y 1 F N"
	print "F0 \"J\" 80 0 40 H V L CNN"
	print "F1 \"MOTRONIC88\" 0 55 30 H I C CNN"
	print "DRAW"

	# C center_x center_y radius ....
	# X pin_name pin_number x y pin_len up/down/.. ..... input/output/passive
	for pin in range(88, 55, -1):
		if connector[pin][0]=="vacant": continue
		x = (88-pin)*50*2
		y = 0
		print "C %d %d 15 0 1 0 N" % (x, y)
		print "X %d %d %d %d 100 U 30 30 1 1 %s" % (pin, pin, x, y-115, connector[pin][0])
	for pin in range(1, 7):
		if connector[pin][0]=="vacant": continue
		x = 3000 - (pin-1)*50*2
		y = 6*50
		print "C %d %d 15 0 1 0 N" % (x, y)
		print "X %d %d %d %d 100 U 30 30 1 1 %s" % (pin, pin, x, y-115, connector[pin][0])
	for pin in range(29, 35):
		if connector[pin][0]=="vacant": continue
		x = 2950 - (pin-29)*50*2
		y = 6*50
		print "C %d %d 15 0 1 0 N" % (x, y)
		print "X %d %d %d %d 100 U 30 30 1 1 %s" % (pin, pin, x, y-115, connector[pin][0])
	for pin in range(7, 22):
		if connector[pin][0]=="vacant": continue
		x = 2400 - (pin-7)*50*2
		y = 5*50
		print "C %d %d 15 0 1 0 N" % (x, y)
		print "X %d %d %d %d 100 U 30 30 1 1 %s" % (pin, pin, x, y-115, connector[pin][0])
	for pin in range(35, 49):
		if connector[pin][0]=="vacant": continue
		x = 2350 - (pin-35)*50*2
		y = 7*50
		print "C %d %d 15 0 1 0 N" % (x, y)
		print "X %d %d %d %d 100 U 30 30 1 1 %s" % (pin, pin, x, y-115, connector[pin][0])
	for pin in range(49, 56):
		if connector[pin][0]=="vacant": continue
		x = 950 - (pin-49)*50*2
		y = 6*50
		print "C %d %d 15 0 1 0 N" % (x, y)
		print "X %d %d %d %d 100 U 30 30 1 1 %s" % (pin, pin, x, y-115, connector[pin][0])
	for pin in range(22, 29):
		if connector[pin][0]=="vacant": continue
		x = 900 - (pin-22)*50*2
		y = 6*50
		print "C %d %d 15 0 1 0 N" % (x, y)
		print "X %d %d %d %d 100 U 30 30 1 1 %s" % (pin, pin, x, y-115, connector[pin][0])
	print "ENDDRAW"
	print "ENDDEF"
	print "#"
	print "#End Library"
else:
	print "PCBNEW-LibModule-V1  Sun 22 Jan 2012 12:13:15 AM CET"
	print "# encoding utf-8"
	print "$INDEX"
	print "motronic88"
	print "$EndINDEX"
	print "$MODULE motronic88"
	print "Po 0 0 0 15 4F1B4664 4F1B4221 ~~"
	print "Li motronic88"
	print "Sc 4F1B4221"
	print "AR "
	print "Op 0 0 0"
	print "T0 600 1200 600 600 0 120 N V 21 N \"motronic88\""
	print "T1 0 0 600 600 0 120 N V 21 N """

	for pin in range(88, 55, -1):
		if connector[pin][0]=="vacant": continue
		x = -milX10(3.25625*(88-pin))
		y = 0
		print_circular_pad(pin, x, y, milX10(2.95), milX10(.5))
	for pin in range(1, 7):
		if connector[pin][0]=="vacant": continue
		x = -milX10(106.7 - (pin-1)*5)
		y = milX10(-6.5)
		print_circular_pad(pin, x, y, milX10(2.2), milX10(.5))
	for pin in range(29, 35):
		if connector[pin][0]=="vacant": continue
		x = -milX10(104.2 - (pin-29)*5)
		y = milX10(-6.5)
		print_circular_pad(pin, x, y, milX10(2.2), milX10(.5))
	for pin in range(7, 22):
		if connector[pin][0]=="vacant": continue
		x = -milX10(76.7 - (pin-7)*3.2857)
		y = milX10(-6)
		print_circular_pad(pin, x, y, milX10(2.2), milX10(.5))
	for pin in range(35, 49):
		if connector[pin][0]=="vacant": continue
		x = -milX10(75.057 - (pin-35)*3.2857)
		y = milX10(-7)
		print_circular_pad(pin, x, y, milX10(2.2), milX10(.5))
	for pin in range(49, 56):
		if connector[pin][0]=="vacant": continue
		x = -milX10(28.2 - (pin-49)*5)
		y = milX10(-6.5)
		print_circular_pad(pin, x, y, milX10(2.2), milX10(.5))
	for pin in range(22, 29):
		if connector[pin][0]=="vacant": continue
		x = -milX10(25.7 - (pin-22)*5)
		y = milX10(-6.5)
		print_circular_pad(pin, x, y, milX10(2.2), milX10(.5))

	print "$EndMODULE  motronic88"
	print "$EndLIBRARY"
