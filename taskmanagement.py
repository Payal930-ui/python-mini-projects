def task():
    tasks=[]
    print("Welcome to the the task management aap.....")
    totaL_task=int(input("How many task you want to add: "))
    for i in range(1,totaL_task+1):
        task_name=input("Enter the name of your task: ")
        tasks.append(task_name)
    print (f"Today's Task are\n{tasks}")
    while True:
        operation=int(input("Enter 1-Add\n 2-Update\n 3-Delete\n 4-View\n 5-Exit/Stop: "))
        if operation==1:
            add=input("Enter the task you want to add: ")
            task.append(add)
            print("task{add} has been added successfully!!")
        elif operation==2:
            update_val= input("Enter the task name you want to update: ")
            if update_val in tasks:
                up=input("Enter new task: ")
                ind=tasks.index(update_val)
                tasks[ind]
                print("UPdated task{up}")
        elif operation==3:
            del_val=input("Enter the task you want to delete: ")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print("Task{del_value} has been deleted successfully!!")
        elif operation==4:
            total_task=print(f"Total tasks given ={tasks}")
        elif operation==5:  
            print("Closing the program...") 
            break
        else:
            print("invalid input")
                                                                                                                                                                                                                                                                             
task()


