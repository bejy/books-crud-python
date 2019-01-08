import pymysql
import sys

connection = pymysql.connect(host = 'localhost',user = 'root',password = '', db = 'books')   
    
choices = 1
while choices:
    print ("[1] = Add new Book\n")
    print ("[2] = Show lists of Books\n")
    print ("[3] = Update Books\n")
    print ("[4] = Delete Books\n")
    print ("[5] = Exit\n")

    choice = input("Input task: ")

    if choice == "1":
         book_title = raw_input("Enter Book title: ")
         book_author= raw_input("Enter Book Author: ")
         book_rating= raw_input("Enter rating: ")
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO books ('book_title', 'book_author', 'book_rating') VALUES (%s, %s, %s)"
            try:
                cursor.execute(sql, (book_title, book_author, book_rating))
                print("Added successfully")
            except:
                print("Something wrong")
                
        connection.commit()
    finally:
        print ("")
  
    
    if choice == "2":
        print ("Books\n")
    try:
        with connection.cursor() as cursor:
            sql = "select * from books"
            cursor.execute(sql)
            connection.commit()
            results = cursor.fetchall()
	    print '%10s'%("ID #         :"),
	    for row in results:
		print '%10d'%(row[0]),
	    print '\n'
	    print '%10s'%("Book Title   :"),
	    for row in results:
		print '%10s'%(row[1]),
	    print '\n'
	    print '%10s'%("Book Author  :"),
	    for row in results:
		print '%10s'%(row[2]),
	    print '\n'
	    print '%10s'%("Book rating  :"),
	    for row in results:
		print '%10s'%(row[3]),
        connection.commit()
    finally:
        print ("")
    
    
    
    if choice == "3":
    	print("Books\n")
    	id = input("Enter your Book ID to Update: ")
    	books_title = raw_input("Enter the new book title: ")
    	book_author = raw_input("Enter the new book author: ")
    	book_rating = raw_input("Enter the new book rating: ")
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE books SET 'book_title'=%s, 'book_author'=%s , 'book_rating'=%s WHERE 'id'= %s"
            try:
                cursor.execute(sql, (book_title, book_author, book_rating, id))
                print("Successfully Updated")
            except:
                print("Something wrong")
 
        connection.commit()
    finally:
        print ("")
      
    
    
    if choice == "4":
	print("Books\n")
    	id = input("Enter the ID of the Book to delete: ")
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM books WHERE id = %s"
            try:
                cursor.execute(sql, (id))
                print("Successfully Deleted")
            except:
                print("Something wrong")
 
        connection.commit()
    finally:
        print ("")
       
    
    
    if choice == "5":
        sys.exit(0)
        
    else:
        print ("Invalid Input!\n")
        choices = 1
