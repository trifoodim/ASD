from class_linked_list import LinkedList, Node


n1 = Node('a2')
n2 = Node('a3')
n3 = Node('a4')
n4 = Node('a5')
n5 = Node('a6')

new_node = Node('a7')
new_node_1 = Node('a8')

lnk_ls = LinkedList()
lnk_ls.add_in_tail(n1)
lnk_ls.add_in_tail(n2)
lnk_ls.add_in_tail(n3)
lnk_ls.add_in_tail(n4)
lnk_ls.add_in_tail(n5)

print("Список узлов до вставки нового элемента:")
lnk_ls.print_all_nodes()

lnk_ls.insert(afterNode=n3, newNode=new_node)
print("Список узлов после вставки нового элемента:")
lnk_ls.print_all_nodes()


lnk_ls.insert(afterNode=None, newNode=new_node_1)
print("Список узлов после вставки элемента в начало списка:")
lnk_ls.print_all_nodes()
