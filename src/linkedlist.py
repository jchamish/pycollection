from typing import Any, Tuple, List, Optional


class Node:

    def __init__(self, data: Any = None, next_node: Any = None) -> None:
        self.next = next_node
        self.data = data


class LinkedList:
    """
    Linked List Object
    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.height = 0

    def insert(self, data: Any) -> None:
        """
        Add an element into the linked list
        :rtype: object
        """

        node: Node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.height = 1
        else:
            self.tail.next = node
            self.tail = node
            self.height += 1

    def __str__(self) -> str:
        return "Data: " + " -> ".join([str(i) for i in self._items])

    @property
    def _items(self) -> Tuple:
        """
        will return all the items
        :return:
        """
        items: List[Any] = []

        if self.head is None:
            return ()

        current_node: Node = self.head
        while current_node is not None:
            items.append(current_node.data)
            current_node = current_node.next

        return tuple(items)

    def pop(self, index: int) -> Optional[Any]:
        """
        removes an element from the linked list will return the element
        :param index:
        :return:
        """
        if index > self.height or self.head is None:
            return None

        if index == 0:
            element: Any = self.head.data
            self.head = self.head.next
            return element
        elif index == self.height-1:
            element: Any = self.tail.data
            self.tail = self.tail.next
            return element
        else:
            current_node = self.head.next
            previous_node = None
            element: Any = None
            i: int = 1
            while current_node is not None:
                if self.height-1 == i:
                    break
                if index == i:
                    element = current_node.data
                    previous_node.next = current_node.next
                    break
                previous_node = current_node
                current_node = current_node.next
                i += 1
            return element

    def __repr__(self) -> str:
        return "{}{}"
