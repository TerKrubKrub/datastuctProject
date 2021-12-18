default = """
#rank {
    background-color: rgb(172, 162, 151);
	border-top-left-radius: 80px;
}

QRadioButton {
	padding-right: 30px;
	color: black;
}
QRadioButton::checked  {
	background-color: rgb(172, 162, 151);
	border-top-left-radius: 20px;
	border-bottom-left-radius: 20px;
	color: white;
}
QRadioButton::indicator {
	width: 0px;
	height: 0px;
}

QPushButton {
	background-color: rgba(255, 255, 255, 0);
}

#genre_label {
    padding-left: 60px;
	color: white;
}

#first_label {
    color: rgb(255, 166, 107);
}

#second_label {
    color: rgb(255, 166, 107);
}

#third_label {
    color: rgb(255, 166, 107);
}
"""

dark_mode = """
#rank {
	background-color: rgb(255, 241, 213);
	border-top-left-radius: 80px;
}

QRadioButton {
	padding-right: 30px;
	color: white;
}
QRadioButton::checked  {
	background-color: rgb(255, 241, 213);
	border-top-left-radius: 20px;
	border-bottom-left-radius: 20px;
	color: black;
}
QRadioButton::indicator {
	width: 0px;
	height: 0px;
}

QPushButton {
	background-color: rgba(255, 255, 255, 0);
}

#genre_label {
    padding-left: 60px;
	color: black;
}

#first_label {
    color: rgb(255, 166, 107);
}

#second_label {
    color: rgb(255, 166, 107);
}

#third_label {
    color: rgb(255, 166, 107);
}
"""
