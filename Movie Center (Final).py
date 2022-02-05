
print("______________________________________****Movies Centre****____________________________________")
print()
print()
print("Hello, I am the driver of the MOVIE_RATER , as we know that humans are very much interested in movies so lets start making a database of the movies in which you just give the commands and I will be helping you.")

print("")

#creating database
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="movie_center")
c1=mydb.cursor()
c1.execute("create database if not exists movie_center")
c1.execute("use movie_center")

#creating required tables 
c1.execute("create table if not exists Bollywood(sno char(44) primary key,Name_movie varchar(130),director_name varchar(30),expenditure char(190),IMDB_rating varchar(60),legend varchar(120),comment varchar(1000))")
c1.execute("create table if not exists Hollywood(sno char(44) primary key,Name_movie varchar(130),director_name char(120),expenditure char(190),IMDB_rating varchar(60),legend char(20),comment varchar(1000))")
c1.execute("create table if not exists Tollywood(sno char(44) primary key,name_movie varchar(30),director_name char(20),expenditure char(100),IMDB_rating varchar(160),legend char(20),comment varchar(1000))")
c1.execute("create table if not exists Chinese(sno char(44) primary key,Name_movie varchar(190),director_name char(120),expenditure varchar(190),IMDB_rating varchar(200),legend char(20),comment varchar(1000))")
mydb.commit()


def Bollywood_entry():
    print()
    Sno=0
    q1="select * from Bollywood"
    c1.execute(q1)
    c=0
    for count in c1:
        c=c+1
    c=c+1
    Sno="Bollywood"+str(c)
        
    Name_movie=input("Enter the name of the movie:")
    director_name=str(input("Enter the name of the director :"))
    IMDB_rating=str(input("Enter the rating given by IMDB:"))
    expenditure=str(input("Enter total Expenditure:"))
    legend=str(input("Was this movie a legendary or not : "))
    comment=input("Write your views on this movie: ")
        #balance=0
    q1="insert into Bollywood (sno,Name_movie,director_name,expenditure,IMDB_rating,legend,comment)values(%s,%s,%s,%s,%s,%s,%s)"
    values=(Sno,Name_movie,director_name,expenditure,IMDB_rating,legend,comment)
    c1.execute(q1,values)
    mydb.commit()
    print("Information is successfull filled!!!")
    
    sql="select * from Bollywood order by sno "
    
    c1.execute(sql)
    
    result = c1.fetchall()
    count=0
    from prettytable import PrettyTable
    t=PrettyTable()
    t.field_names=["Sno",'Movie',"Director","Expenditure"]#,"IMDB Rating","Legend",]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3]])#,col[4],col[5]])
        count+=1
    print(t)

            
def Hollywood_entry():
    Sno=0
    q1="select * from Hollywood"
    c1.execute(q1)
    c=0
    for count in c1:
        c=c+1
    c=c+1
    Sno="Hollywood"+str(c)
        
    Name_movie=input("Enter the name of the movie:")
    director_name=str(input("Enter the name of the director :"))
    IMDB_rating=str(input("Enter the rating given by IMDB:"))
    expenditure=str(input("Enter total Expenditure:"))
    legend=str(input("Was this movie a legendary or not : "))
    comment=input("Write your views on this movie: ")
        #balance=0
    q1="insert into Hollywood (sno,Name_movie,director_name,expenditure,IMDB_rating,legend,comment)values(%s,%s,%s,%s,%s,%s,%s)"
    values=(Sno,Name_movie,director_name,expenditure,IMDB_rating,legend,comment)
    c1.execute(q1,values)
    mydb.commit()
    print("Information is successfull filled!!!")
    sql="select * from Hollywood order by sno "
    
    c1.execute(sql)
    
    result = c1.fetchall()
    count=0
    from prettytable import PrettyTable
    t=PrettyTable()
    t.field_names=["Sno",'Movie',"Director","Expenditure"]#,"IMDB Rating","Legend"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3]])#,col[4],col[5]])
        count+=1
    print(t)


