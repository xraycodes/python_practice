def greet_pythons(items: list) -> None:
    greeting = 'Hello'

    def make_greeting(item: str) -> str:
        # greeting = 'Hi'
        return f'{greeting} {item}'
        

    for item in items:
        print(make_greeting(item))
    print(f'Inside greet_pythons,`greeting` is {greeting}')


names = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greet_pythons(names)
