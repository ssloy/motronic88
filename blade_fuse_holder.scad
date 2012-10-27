function mil(mm) = mm*1000/25.4;

difference() {
	cube(size = [mil(20)/100,mil(7)/100,mil(8)/100], center = true);
	translate([0,0,mil(2)/100]) {
		cube(size = [mil(17)/100,mil(4)/100,mil(8)/100], center = true);
	}
}

translate([mil(15/2-1.5/2)/100, mil(4/2-.5/2)/100, mil(0)/100]) {
	cube(size = [mil(3.5)/100,mil(1)/100,mil(5)/100], center = true);
}

translate([-mil(15/2-1.5/2)/100, -mil(4/2-.5/2)/100, mil(0)/100]) {
	cube(size = [mil(3.5)/100,mil(1)/100,mil(5)/100], center = true);
}

translate([mil(15/2-1.5/2)/100, -mil(4/2-.5/2)/100, mil(0)/100]) {
	cube(size = [mil(3.5)/100,mil(1)/100,mil(5)/100], center = true);
}

translate([-mil(15/2-1.5/2)/100, mil(4/2-.5/2)/100, mil(0)/100]) {
	cube(size = [mil(3.5)/100,mil(1)/100,mil(5)/100], center = true);
}


translate([mil(15/2-1.5/2)/100, mil(4/2-.5/2)/100, mil(-5)/100]) {
	cube(size = [mil(1.5)/100,mil(.5)/100,mil(4)/100], center = true);
}
translate([mil(-15/2+1.5/2)/100, mil(4/2-.5/2)/100, mil(-5)/100]) {
	cube(size = [mil(1.5)/100,mil(.5)/100,mil(4)/100], center = true);
}
translate([mil(15/2-1.5/2)/100, -mil(4/2-.5/2)/100, mil(-5)/100]) {
	cube(size = [mil(1.5)/100,mil(.5)/100,mil(4)/100], center = true);
}
translate([mil(-15/2+1.5/2)/100, -mil(4/2-.5/2)/100, mil(-5)/100]) {
	cube(size = [mil(1.5)/100,mil(.5)/100,mil(4)/100], center = true);
}

