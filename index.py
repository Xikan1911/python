def describe_pet(pet_name, animal_type='dog'):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet(pet_name='Sova')
describe_pet(pet_name='harry', animal_type='hamster')


def describe_pet(pet_name, animal_type='dog'):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#Dog for name Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

#hamster for name Garry.
describe_pet('harry','hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
