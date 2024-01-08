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

print("Today's dinner is only enough for two people")

pop_guset = guest_list.pop(0)
print(f"{pop_guset}, I'm very sorry that I can't ask you to come to dinner today.")

pop_guset = guest_list.pop(0)
print(f"{pop_guset}, I'm very sorry that I can't ask you to come to dinner today.")

pop_guset = guest_list.pop(0)
print(f"{pop_guset}, I'm very sorry that I can't ask you to come to dinner today.")

pop_guset = guest_list.pop(0)
print(f"{pop_guset}, I'm very sorry that I can't ask you to come to dinner today.")

print(f"{guest_list[0]}, it's an honor to invite you to dinner today")
print(f"{guest_list[1]}, it's an honor to invite you to dinner today")


del guest_list[1]
del guest_list[0]

print(guest_list)

