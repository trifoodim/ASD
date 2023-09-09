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
lnk_ls.delete(12)
# lnk_ls.delete(55)
print("Список узлов после удаления одного элемента:")
lnk_ls.print_all_nodes()