def Tollywood_entry():
    
    Sno=0
    q1="select * from Tollywood"
    c1.execute(q1)
    c=0
    for count in c1:
        c=c+1
    c=c+1
    Sno="Tollywood"+str(c)
        
    Name_movie=input("Enter the name of the movie:")
    director_name=str(input("Enter the name of the director :"))
    IMDB_rating=str(input("Enter the rating given by IMDB:"))
    expenditure=str(input("Enter total Expenditure:"))
    legend=str(input("Was this movie a legendary or not : "))
    comment=input("Write your views on this movie: ")
        #balance=0
    q1="insert into Tollywood (sno,Name_movie,director_name,expenditure,IMDB_rating,legend,comment)values(%s,%s,%s,%s,%s,%s,%s)"
    values=(Sno,Name_movie,director_name,expenditure,IMDB_rating,legend,comment)
    c1.execute(q1,values)
    mydb.commit()
    print("Information is successfull filled!!!")
    sql="select * from Tollywood order by sno "
    
    c1.execute(sql)
    
    result = c1.fetchall()
    count=0
    from prettytable import PrettyTable
    t=PrettyTable()
    t.field_names=["Sno",'Movie',"Director","Expenditure"]#,"IMDB Rating","Legend"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3]])#,col[4],col[5]])
        count+=1
    print(t)

   
def Chinese_entry():
    Sno=0
    q1="select * from Chinese"
    c1.execute(q1)
    c=0
    for count in c1:
        c=c+1
    c=c+1
    Sno="Chinese"+str(c)
        
    Name_movie=input("Enter the name of the movie:")
    director_name=str(input("Enter the name of the director :"))
    IMDB_rating=str(input("Enter the rating given by IMDB:"))
    expenditure=str(input("Enter total Expenditure:"))
    legend=str(input("Was this movie a legendary or not : "))
    comment=input("Write your views on this movie: ")
        #balance=0
    q1="insert into chinese(sno,Name_movie,director_name,expenditure,IMDB_rating,legend,comment)values(%s,%s,%s,%s,%s,%s,%s)"
    values=(Sno,Name_movie,director_name,expenditure,IMDB_rating,legend,comment)
    c1.execute(q1,values)
    mydb.commit()
    print("Information is successfull filled!!!")
    
    sql="select * from chinese order by sno "
    
    c1.execute(sql)
    
    result = c1.fetchall()
    count=0
    from prettytable import PrettyTable
    t=PrettyTable()
    t.field_names=["Sno",'Movie',"Director","Expenditure"]#,"IMDB Rating","Legend","Comment"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3]])#,col[4],col[5]])
        count+=1
    print(t)

    
#To search the records
    
def Bollywood_Search():
    sno=str(input("Enter the name of the movie :"))
    from prettytable import PrettyTable
    t=PrettyTable()
    
    sql="select * from Bollywood where Name_movie like %s "
    movie=(sno,)
    c1.execute(sql,movie)
    
    result = c1.fetchall()
    count=0
    
    t.field_names=["Sno",'Movie',"Director","Expenditure","IMDB Rating","Legend"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3],col[4],col[5]])
        count+=1
        
    if count>0:
        print(t)
    else:
        print("No Record Found")
        
   
def Hollywood_Search():
    sno=str(input("Enter the name of the movie :"))
    from prettytable import PrettyTable
    t=PrettyTable()
    
    sql="select * from hollywood where Name_movie like %s "
    movie=(sno,)
    c1.execute(sql,movie)
    
    result = c1.fetchall()
    count=0
    
    t.field_names=["Sno",'Movie',"Director","Expenditure","IMDB Rating","Legend"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3],col[4],col[5]])
        count+=1
        
    if count>0:
        print(t)
    else:
        print("No Record Found")


def Tollywood_Search():
    sno=str(input("Enter the name of the movie :"))
    from prettytable import PrettyTable
    t=PrettyTable()
    
    sql="select * from Tollywood where Name_movie like %s "
    movie=(sno,)
    c1.execute(sql,movie)
    
    result = c1.fetchall()
    count=0
    
    t.field_names=["Sno",'Movie',"Director","Expenditure","IMDB Rating","Legend"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3],col[4],col[5]])
        count+=1
        
    if count>0:
        print(t)
    else:
        print("No Record Found")


def Chinese_Search():
    sno=str(input("Enter the name of the movie :"))
    from prettytable import PrettyTable
    t=PrettyTable()
    
    sql="select * from Chinese where Name_movie like %s "
    movie=(sno,)
    c1.execute(sql,movie)
    
    result = c1.fetchall()
    count=0
    
    t.field_names=["Sno",'Movie',"Director","Expenditure","IMDB Rating","Legend"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3],col[4],col[5]])
        count+=1
        
    if count>0:
        print(t)
    else:
        print("No Record Found")


