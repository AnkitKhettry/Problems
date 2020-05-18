package datastructures.trees

import scala.collection.mutable

//Geeks for Geeks

object BinaryTreeOperations {

  def main(args: Array[String]): Unit = {

    val bTree = AVLTree()
    bTree.insertValue(7)
    bTree.insertValue(2)
    bTree.insertValue(3)
    bTree.insertValue(1)
    bTree.insertValue(4)
    bTree.insertValue(6)
    bTree.insertValue(5)

    println(bTree.searchValue(6))
    println(bTree.searchValue(8))

    println("In Order traversal: ")
    bTree.traverse(Traversal.inOrder)
    println

    println("Pre Order traversal: ")
    bTree.traverse(Traversal.preOrder)
    println

    println("Post Order traversal: ")
    bTree.traverse(Traversal.postOrder)
    println()

    println("Level Order traversal: ")
    bTree.traverse(Traversal.levelOrder)
    println()

    println("Height of tree: "+bTree.getRoot.height())
  }
}
