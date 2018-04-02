# Log_Analysis_Project
=========================
- It's a Project in the curriculum of the Udacity Full Stack Developer Nanodegree.
- In this Project, Analytical data is retrieved from newspapers using Python program connected with Postgresql database by the psycopg2    Library.

The expected program output is as the following :
 ------------------------------------------------ 
 The most popular three articles of all time :
 ---------------------------------------------
  *  Candidate is jerk, alleges rival __ 338647  Views
  *  Bears love berries, alleges bear __ 253801  Views
  *  Bad things gone, say good people __ 170098  Views
 ---------------------------------------------
 The Authors Popularity:
 ---------------------------------------------
  *  Ursula La Multa __ 507594  Views
  *  Rudolf von Treppenwitz __ 423457  Views
  *  Anonymous Contributor __ 170098  Views
  *  Markoff Chaney __ 84557  Views
 ---------------------------------------------
 The Days where Error-Status > 1%:
 ---------------------------------------------
  July 17, 2016 __ 2.3 %  errors
 ---------------------------------------------

Steps to run the Program :
--------------------------
1) Install Vagrant from https://www.vagrantup.com/
2) Install VirtualBox from https://www.virtualbox.org/
3) Download vagrant setup files from https://github.com/udacity/fullstack-nanodegree-vm
4) Download database from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
5) Unzip the data to get the newsdata.sql file.
6) Put the newsdata.sql file into the vagrant directory
7) Download the Logs Analysis project
8) Upzip and copy all files into the vagrant directory into a folder called Logs_Analysis_Project
9) Run the Virtual Machine:
10) Download GitBash or any terminal
11) Open your terminal and navigate to the FSND-Virtual-Machine folder.
12) cd into the vagrant directory
13) Run vagrant up to build the VM.
14) run vagrant ssh to connect.
15) cd into the correct project directory: cd /vagrant/Logs_Analysis_Project
16) Load the data into the database using the following command: psql -d news -f newsdata.sql
17) Run the views scripts (please find them in the Views Scripts section) and press Enter after typing each view script 
18) Finally, Type the command: python Logs_analyis_Project.py

Views Scripts
-----------
1) Create View AllStatusView as
    SELECT time::date as V1Day, count(status) as CountAllDayStatus From Log
    Group By(V1Day);
    
2) Create View FailedStatusView as
    SELECT time :: date as V2Day, count(status) as CountDayFailedStatus
    From Log
    where status <> '200 OK'
    Group By(V2Day);




