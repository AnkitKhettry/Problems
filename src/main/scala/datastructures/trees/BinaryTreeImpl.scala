package datastructures.trees

import datastructures.trees.Traversal.Traversal

import scala.collection.mutable


class BinarySearchTree() {

  var root: Option[Node] = None

  def getRoot = root

  def insertValue(value: Int) = {

    if (!root.isDefined)
      root = Some(Node(value))
    else{

      _insert(root.get, value)
    }
  }

  def searchValue(value: Int): Boolean = {
    _search(root, value)
  }

  def traverse(traverseType: Traversal) = {
    traverseType match {
      case Traversal.inOrder => _inOrderTraversal(root)
      case Traversal.preOrder => _preOrderTraversal(root)
      case Traversal.postOrder => _postOrderTraversal(root)
      case Traversal.levelOrder => _levelOrderTraversal(root)
    }
  }

  def removeValue= ???
  def balance = ???

  //Level order traversal == Bredth first
  private def _levelOrderTraversal(node: Option[Node]) : Unit = {

    if (!node.isDefined){
      println("Empty tree!!")
      return
    }

    val queueBuffer = mutable.Queue(node.get)
    while (!queueBuffer.isEmpty){
      val currNode = queueBuffer.dequeue()
      print(currNode.getValue + " ")
      val children = Seq(currNode.getLeft, currNode.getRight).flatten
      queueBuffer.enqueue(children : _*)
    }
  }

  private def _inOrderTraversal(node: Option[Node]) : Unit = {

    if(node.isDefined){
      _inOrderTraversal(node.get.getLeft)
      print(node.get.getValue+" ")
      _inOrderTraversal(node.get.getRight)
    }
  }

  private def _preOrderTraversal(node: Option[Node]) : Unit = {

    if(node.isDefined){
      print(node.get.getValue+" ")
      _preOrderTraversal(node.get.getLeft)
      _preOrderTraversal(node.get.getRight)
    }
  }

  private def _postOrderTraversal(node: Option[Node]): Unit= {

    if(node.isDefined){
      _postOrderTraversal(node.get.getLeft)
      _postOrderTraversal(node.get.getRight)
      print(node.get.getValue+" ")
    }
  }

  private def _insert(parentNode: Node, value: Int) : Unit = {

    if (value < parentNode.getValue){
      if (parentNode.left.isDefined)
        _insert(parentNode.left.get, value)
      else parentNode.setLeft( Node(value) )
    }
    else {
      if (parentNode.right.isDefined)
        _insert(parentNode.right.get, value)
      else parentNode.setRight( Node(value) )
    }
  }

  private def _search(node: Option[Node], value: Int) : Boolean = {
    if (!node.isDefined) false
    else if (node.get.getValue == value) true
    else{
      if (value<node.get.getValue) _search(node.get.getLeft, value)
      else _search(node.get.getRight, value)
    }
  }

}

object BinarySearchTree{

  def apply(): BinarySearchTree = new BinarySearchTree()
}

class Node(value: Int, var left: Option[Node], var right: Option[Node]) {

  def getValue = value

  def getLeft = left

  def getRight = right

  def setLeft(node: Node) = {
    this.left = Some(node)
  }
  def setRight(node: Node) = {
    this.right = Some(node)
  }
  def unsetLeft() = {
    this.left = None
  }

  def unsetRight() = {
    this.right = None
  }

}

object Node{

  def apply(value: Int): Node = new Node(value, None, None)

  implicit class OptionalNodeOps(n: Option[Node]){

    def height() : Int = {

      if (n.isDefined)
        1 + Math.max(n.get.getLeft.height() , n.get.getRight.height())
      else 0
    }

  }

}

object Traversal extends Enumeration
{
  type Traversal = Value

  // Assigning values
  val inOrder, preOrder, postOrder, levelOrder = Value
}