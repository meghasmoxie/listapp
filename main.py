to_do_list = []

def show_help():
    print("What do you want to accomplish today fellow superheroine?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' to see your current list.
    """)

def show_list():
    print("Here's what you will accomplish today you awesome superheroine:")
    for item in to_do_list:
        print(item)

def add_to_list(new_item):
    to_do_list.append(new_item)
    print("Added '{}'. List now has {} number of items.".format(new_item, len(to_do_list)))

show_help()

while True:
    new_item = input("> ")
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)

show_list()
