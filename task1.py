
def comparelong():
     f1=open('Book1.txt','r')
     f2=open('Book2.txt','r')
     f3=open('Book3.txt','r')

     long1=''
     for line in f1:
      for word in line.split():
       if len(word)>len(long1):
        long1=word
     print("long word in book1 is"  ,long1)
     print("length is ",len(long1))

     f1.close()


     long2=''
     for line in f2:
      for word in line.split():
       if len(word)>len(long2):
        long2=word
     print("long word in biik2 is"  ,long2)
     print("length is ",len(long2))
     f2.close()



     long3=''
     for line in f3:
      for word in line.split():
       if len(word)>len(long3):
        long3=word
     print("long word in book3 is"  ,long3)
     print("length is ",len(long3))
     f3.close()


comparelong()
