texts = ['Hello', 'GTG', 'BRB', 'luv u', 'omw']

sent_messages = []


def show_messages(list):
    while list:
        used_object = list.pop(0)
        print(used_object)
        sent_messages.append(used_object)


show_messages(texts[:])

print(texts)
print(sent_messages)
