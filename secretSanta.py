import random

group_size = 2
groups = []
people = input("Enter Names (seperated by a comma): ").split(",")
print(people)
if len(people) % group_size == 0:
    random.shuffle(people)
    Cgroup, Csize = [], 0
    for person in people:
        if Csize >= group_size:
            print(f"adding {Cgroup}")
            groups.append(Cgroup)
            Cgroup.clear()
            Csize = 0
        Cgroup.append(person)
        Csize += 1
    groups.append(Cgroup)
print(groups)
