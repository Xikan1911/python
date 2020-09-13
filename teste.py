unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifyting user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe folloving users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())