#To display the records

def Bollywood_Show():
    
    from prettytable import PrettyTable
    t=PrettyTable()
    
    sql="select * from Bollywood order by sno  "
    
    c1.execute(sql)
    
    result = c1.fetchall()
    count=0
    
    t.field_names=["Sno",'Movie',"Director","Expenditure","IMDB Rating","Legend"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3],col[4],col[5]])
        count+=1
    print(t)
    print("Total Records: ",count)

   
def Hollywood_Show():
    
    from prettytable import PrettyTable
    t=PrettyTable()
    
    sql="select * from hollywood order by sno "
    
    c1.execute(sql)
    
    result = c1.fetchall()
    count=0
    
    t.field_names=["Sno",'Movie',"Director","Expenditure","IMDB Rating","Legend"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3],col[4],col[5]])
        count+=1
    print(t)
    print("Total Records: ",count)


def Tollywood_Show():
    
    from prettytable import PrettyTable
    t=PrettyTable()
    
    sql="select * from Tollywood order by sno "
   
    c1.execute(sql)
    
    result = c1.fetchall()
    count=0
    
    t.field_names=["Sno",'Movie',"Director","Expenditure","IMDB Rating","Legend"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3],col[4],col[5]])
        count+=1
    print(t)
    print("Total Records: ",count)
        
   
def Chinese_Show():
    
    from prettytable import PrettyTable
    t=PrettyTable()
    
    sql="select * from Chinese order by sno"
    
    c1.execute(sql)
    
    result = c1.fetchall()
    count=0
    
    t.field_names=["Sno",'Movie',"Director","Expenditure","IMDB Rating","Legend"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3],col[4],col[5]])
        count+=1
    print(t)
    print("Total Records: ",count)
        
   

        
#To delete the records
    
def Hollywood_Delete():
       
    sno=str(input("Enter the serial number:"))
    sql="select * from Hollywood where sno like %s "
    movie=(sno,)
    c1.execute(sql,movie)
    
    result = c1.fetchall()
    count=0
    from prettytable import PrettyTable
    t=PrettyTable()
    t.field_names=["Sno",'Movie',"Director","Expenditure","IMDB Rating","Legend"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3],col[4],col[5]])
        count+=1
    if count>0:
        
        print (t)
        choice=input("Are you sure to delete this record? (Y/N): ")
        if choice=="Y" or choice=="y":
            sql="delete from Hollywood where sno like %s "
            movie=(sno,)
            c1.execute(sql,movie)
            mydb.commit()
            print("Information is successfull deleted!!!")
        else:
            return
    else:
        print("Movie not found")
        return
    

def Bollywood_Delete():
       
    sno=str(input("Enter the serial number:"))
    sql="select * from Bollywood where sno like %s "
    movie=(sno,)
    c1.execute(sql,movie)
    
    result = c1.fetchall()
    count=0
    from prettytable import PrettyTable
    t=PrettyTable()
    t.field_names=["Sno",'Movie',"Director","Expenditure","IMDB Rating","Legend"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3],col[4],col[5]])
        count+=1
    if count>0:
        
        print (t)
        choice=input("Are you sure to delete this record? (Y/N): ")
        if choice=="Y" or choice=="y":
            sql="delete from Bollywood where sno like %s "
            movie=(sno,)
            c1.execute(sql,movie)
            mydb.commit()
            print("Information is successfull deleted!!!")
        else:
            return
    else:
        print("Movie not found")
        return


def Tollywood_Delete():
       
    sno=str(input("Enter the serial number:"))
    sql="select * from Tollywood where sno like %s "
    movie=(sno,)
    c1.execute(sql,movie)
    
    result = c1.fetchall()
    count=0
    from prettytable import PrettyTable
    t=PrettyTable()
    t.field_names=["Sno",'Movie',"Director","Expenditure","IMDB Rating","Legend"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3],col[4],col[5]])
        count+=1
    if count>0:
        
        print (t)
        choice=input("Are you sure to delete this record? (Y/N): ")
        if choice=="Y" or choice=="y":
            sql="delete from Tollywood where sno like %s "
            movie=(sno,)
            c1.execute(sql,movie)
            mydb.commit()
            print("Information is successfull deleted!!!")
        else:
            return
    else:
        print("Movie not found")
        return
          

