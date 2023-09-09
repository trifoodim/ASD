from class_linked_list import LinkedList, Node


n1 = Node(12)
n2 = Node(55)
n3 = Node(7)
n4 = Node(55)
n5 = Node(20)

lnk_ls = LinkedList()
lnk_ls.add_in_tail(n1)
lnk_ls.add_in_tail(n2)
lnk_ls.add_in_tail(n3)
lnk_ls.add_in_tail(n4)
lnk_ls.add_in_tail(n5)

print("Список узлов до удаления одного элемента:")
lnk_ls.print_all_nodes()
ls = lnk_ls.find_all(55)

if not ls:
    print("Искомых значений в списке нет.")
else:
    print("Список всех найденных узлов:")
    for i, elem in enumerate(ls):
        print(f'{i}, {elem.value}')
