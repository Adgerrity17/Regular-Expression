
#Finding patterns in text without regular expressions
import re #import regular expression library

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') #matching multiple groups
mo = batRegex.search('And the Batmobile lost a wheel and the joker got away')
print(mo.group())
print(mo.group(1))

batRegex1 = re.compile(r'Bat(wo)?man') #optional matching with the ?
mo1 = batRegex1.search('The Adventures of Batwoman')
print(mo1.group())

batRegex2 = re.compile(r'Bat(wo)*man') #matching more than one itteration with the *
mo2 = batRegex2.search('The Adventures of Batwowowowoman')
print(mo2.group())

batRegex3 = re.compile(r'Bat(wo)+man') #matching one or more with +. The group preceding the + must be included
mo3 = batRegex3.search('The Adventures of Batman') #this is false because it requires the wo
print(mo3 == None)




