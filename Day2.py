class Std:
    def _init_(self): 
        self.__USN = None
        self.__Name = None
        self.__Marks = []
        self.__Percentage = None
        self.__Grade = None

    def Std_Input(self):
        self.__Name = input("Enter your Name: ")
        self.__USN = input("Enter Your USN: ")
        for i in range (0,5):
            marks = input(f"Enter Your Marks in Sub{i+1} : ")
            self.__Marks.append(marks)

    def calc_percentage (self):
        sum = 0
        for i in self.__Marks:
            sum = sum + int(i)
        self.__Percentage = (sum/500)*100

    def calc_Grade(self):
        per = float(self.__Percentage)
        if per<=100 and per >=80:
            self.__Grade = "A"
        elif per<80 and per >=60:
            self.__Grade = "B"
        elif per<60 and per >=40:
            self.__Grade = "C"
        elif per<40 and per >=0:
            self.__Grade = "D"
        else: 
            self.__Grade = "Inavlid"

    def print_details(self):
        print("Name: ",self.__Name)
        print("USN : ",self.__USN)
        print("Marks in Five Subject are :")
        for i in range(0,5):
            print(f"Subject {i+1} = {self.__Marks[i]}")
        print("Percentage : ", self.__Percentage)
        print("Grade : ", self.__Grade)

    def convert_list(self):
        st_list = [self._USN,self.Name,self.Marks,self.Percentage,self._Grade]
        return st_list

    def covert_ob(self,stu_list):
        self.__USN = stu_list[0]
        self.__Name = stu_list[1]
        self.__Marks = stu_list[2]
        self.__Percentage = stu_list[3]
        self.__Grade = stu_list[4]

st1 = Std()

print(type(st1))

st1.Std_Input()

st1.calc_percentage()
st1.calc_Grade()

st1.print_details()

#Using files
with open("student.txt",'wb') as File:
    L=st1.convert_list()
    data = f"{L[0]}|{L[1]}|{L[2][0]},{L[2][1]},{L[2][2]},{L[2][3]},{L[2][4]}|{L[3]}|{L[4]}\n"
    File.write(data.encode())
    File.close()
    stu_list=[]

with open("student.txt",'rb') as File:
    data = File.readline().decode('utf-8')
    print(data)
    for i in data.split("|"):
        stu_list.append(i)
    mrks=stu_list[2]
    mrks_list = []
    for i in mrks.split(','):
        mrks_list.append(i)
    stu_list[2]=mrks_list


print(stu_list)
st2=Std()
st2.covert_ob(stu_list)
st2.print_details()






















'''
class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
class list:
    Head=Tail=list(10)
    Head.next=list(20)
    Head.next.next=list(30)
    Tail=Head.next.next
    Head=None
    Tail=None
    def print_list(self):
        if self.Head==None:
            print("List is empty")
        else:
            cur=self.Head
            while cur!=None:
                print(cur.value)
                cur=cur.next

    #print_list(Head)
    #newN=Node(60)
    def InsF(self,data):
        newN=Node(data)
        
        if self.Head==None:
            self.Head=newN
        else:
            newN.next=Head
            self.Head=newN
l=list()
l.InsF(60)
l.print_list()'''

'''def InsE(Head,data):
        temp=Node(data)
        if Head==None:
            Head=temp
        else:
            cur=Head
            while cur.next!=None:
                cur=cur.next
                cur.next=temp

    InsE(Head,60)
    print_list(Head)'''


            


