def solution(new_id):
	new_id = bigToSmall(new_id)
	new_id = removeSpecial(new_id)
	new_id = changeDuplicate(new_id)
	new_id = checkDotPosition(new_id)
	new_id = emptyToa(new_id)
	new_id = validateLength(new_id)
	new_id = extendLength(new_id)
	new_id = checkDotPosition(new_id)
 
	return new_id

def bigToSmall(id) :
	return id.lower()

def removeSpecial(id) :
	for c in id :
		if(c not in 'abcdefghijklmnopqrstuvwxyz0123456789-_.') :
			id = id.replace(c,'')
	return id

def changeDuplicate(id) :
	while '..' in id :
		id = id.replace('..', '.') 
	return id

def checkDotPosition(id) :
	if id and id[0] == '.':
		id = id[1:]
	if id and id[len(id)-1] == '.' :
		id = id[:(len(id)-1)]
	return id

def emptyToa(id) :
	if ' ' in id :
		id = id.replace(' ', 'a')
	return id
    
def validateLength(id) :
	id = id[:15]
	id = checkDotPosition(id)
	return id

def extendLength(id) :
	if len(id) == 0:
		return 'aaa'
	while len(id) <= 2 :
		id += id[len(id)-1]
	return id

solution("=.=")