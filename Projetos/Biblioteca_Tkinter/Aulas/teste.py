this = 'users'
this1 = [this[count] for count in range(0,len(this)) if count != len(this)-1]
this = ''.join(this1)
print(this)