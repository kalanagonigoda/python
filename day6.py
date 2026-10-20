# list and function
#a list stores marks
marks=[85,90,78,92,88]
print(f"my marks:{marks}")

#add new mark
marks.append(95)
print(f"after adding:{marks}")

#access element
print(f"first mark:{marks[0]}")
print(f"total subjects:{len(marks)}")

#loop through list
total =0
for m in marks:
    total += m
    print(f"total:{total}")
    print(f"average:{total/len(marks):.2f}")

    #function
    # function calculate average
    def calculate_average(numbers):
        """calculate average list"""
        if len(numbers)==0:
            return 0
        return sum(numbers)/len(numbers)

    def find_max_min(numbers):
        """find max and min"""
        return max(numbers),min(numbers)
    #use the functions
    avg=calculate_average(marks)
    max_mark,min_mark=find_max_min(marks)

    print(f"\nusing function:")
    print(f"average is:{avg:.2f}")
    print(f"max:{max_mark},min:{min_mark}")

    #to do list
    todo=[]
    todo.append("learn python")
    todo.append("push to github")
    todo.append("post on linekdin")

    print("\nmy to do list:")

    for i,task in enumerate(todo,1):
        print(f"{i}.{task}")