#this is a form for register in library to borrow books

"wellcome to our website for add new books and borrow which one you like"

x=int(input("please enter no 1 for create your profile / enter no 2 for add new book / enter no 3 for borrow book"))

#create prifile

if x == (1):

    import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="eee",
  password="123",
  database="library"
    )

    mycursor = mydb.cursor()

    #get information from user
    fname = input("first name :")
    lname = input("last name :") 
    ncode = int(input("national code :"))
    pnumber = int(input("phone number :"))


    sql = "INSERT INTO members (firstname , lastname , ncode , phone number) VALUES (%s, %s, %s, %s)"
    val = (fname , lname , ncode , pnumber)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

#add book

    if x == (2):

        import mysql.connector

    mydb = mysql.connector.connect(
    host="localhost",
    user="eee",
    password="123",
    database="library"
        )
        mycursor = mydb.cursor()

        #get books information
        
        bname = input("book name")
        shabak = int(input("shabak"))
        price = int(input("book price"))


        sql = "INSERT INTO book (book name , shabak , book price) VALUES (%s, %s, %s)"
        val = (bname , shabak , price)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
