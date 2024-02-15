all: robot_utils kg-microbe uniprot-download

robot_utils:

	wget "https://github.com/ontodev/robot/releases/download/v1.9.5/robot.jar" -O robot.jar
	wget "https://raw.githubusercontent.com/ontodev/robot/master/bin/robot" -O robot

kg-microbe:

	wget "https://raw.githubusercontent.com/Knowledge-Graph-Hub/kg-microbe/master/data/raw/exclusion_branches.tsv" -O exclusion_branches.tsv

	

uniprot-download:

	up download-uniprot-genomes