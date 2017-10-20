
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

     


     long2=''
     for line in f2:
      for word in line.split():
       if len(word)>len(long2):
        long2=word
     print("long word in biik2 is"  ,long2)
     print("length is ",len(long2))
     



     long3=''
     for line in f3:
      for word in line.split():
       if len(word)>len(long3):
        long3=word
     print("long word in book3 is"  ,long3)
     print("length is ",len(long3))
     print("FINNALY THE LONGEST WORD AMONG THREE BOOKS ARE")
     if long1 > long2 and long1>long3:
         print("The longest word is  in Book1 ie. ",long1) 
     
     elif long2 > long3 and long2>long1: 
         print("The longest word is  in Book2 ie. ",long2) 
       
     else:
        print("The longest word is in Book3 ie. ",long3)    

     

comparelong()
