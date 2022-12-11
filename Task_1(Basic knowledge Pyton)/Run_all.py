import Task_1
import Task_2
import Task_3
import Task_4
import Task_5
import Task_1_extra

print("----------------------Task #1----------------------")
first_task = []
first_task.append([1, 2, 'a', 'b'])
first_task.append([1, 'a', 'b', 0, 15])
first_task.append([1, 2, 'aasf', '1', '123', 123])
for list in first_task:
    print(f"Filtering list: {list}, gives us {Task_1.filter(list)}")
print("")

print("----------------------Task #2----------------------")
second_task = []
second_task.append("stress")
second_task.append("sTreSS")
second_task.append("abbsas")
for string in second_task:
    print(f"Input string: {string}, gives us {Task_2.first_non_repeating_letter(string)}")
print("")

print("----------------------Task #3----------------------")
third_task = []
third_task.append(16)
third_task.append(832)
third_task.append(164867)
third_task.append(4862762)
for integer in third_task:
    print(f"Digital root of {integer} is {Task_3.digital_root(integer)}")
print("")

print("----------------------Task #4----------------------")
forth_task = []
forth_task.append(([1, 3, 6, 2, 2, 0, 4, 5], 5))
forth_task.append(([item for item in range(16)], 16))
for list, target in forth_task:
    print(f"All pairs for target {target} is {Task_4.get_pair_for_target(list, target)}")
print("")

print("----------------------Task #5----------------------")
fifth_task = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print("Raw string:", fifth_task)
print("Formatted string:", Task_5.format_string(fifth_task))
print("")

print("----------------------Task #1 Extra----------------------")
first_task_extra = []
first_task_extra.append(48)
first_task_extra.append(513)
first_task_extra.append(2017)
first_task_extra.append(9)
first_task_extra.append(111)
first_task_extra.append(531)
for value in first_task_extra:
    print(f"Checking next rearranging bigger value of {value} gives {Task_1_extra.bigger(value)}")
print("")
