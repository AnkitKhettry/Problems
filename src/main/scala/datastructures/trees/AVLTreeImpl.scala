package datastructures.trees

class AVLTree() extends BinarySearchTree() {

  override def insertValue(value: Int) = {

    if (!root.isDefined)
      root = Some(Node(value))
    else
      root = Some(_insert(root.get, value))
  }

  private def _insert(parentNode: Node, value: Int) : Node = {

    if (value < parentNode.getValue){
      if (parentNode.left.isDefined)
        parentNode.setLeft( _insert(parentNode.left.get, value) )
      else
        parentNode.setLeft( Node(value) )
    }
    else {
      if (parentNode.right.isDefined)
        parentNode.setRight( _insert(parentNode.right.get, value) )
      else
        parentNode.setRight( Node(value) )
    }
    val leftSubnodeHeight = parentNode.left.height()
    val rightSubnodeHeight = parentNode.right.height()
    val heightDiff = rightSubnodeHeight - leftSubnodeHeight

    val balancedNode =
      if (heightDiff < -1){

        if (value > parentNode.left.get.getValue)
          parentNode.setLeft(rotateLeft(parentNode.left.get))

        rotateRight(parentNode)

      }else if (heightDiff > 1){

        if (value < parentNode.right.get.getValue)
          parentNode.setRight(rotateRight(parentNode.right.get))

        rotateLeft(parentNode)

      }else parentNode

    return balancedNode
  }

  def rotateRight(node: Node) : Node = {

    val tempNode = node.getLeft.get
    if (tempNode.getRight.isDefined) node.setLeft(tempNode.getRight.get) else node.unsetLeft()
    tempNode.setRight(node)
    tempNode
  }

  def rotateLeft(node: Node) : Node = {

    val tempNode = node.getRight.get
    if (tempNode.getLeft.isDefined) node.setRight(tempNode.getLeft.get)  else node.unsetRight()
    tempNode.setLeft(node)
    tempNode
  }
}
object AVLTree{
  def apply(): AVLTree ={
    new AVLTree()
  }
}