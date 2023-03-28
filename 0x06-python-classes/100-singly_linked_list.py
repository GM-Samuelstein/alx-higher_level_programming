#!/usr/bin/python3
"""
Module 100-singly_linked_list.py.

This module has two classes and zero functions.

Classes:
    Node:
        A class that defines a node of a singly linked list.
    
    SinglyLinkedList:
        A class representing a singly linked list.

Functions:
    This module has no functions.
"""


class Node:
    """
    A class that defines a node of a singly linked list.

    Attributes:
        data (int): A private instance attribute.
            The data stored in the new node.

        next_node (Node) : A private instance attribute.
            The next node in the linked list that the current node points to.

    Methods:
        __init__(self, data, next_node=None) : 
            Initializes a new Node object with the given attributes.
        
        data(self) : @property
            Gets the property `data`.
        
        data(self, value) : @data.setter
            Sets the property `data`.

        next_node(self) : @property
            Gets the property `next_node`.

        next_node(self, value) : @next_node.setter
            Sets the property `next_node`.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node object with the given attributes.

        Args:
            data (int): A private instance attribute.
                The data stored in the new node.

            next_node (Node) : A private instance attribute.
                The next node in the linked list that the current node
                points to. Its default value = None.

        """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """
        Gets the property `data`.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the property `data`.

        Args:
            value (int) : A private instance attribute.
                The data stored in the new node.

        Raises:
            TypeError : Exception
                If `value` is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    
    @property
    def next_node(self):
        """
        Gets the property `next_node`.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the property `next_node`.

        Args:
            value (Node) : A private instance attribute.
                The next node in the linked list that the current node
                points to.

        Raises:
            TypeError : Exception
                If `value` is not a Node object.
        """
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value
  

class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head (Node) : Private instance attribute.
            The head of the singly linked list.

    Methods:
        __init__(self) : 
            Initializes a new singly linked list with the given attribute.

        sorted_insert(self, value) :
            Inserts a new `Node` into the singly liked list.
    """

    def __init__(self):
        """
        Initializes a new singly linked list with the given attribute.

        Args:
            head (Node) : Private instance attribute.
                The head of the singly linked list.
        """
        self.__head = None
    
    def sorted_insert(self, value):
        """
        Inserts a new Node into the singly liked list.
        
        The new Node is inserted in the correct sorted position in the
        list (increasing order).

        Args:
            value (Node) :
                The new node to be inserted in the singly linked list.
        """
        new_node = Node(value)
        