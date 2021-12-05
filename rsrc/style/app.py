default = """
#booque {
	background-color: rgb(255, 247, 237);
}

#prof_btn::menu-indicator {
    image: url(myindicator.png);
    subcontrol-position: right center;
    subcontrol-origin: padding;
    left: -5px;
}

QMenu {
	background-color: rgb(250, 239, 225);
}
QMenu::item {
	padding: 5px 10px 5px 20px;
	border: 1px solid transparent; 
	spacing: 10px;
	color: black;
}
QMenu::item:selected {
	background-color: rgb(255, 230, 212);
}
"""

dark_mode = """
#booque {
	background-color: rgb(49, 46, 43);
}

#prof_btn::menu-indicator {
    image: url(myindicator.png);
    subcontrol-position: right center;
    subcontrol-origin: padding;
    left: -5px;
}

QMenu {
	background-color: rgb(71, 64, 56);
}
QMenu::item {
	padding: 5px 10px 5px 20px;
	border: 1px solid transparent; 
	spacing: 10px;
	color: white;
}
QMenu::item:selected {
	background-color: rgb(87, 79, 70);
}
"""
