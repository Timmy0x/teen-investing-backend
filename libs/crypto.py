def hash(data):
	from hashlib import blake2b
	string = blake2b(data.encode()).hexdigest()
	return string