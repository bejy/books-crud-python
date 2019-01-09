import pymysql

connection = pymysql.connect(host = 'localhost',user = 'root',password = '',db = 'books')


def create(title,author,genre): 
    with connection.cursor() as cursor:
    	sql = 'INSERT INTO books (id ,title,author,genre) VALUES ( NULL, %s, %s, %s);'
    	try:
    		cursor.execute(sql, (title, author, genre))
    		print('\nSuccessfully Added!')
    	except:
    		print('\nSomething went wrong!')
    connection.commit()

def read(create):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM books"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
	    print '%10s'%('\nID #       	:'),
	    for row in results:
		print '%10d'%(row[0]),
	    print '\n'
	    print '%10s'%('Book Title 	:'),
	    for row in results:
		print '%10s'%(row[1]),
	    print '\n'
	    print '%10s'%('Book Author	:'),
	    for row in results:
		print '%10s'%(row[2]),
	    print '\n'
	    print '%10s'%('Book Genre 	:'),
	    for row in results:
		print '%10s'%(row[3]),
	except:
	     print('\nSomething went wrong!')

    connection.commit()


def update(id):
    with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM books WHERE  id = %s',id)
            cursor.fetchall()
            if cursor.rowcount > 0 :
                new_title = raw_input('\nEnter New Title: ')
                new_author = raw_input('Enter New Author: ')
                new_genre = raw_input('Enter New Genre: ')
                cursor.execute('UPDATE books SET title = %s, author = %s, genre=%s WHERE id = %s',(new_title,new_author,new_genre,id))
                print('\nSuccessfully Updated!')
            else:
                print("\nDoesn't exist")

    connection.commit()


def delete(id):
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM books WHERE id = %s'
        try:
            cursor.execute(sql, id)
            if cursor.rowcount > 0 :
                delete = "DELETE FROM books WHERE id = " + "'" + id + "'"
                cursor.execute(delete)
                print ('\nSuccessfully Deleted!')
            else:
                print "\nDoesn't Exist!"
        except:
            print ('\nSomething went wrong!')

    connection.commit()

""" Choices """
x = 1
while x:
    print '\n'
    print '[C] Create'
    print '[R] Read'
    print '[U] Update'
    print '[D] Delete'
    print '[E] Exit\n'



    choice = raw_input('Enter Choice: ')

    if choice == 'c' or choice == 'C':
        title  = raw_input('\nBook Title   : ')
        author  = raw_input('Book Author  : ')
        genre  = raw_input('Book Genre   : ')
        create(title,author,genre)
    elif choice == 'r' or choice == 'R':
        read(create)
    elif choice == 'u' or choice == 'U':
        id = raw_input('\nEnter ID that you wish to Update:')
        update(id)
    elif choice == 'd' or choice == 'D':
        id = raw_input('\nEnter ID that you wish to delete: ')
        delete(id)
    elif choice == 'e' or choice == 'E':   

        break 
    else:
 	print "Invalid Choice"
