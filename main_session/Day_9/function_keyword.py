#Keyword args

def hello(greet,title,first,last):
    print(f"{greet} {title} {first} {last}")

hello("Mr","Hello","Mukesh","Kumar")


hello("Hello","Mr",last="Kumar",first="Mukesh")

hello(last="Kumar",first="Mukesh",title="Mr",greet="Hi")