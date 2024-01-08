guest_list = ["alex", "alice", "jeck"]
print(guest_list)

print(f"{guest_list[0]} can't attend dinner")

guest_list[0] = "max"
print(guest_list)

print("Find a bigger dining table")

guest_list.insert(0, "bob")
guest_list.insert(2, "lisa")
guest_list.append("chen")

print(guest_list)

print(f"{guest_list[0]}, it's an honor to invite you to dinner today")
print(f"{guest_list[1]}, it's an honor to invite you to dinner today")
print(f"{guest_list[2]}, it's an honor to invite you to dinner today")
print(f"{guest_list[3]}, it's an honor to invite you to dinner today")
print(f"{guest_list[4]}, it's an honor to invite you to dinner today")
print(f"{guest_list[5]}, it's an honor to invite you to dinner today")