favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

if 'andrey' not in favorite_languages.keys():
    print("Andrey, please take our poll!")

if 'jura' not in favorite_languages.keys():
    print("Jura, please take our poll!")

friends = ['jen', 'sarah', 'phil']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")