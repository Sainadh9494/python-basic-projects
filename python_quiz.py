class PythonQuiz:
    def __init__(self):
        self.score=0
        self.student_ids = [
                            1001,
                            1002,
                            1003,
                            1004,
                            1005,
                            1006,
                            1007,
                            1008,
                            1009,
                            1010
                       ]
        self.data=[
                    {"question":"Which keyword is used to define a function in Python?",
                    "options":{"A":"func","B": "def","C": "function","D": "define"},
                    "answer":"B"},

                        {
                "question": "Which data type stores key-value pairs in Python?",
                "options": {
                    "A": "List",
                    "B": "Tuple",
                    "C": "Dictionary",
                    "D": "Set"
                },
                "answer": "C"

                },
                {
                "question": "What is the output of 3 ** 2 in Python?",
                "options": {
                    "A": "6",
                    "B": "9",
                    "C": "8",
                    "D": "5"
                },
                "answer": "B"
                },
            {
                "question": "Which method adds an element to the end of a list?",
                "options": {
                    "A": "add()",
                    "B": "insert_end()",
                    "C": "append()",
                    "D": "push()"
                },
                "answer": "C"
            },
            {
                "question": "Which keyword is used to create a class in Python?",
                "options": {
                    "A": "object",
                    "B": "class",
                    "C": "define",
                    "D": "struct"
                },
                "answer": "B"
            }
              ]
    def display_question(self,num):
        while(True):
            print(f"========== QUESTION-{num+1} ==========\n")
            print(self.data[num]["question"])
            
            options=list(self.data[num]["options"].items())
            for i in range(0,4):
                print(options[i][0],end=": ")
                print(options[i][1])
            print()
            ans=input("enter the option : ").upper()
            if(ans in ['A','B','C','D']):
                break
            else:
                print("enter the valid option")
        return ans
    def check_answer(self,option,num):
        option=option.upper()
        print("your answer : ",option)
        if(option==self.data[num]["answer"]):
            print("correct!")
            self.score+=1
        else:
            print("wrong")
    def display_result(self,num):
        print("========== QUIZ RESULT ==========")
        print(f"ATTEMPTED QUESTIONS  : {num+1}")
        percentage=round((self.score*100)/(num+1),2)
        if(percentage==100):
            print("Congratulations ! ")
            print("YOU HAVE SCORED FULL SCORE")
        print(f"SCORE : {self.score}/{num+1}")
        print(f"PERCENTAGE : {percentage}%")
        print("THANK YOU ")
    def display_bar(self):
        print("========== PYTHON QUIZ ==========")
        print(f"number of questions the quiz contain {len(self.data)}")
        print(f"negative marks are NOT there")
        ans=input("START (y/n): ").lower()
        return ans
    def run(self):
        print("========== WELCOME TO FUN  QUIZ==========")
        flag=0
        try:
            n=int(input("ENTER THE ID : "))
            if(n in self.student_ids):
                while(True):
                    start=self.display_bar()
                    if(start in('y','n')):
                        if(start=='y'):
                            flag=1
                        else :
                            print("thank you")
                            return
                        break
                    else:
                        print("enter the valid input ")    
            else:
                print("Invalid id!\n your id is not found...")
        except ValueError:
            print("please enter the valid number  ")
        if(flag==1):
            for i in range(0,len(self.data)):
                ans=self.display_question(i)
                self.check_answer(ans,i)
                while True:
                    next=input("NEXT(y/n) : ")
                    if(next in ['y','n']):
                        break
                    else:
                        print("please enter the valid input... ")
                if(next=='y'):
                     continue
                else:
                    self.display_result(i)
                    return
                        
            self.display_result(len(self.data)-1)

q1=PythonQuiz()
q1.run()


    

                




        
    
