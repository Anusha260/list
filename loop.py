print('welcome to state bank of india')
print('please insert your card')
print('1.english')
print('2.telugu')
print('3.hindi')
language=int(input('please select your language'))
pin=int(input('please enter pin number'))
print('1.withdrawl')
print('2.deposite')
print('3.balance enquiry')
print('4.pin change')
print('5.exit')
transaction=input('please select your transaction')
if(transaction=='1'):
	print('1.saving')
	print('2.current')
	type=int(input('choose account type'))
	amount=int(input('please enter amount'))
	if amount<=10000:
		print('please collect your cash')
	else:
		print('you do not have sufficient balance try later')
if(transaction=='2'):
	deposite=int(input('please enter deposite amount'))
	if deposite<=20000:
		print('your money successfully deposited')
	else:
		print('this money more than deposited limit')
if(transaction=='3'):
	receipt=input|('do you want receipt')
	if(receipt=='yes'):
		print('please collect your receipt')
	else:
		print('thank for using...')
if(transaction=='4'):
	oldpin=int(input('enter your old pin'))
	if(oldpin==1234):
		newpin=input('do you want to old pin')
		if(newpin=='yes'):
			print('successfully change yoir pin')
		else:
			print('please enter valid pin number')
	else:
			print('enter valid old pin number')
if(transaction=='5'):
			print(exit)