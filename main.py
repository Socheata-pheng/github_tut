# print("hello world")
# ## i am working on the project

def move_last_index_to_first(list_):

  if not list_:
    return list_
  else:
    last_element = list_[-1]
    list_.remove(last_element)
    list_.insert(0, last_element)
    return list_


list_ = [5, 9, 4, 8,3,7]
new_list = move_last_index_to_first(list_) 
print(new_list)