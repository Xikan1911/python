current_users = ['bone', 'mEat', 'apple', 'orange', 'Slark', 'ask']
new_users = ['bone', 'meat', 'APPLE', 'orange', 'slark', 'Ask']
for new_user in new_users:
    if new_user.lower() in current_users :
         print("No correct name please replay this")
    else:
        print("Hello new user, " + new_user + ".")