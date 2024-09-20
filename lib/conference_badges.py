def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names] 

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {i}!" for i, name in enumerate(names, start =1)]

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)

    rooms = assign_rooms(names)
    for room in rooms:
        print(room)
       
    
