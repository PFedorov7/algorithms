from collections import deque

def person_is_seller(name): 
	return name[-1] == 'n'

def search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print person + ' is a mango seller!'
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False

graph = {}
graph['you'] = ['Mike', 'Rose']
graph['Mike'] = ['Peep', 'Cotlin']
graph['Rose'] = ['Mann']
graph['Peep'] = ['friend']
graph['Cotlin'] = ['friend']
search("you")

