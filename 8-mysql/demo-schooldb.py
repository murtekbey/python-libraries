import mysql.connector
import datetime
from connection import connection

ogrenciler = [
    ("0001","Murat","Altınpınar",datetime.datetime(1994,1,29),"E"),
    ("0002","Gurur","Altınpınar",datetime.datetime(2001,9,19),"E"),
    ("0003","Kadir","Altınpınar",datetime.datetime(1972,11,10),"E"),
    ("0004","Anıl","Koralay",datetime.datetime(1994,2,6),"E"),
    ("0005","Efe","Özcan",datetime.datetime(1995,5,15),"E"),
    ("0006","Süleyman","Yaka",datetime.datetime(1993,11,1),"E")
]

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None: # eğer id bilgisi gönderilmiyorsa, id bilgisine 0 değerini verelim.
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
    
    def saveStudent(self):
        sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)
        try:
            Student.connection.commit() # sorgu databaseye gönderiliyor.
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
            print(f'Son eklenen kaydın id numarası: {Student.mycursor.lastrowid}')
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:
            Student.connection.close()
            print('Database bağlantısı kapandı.')

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        values = (students)
        Student.mycursor.executemany(sql,values)
        try:
            Student.connection.commit() # sorgu databaseye gönderiliyor.
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
            print(f'Son eklenen kaydın id numarası: {Student.mycursor.lastrowid}')
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:
            Student.connection.close()
            print('Database bağlantısı kapandı.')
    
    @staticmethod
    def getStudentById(id):
        sql = "select * from student where id=%s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print('Hata:',err)
    
    def updateStudent(self):
        sql = "Update student set studentNumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.mycursor.execute(sql,values) # bekleyen sql sorguları

        try:
            Student.connection.commit() # gönderilen sql sorguları
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('Hata:',err)

    @staticmethod
    def getStudentsGender(gender):
        sql = "select * from student where gender=%s"
        value = (gender,)

        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print('Hata:',err)

    @staticmethod
    def updateStudents(liste):
        sql = "Update student set studentNumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = [] # values listesini düzenli hale getirelim.
        order = [1,2,3,4,5,0] # istediğimiz index numaralarını yazdık. 0. eleman id'ye karşılık gelsin, 1. elemanda student numbera karşılık gelsin.
        # gelen bilgilerin index numaralarını bu şekilde güncelledik.
        for item in liste: # bize gelen listenin her elemanını tek tek dolaşalım.
            item = [item[i] for i in order] # orderdan gelen index numarasına göre her bir itemi alıcaz. item içerisine kopyalıcaz.
            values.append(item) # ve values listesi içerisine append edicez.

        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit() # gönderilen sql sorguları
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('Hata:',err)

# ahmet = Student('108','Gurur','Altınpınar',datetime.datetime(2005,5,17),'E')
# ahmet.saveStudent()
# Student.saveStudents(ogrenciler)
# Student.updateStudent(2,4582,'Anıl','Koralay')

# student = Student.getStudentById(2)
# student.name = 'Murat'
# student.surname = 'Altınpınar'
# student.updateStudent()

students = Student.getStudentsGender('E') # gender bilgileriyle eşlesenleri students içerisine gönderdik.
print(students)

liste = [] # boş bir liste oluşturduk.
for std in students: # students'ın içerisindeki bütün elemanların arasında dolaşalım.
    std = list(std) # tuple listede değişiklik yapamadığımız için önce tuple'ı listeye dönüştürelim.
    std[2] = 'Mr. ' + std[2] # students'dan aldığımız bilginin 0. indexinde id, 1. indexinde studentnumber, 2. indexinde name bilgisi var.
    # std[2] yi Mr. [std2] ile güncellicez bu sayede tüm erkeklerin önüne Mr. ifadesi gelmiş olucak.
    liste.append(std) # güncellenen her bir elemanı liste üzerine append ettik.

Student.updateStudents(liste) # liste içerisine append ettiğimiz yeni bilgileri, updateStudents fonksiyonunu çağırarak veritabanındaki bilgilerle değiştirelim.