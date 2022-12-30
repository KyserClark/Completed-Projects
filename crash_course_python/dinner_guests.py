guest_list = ['Jesus Christ', 'Thomas Jefferson', 'Elon Musk']

print(f"Hello {guest_list[0]}, you are invited to my dinner tonight.")
print(f"Hello {guest_list[1]}, you are invited to my dinner tonight.")
print(f"Hello {guest_list[2]}, you are invited to my dinner tonight.")
print(f"Dang, looks like {guest_list[0]} can't make it tonight.")
guest_list.pop(0)
print(f"How about you {guest_list[0]}, can you still make it?")
print(f"How about you {guest_list[1]}, can you still make it?")
print(f"Oh snap! Hey, {guest_list[0]}, and {guest_list[1]}, I found a bigger table, I'm going to invite more people.")

guest_list.insert(0,'Muhammad')
guest_list.insert(2,'Neil Armstrong')
guest_list.append('Steve Jobs')


print(f"Hello {guest_list[0]}, you are invited to my dinner tonight.")
print(f"Hello {guest_list[2]}, you are invited to my dinner tonight.")
print(f"Hello {guest_list[-1]}, you are invited to my dinner tonight.")
print(f"Dang, the new table won't arrive on time. I can only have two people over.")

first_pop = guest_list.pop()
print(f"Sorry {first_pop}, the new dinner tabele didn't come in time. I can no longer invite you to dinner.")
second_pop = guest_list.pop()
print(f"Sorry {second_pop}, the new dinner tabele didn't come in time. I can no longer invite you to dinner.")
third_pop = guest_list.pop()
print(f"Sorry {third_pop}, the new dinner tabele didn't come in time. I can no longer invite you to dinner.")

print(f"{guest_list[0]} and {guest_list[1]}, you guys are still invited. See you tonignt!")
#del guest_list[0]
#del guest_list[0]

print(len(guest_list))