module upper_pin() {
	color([.9,.9,.9]) {
		translate([0,0,2.55]) {
			cube(size = [.25,.25,6.7], center = true);
			translate([0,3.35,3.225]) {
				cube(size = [.25,6.7,.25], center = true);
			}
		}
	}
}
module lower_pin() {
	color([.9,.9,.9]) {
		translate([0,0,.55]) {
			cube(size = [.25,.25,2.7], center = true);
			translate([0,2.35,1.225]) {
				cube(size = [.25,4.7,.25], center = true);
			}
		}
	}
}

module middle_pin() {
	color([.9,.9,.9]) {
		translate([0,0,1.55]) {
			cube(size = [.25,.25,4.7], center = true);
			translate([0,2.35,2.225]) {
				cube(size = [.25,4.7,.25], center = true);
			}
		}
	}
}



translate([0.000000, 0.000000, 0]) { upper_pin(); }
translate([-1.281000, 0.000000, 0]) { upper_pin(); }
translate([-2.563000, 0.000000, 0]) { upper_pin(); }
translate([-3.845000, 0.000000, 0]) { upper_pin(); }
translate([-8.973000, 0.000000, 0]) { upper_pin(); }
translate([-12.819000, 0.000000, 0]) { upper_pin(); }
translate([-14.101000, 0.000000, 0]) { upper_pin(); }
translate([-17.947000, 0.000000, 0]) { upper_pin(); }
translate([-19.229000, 0.000000, 0]) { upper_pin(); }
translate([-21.793000, 0.000000, 0]) { upper_pin(); }
translate([-23.075000, 0.000000, 0]) { upper_pin(); }
translate([-25.639000, 0.000000, 0]) { upper_pin(); }
translate([-26.921000, 0.000000, 0]) { upper_pin(); }
translate([-29.485000, 0.000000, 0]) { upper_pin(); }
translate([-30.767000, 0.000000, 0]) { upper_pin(); }
translate([-35.895000, 0.000000, 0]) { upper_pin(); }
translate([-37.177000, 0.000000, 0]) { upper_pin(); }
translate([-41.023000, 0.000000, 0]) { upper_pin(); }
translate([-42.007000, 2.559000, 0]) { lower_pin(); }
translate([-40.039000, 2.559000, 0]) { lower_pin(); }
translate([-38.070000, 2.559000, 0]) { lower_pin(); }
translate([-36.102000, 2.559000, 0]) { lower_pin(); }
translate([-34.133000, 2.559000, 0]) { lower_pin(); }
translate([-32.165000, 2.559000, 0]) { lower_pin(); }
translate([-41.023000, 2.559000, 0]) { middle_pin(); }
translate([-37.086000, 2.559000, 0]) { middle_pin(); }
translate([-35.118000, 2.559000, 0]) { middle_pin(); }
translate([-33.149000, 2.559000, 0]) { middle_pin(); }
translate([-31.181000, 2.559000, 0]) { middle_pin(); }
translate([-28.903000, 2.362000, 0]) { lower_pin(); }
translate([-25.022000, 2.362000, 0]) { lower_pin(); }
translate([-23.728000, 2.362000, 0]) { lower_pin(); }
translate([-22.435000, 2.362000, 0]) { lower_pin(); }
translate([-21.141000, 2.362000, 0]) { lower_pin(); }
translate([-18.554000, 2.362000, 0]) { lower_pin(); }
translate([-17.261000, 2.362000, 0]) { lower_pin(); }
translate([-28.256000, 2.755000, 0]) { middle_pin(); }
translate([-26.962000, 2.755000, 0]) { middle_pin(); }
translate([-21.788000, 2.755000, 0]) { middle_pin(); }
translate([-19.201000, 2.755000, 0]) { middle_pin(); }
translate([-17.907000, 2.755000, 0]) { middle_pin(); }
translate([-12.733000, 2.755000, 0]) { middle_pin(); }
translate([-9.133000, 2.559000, 0]) { middle_pin(); }
translate([-7.165000, 2.559000, 0]) { middle_pin(); }
translate([-5.196000, 2.559000, 0]) { middle_pin(); }
translate([-1.259000, 2.559000, 0]) { middle_pin(); }
translate([0.708000, 2.559000, 0]) { middle_pin(); }
translate([-8.149000, 2.559000, 0]) { lower_pin(); }
translate([-6.181000, 2.559000, 0]) { lower_pin(); }
translate([-4.212000, 2.559000, 0]) { lower_pin(); }
translate([-2.244000, 2.559000, 0]) { lower_pin(); }
translate([-0.275000, 2.559000, 0]) { lower_pin(); }
translate([1.692000, 2.559000, 0]) { lower_pin(); }



translate([-49.488189, 3.346456, 1.98]) {
translate([-2.76, 1.7716535433, -1.98]) {cube(size = [62.8,6,8.94], center = false);}
	scale([.393700, .393700, .393700]) {
		dxf_linear_extrude(file="motronic88_plastic_piece.dxf",layer="0",height=10,center=true,$fn=100,convexity=10);
	}
}
