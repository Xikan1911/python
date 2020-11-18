#ivent 8.3
def make_shirt(t_size, t_text):
    """Outout info for tshitr and size , text"""
    print(f"\nMe need a t-shirt a size {t_size}.")
    print(f"\nMe need a new text on t-shirt {t_text}.")
make_shirt('52' , 'I love the coding on Python')
#ivent 8.4
def make_shirt(t_size='L' , t_text='I love python'):
    """output info for t-shitr and size , text"""
    print(f"\nMe need a t-shirt a size {t_size} and text: {t_text}")
    print(f"\n")
make_shirt(t_size='L' , t_text='I love python')
make_shirt('XXL' , 'I dont love python')
#ivent 8.5
def describy_city(city_name='Kolomna , Moscow , Murom', capital_name='Russian'):
	"""Output info for city and capital"""
	print(f"\n{city_name} is in {capital_name}")
describy_city(capital_name='Russian' , city_name='Kolomna')
describy_city(city_name='Moscow' , capital_name='Russian')
describy_city(city_name='Murom' , capital_name='Russian')
describy_city('Florencia' , 'Itali')
