def to_do_list(lists):
    to_do = {}
    what_to_do = input("What would you like to do?")
    what_day = input("What day?")
    if what_to_do == "add":
        what_to_add = [input("What would you like to add to the to-do list?")]
        to_do[what_day] = what_to_add
        print(to_do_list(lists))
    elif what_to_do == 'get':
        task_request = input("Tasks for what day?")
        if task_request in to_do.keys():
            print("hi")


hi = "TO DO LIST"
to_do_list(hi)
# I received help from James, but it turns out that we were both wrong... I'm still struggling a bit with the code
