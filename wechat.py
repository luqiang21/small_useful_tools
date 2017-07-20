'''import itchat and login'''
import itchat
itchat.login()
friends = itchat.get_friends(update=True)[0:]

male = female = other = 0
for i in friends[1:]:
    gender = i["Sex"]
    if gender == 1:
        male += 1
    elif gender == 2:
        female += 1
    else:
        other += 1

total = len(friends[1:])
print 'male friends:', male, float(male)/total*100, '%'
print 'female friends:', female, float(female)/total*100, '%'
print 'other', other, float(other)/total*100, '%'
