# HackademicRTB1-SQLi-Script


	provide arguments:
	./poc.py target_ip sql_query(within quotes)

	eg: ./poc.py 192.168.0.1 'uname from users'


	"Donot add select query before any query you write
	its already there in the source code"

	If you intent to execute query "select uname from users"
	write it like this
	eg: "uname from users"
