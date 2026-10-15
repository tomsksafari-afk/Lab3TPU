values = (1, 2, 3, 4, 5, 6)
after_lst = list(values)
after_tpl = tuple(values)

print(type(after_lst), id(after_lst))
print(type(after_tpl), id(after_tpl))

id_before = id(after_lst)
after_lst[0] = 999
print(id_before == id(after_lst))          # id не изменился

 
tpl_new = (999,) + after_tpl[1:]         
print(id(after_tpl) == id(tpl_new))        # id изменился