def Chinese_Delete():
       
    sno=str(input("Enter the serial number:"))
    sql="select * from Chinese where sno like %s "
    movie=(sno,)
    c1.execute(sql,movie)
    
    result = c1.fetchall()
    count=0
    from prettytable import PrettyTable
    t=PrettyTable()
    
    t.field_names=["Sno",'Movie',"Director","Expenditure","IMDB Rating","Legend"]
    for col in result:
        t.add_row([col[0],col[1],col[2],col[3],col[4],col[5]])
        count+=1
    if count>0:
        
        print (t)
        choice=input("Are you sure to delete this record? (Y/N): ")
        if choice=="Y" or choice=="y":
            sql="delete from Chinese where sno like %s "
            movie=(sno,)
            c1.execute(sql,movie)
            mydb.commit()
            print("Information is successfull deleted!!!")
        else:
            return
    else:
        print("Movie not found")
        return
    




    
while(True):
    print("========================== Welcome to Movie Center ===========================")
    print("Press-1 for Bollywood Movies")
    print("Press-2 for Hollywood Movies")
    print("Press-3 for Tollywood Movies")
    print("Press-4 for Chinese Movies ")
    print("Press-5 To Quit Application ")
    
    ch=int(input("Enter your choice:"))

    if ch==1:
        while True:
            print("---------------  Bollywood Movies  ------------------ ")
            print("Press-1 To Fill Information of Bollywood Movies")
            print("Press-2 To Display All Bollywood Movies")
            print("Press-3 To Search Bollywood Movies by Name:")
            print("Press-4 To Delete any Bollywood Movie by SrNo:")
            print("Press-5 To Go To Main Menu:")
            chh=int(input("Enter your choice:"))
            if chh==1:
                Bollywood_entry()
            elif chh==2:
                Bollywood_Show()
            elif chh==3:
                Bollywood_Search()
            elif chh==4:
                Bollywood_Delete()
            elif chh==5:
                break
            else:
                print("Wrong choice! Try Again...")
            
    elif ch==2:
        
        while True:
            
            print("---------------  Hollywood Movies  ------------------ ")
            print("Press-1 To Fill Information of Hollywood Movies")
            print("Press-2 To Display All Hollywood Movies")
            print("Press-3 To Search Hollywood Movies by Name:")
            print("Press-4 To Delete any Hollywood Movie by SrNo:")
            print("Press-5 To Go To Main Menu:")
            chh=int(input("Enter your choice:"))
            if chh==1:
                Hollywood_entry()
            elif chh==2:
                Hollywood_Show()
            elif chh==3:
                Hollywood_Search()
            elif chh==4:
                Hollywood_Delete()
            elif chh==5:
                break
            else:
                print("Wrong choice! Try Again...")
    elif ch==3:
        while True:
            print("---------------  Tollywood Movies  ------------------ ")
            print("Press-1 To Fill Information of Tollywood Movies")
            print("Press-2 To Display All Tollywood Movies")
            print("Press-3 To Search Tollywood Movies by Name:")
            print("Press-4 To Delete any Tollywood Movie by SrNo:")
            print("Press-5 To Go To Main Menu:")
            chh=int(input("Enter your choice:"))
            if chh==1:
                Tollywood_entry()
            elif chh==2:
                Tollywood_Show()
            elif chh==3:
                Tollywood_Search()
            elif chh==4:
                Tollywood_Delete()
            elif chh==5:
                break
            else:
                print("Wrong choice! Try Again...")
        
    elif ch==4:
        while True:
            print("---------------  Chinese Movies  ------------------ ")
            print("Press-1 To Fill Information of Chinese Movies")
            print("Press-2 To Display All Chinese Movies")
            print("Press-3 To Search Chinese Movies by Name:")
            print("Press-4 To Delete any Chinese Movie by SrNo:")
            print("Press-5 To Go To Main Menu:")
            chh=int(input("Enter your choice:"))
            if chh==1:
                Chinese_entry()
            elif chh==2:
                Chinese_Show()
            elif chh==3:
                Chinese_Search()
            elif chh==4:
                Chinese_Delete()
            elif chh==5:
                break
            else:
                print("Wrong choice! Try Again...")
    elif ch==5:
        print("Thank You for using our Online Movie Centre...........")
        break
 
