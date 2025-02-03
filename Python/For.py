
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

# Create a simple Collection
users = {'admin': 'active', 'root': 'active', 'user': 'inactive', 'guest': 'inactive', 'test': 'inactive'}

# Iterate over a copy of the dictionary
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)