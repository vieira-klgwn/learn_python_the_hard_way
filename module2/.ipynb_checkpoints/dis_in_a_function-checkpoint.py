from dis import dis

dis(
'''
def decide():
    if True:
        print("This is true")
    return "We can do it"

var = decide()
print(var)
''')

