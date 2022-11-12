from pprint import pprint

new_dict = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(16)]

pprint(new_dict)