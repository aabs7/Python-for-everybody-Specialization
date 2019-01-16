import sqlite3

conn = sqlite3.connect('orgDatabase.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if(len(fname) <1) : fname = 'mbox-short.txt'
fHandle = open(fname)

for line in fHandle:
	if not (line.startswith('From:')) : continue
	seperated = line.split()
	org = seperated[1].split('@')[1]
	cur.execute('SELECT count FROM Counts where org = ?',(org,))
	row = cur.fetchone()
	if row is None:
		cur.execute('INSERT INTO Counts(org,count) VALUES(? , 1)',(org,))
	else:
		cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))

	#conn.commit() commits outstanding changes to the disk each time through the loop
	#The program can be made faster by moving the commit so it runs only after loop completes
conn.commit()

sqlstr = 'SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10'
print('Counts:')
for row in cur.execute(sqlstr):
	print(str(row[0]),row[1])
cur.close()
