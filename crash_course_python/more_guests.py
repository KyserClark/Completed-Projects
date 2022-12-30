guest_list = ['Jesus Christ', 'Thomas Jefferson', 'Elon Musk']

print(f"Hello {guest_list[0]}, you are invited to my dinner tonight.")
print(f"Hello {guest_list[1]}, you are invited to my dinner tonight.")
print(f"Hello {guest_list[2]}, you are invited to my dinner tonight.")
print(f"Dang, looks like {guest_list[0]} can't make it tonight.")
print(f"How about you {guest_list[1]}, can you still make it?")
print(f"How about you {guest_list[2]}, can you still make it?")
print(f"Oh snap! Hey, {guest_list[1]}, and {guest_list[2]}, I found a bigger table, I'm going to invite more people.")

guest_list.insert(0,'Muhammad')
guest_list.insert(2,'Neil Armstrong')
guest_list.append('Steve Jobs')

print(f"Hello {guest_list[0]}, you are invited to my dinner tonight.")
print(f"Hello {guest_list[2]}, you are invited to my dinner tonight.")
print(f"Hello {guest_list[-1]}, you are invited to my dinner tonight.")