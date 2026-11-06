class TodoListManager:
    def __init__(self):
        self.tasks=[]
    def add_task(self):
        name=input("ENTER THE NAME OF THE TASK NAME : ")
        name=name.strip()
        if not name:
            return 
        task={"name":name,
              "compeleted":False}
        self.tasks.append(task)
        print("THE TASK IS SUCESSFULLY ADDED....")
    def view_tasks(self):
        if not self.tasks:
            print("THERE ARE NO TASKS TODAY")
        print("==================================")
        print("||     TARGETS OF THE DAY       ||")
        print("==================================")
        n=len(self.tasks)
        list_tasks=self.tasks
        index=0
        for i in list_tasks:
            index+=1

            if(i["compeleted"]):
                k="compeleted"
            else:
                k="pending"
            print(f"{index}.    {i["name"]}     :       {k} ")
    def complete_task(self):
        self.view_tasks()
        if not self.tasks:
            return
        try:
            number=int(input("ENTER THE TASK INDEX : "))
            if(1<=number and number<=len(self.tasks)):
                flag=0
                while(flag==0):
                    status=input("ENTER THE STATUS : (y/n)")
                    status=status.lower()
                    if(status in ['y','n']):
                        if(status=='y'):
                            self.tasks[number-1]["compeleted"]="compeleted"
                        else:
                            self.tasks[number-1]["compeleted"]="pending"
                        flag=1
            else:
                print("INVALIED TASK NUMBER ")
        except ValueError:
            print("Please enter a valid number") 
    def delete_task(self):
        self.view_tasks()
        if not self.tasks:
            return 
        try:
            number=int(input("enter task number to delete : "))
            tasks=self.tasks
            
            if(number>=1 and number<=len(tasks)):
                task=self.tasks.pop(number-1)
                print(f"DELETED TASK : {task["name"]}")
            else:
                print("you entered the invalid index ")
        except ValueError:
            print("please enter the valid number ")  
    def run(self):
         while(True):
            print("\n===== TO-DO LIST MANAGER =====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Exit")
            try:
                choice=int(input("ENTER YOUR CHOICE : "))
                if(choice==1):
                    self.add_task()
                elif(choice==2):
                    self.view_tasks()
                elif(choice==3):
                    self.complete_task()
                elif(choice==4):
                    self.delete_task()
                elif(choice==5):
                    print("=======================================================")
                    print("===== THANK YOU FOR USEING THE TO DO LIST MANAGER =====")
                    print("=======================================================")
                    break
                else:
                    print()
                    print("YOU ENTERED  NUMBER  IS IN OUT OF RANGE 1")
                    print()
            except ValueError:
                print("==============================")
                print("YOU ENTERED THE INVALID NUMBER")
                print("==============================")
                

T=TodoListManager()
T.run()

            
            



                

        
        
