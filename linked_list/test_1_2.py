from class_linked_list import LinkedList, Node


n1 = Node(12)
n2 = Node(55)
n3 = Node(7)
n4 = Node(55)
n5 = Node(20)
n6 = Node(12)
n7 = Node(12)
n8 = Node(12)

lnk_ls = LinkedList()
lnk_ls.add_in_tail(n1)
lnk_ls.add_in_tail(n2)
lnk_ls.add_in_tail(n3)
lnk_ls.add_in_tail(n4)
lnk_ls.add_in_tail(n5)
lnk_ls.add_in_tail(n6)
lnk_ls.add_in_tail(n7)
lnk_ls.add_in_tail(n8)


# print("Список узлов до удаления одного элемента:")
# lnk_ls.print_all_nodes()
#
# print(f"Список узлов после удаления всех элементов:")
# lnk_ls.delete(12, True)
# lnk_ls.print_all_nodes()

# print("Список узлов после удаления двух элементов:")
# lnk_ls.delete(55, True)
# lnk_ls.print_all_nodes()

linked_list_1 = LinkedList()
linked_list_1.delete(12, True)