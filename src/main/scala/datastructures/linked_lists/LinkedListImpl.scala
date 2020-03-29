package datastructures.linked_lists

class LinkedList(var head: Option[Node]) {

  /**
    * Inserts a node with the given value at the beginning of the list.
    * @param nodeValue Value to be inserted
    */
  def insert(nodeValue: Int) = {

    val newHead = new Node(nodeValue, head)
    head = Some(newHead)
  }

  /**
    * Removes an element from the top of the LL
    */
  def remove() = {

    val newHead = head.flatMap(_.getNext)
    this.head = newHead
  }

  /**
    * Traverses the entire LL while printing the values stored in each node.
    */
  def traverseLinkedList() = {

    var current = head
    while (current.isDefined){

      print (current.get.getValue + " ")
      current = current.flatMap(_.getNext)
    }
    println
  }

  /**
    * Searches for a value in the LL
    * @param value value to be searched
    * @return Index of the node with the value. -1 if the value was not found
    */
  def searchValue(value: Int) : Int = {

    var current = head
    var idx = 0
    while (current.isDefined){

      if (current.get.getValue == value)
        return idx
      current = current.flatMap(_.getNext)
      idx = idx + 1
    }

    return -1
  }
}

object LinkedList{

  def apply() = new LinkedList(None)
}

class Node(value: Int, next: Option[Node]){

  def getValue = value
  def getNext = next
}

object Node{

  def apply(value: Int, next: Option[Node]): Node = new Node(value, next)
}