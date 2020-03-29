package datastructures.stacks

import scala.collection.mutable

object StackOperations {

  def main(args: Array[String]): Unit = {

    val stack1 = mutable.Stack[Int]()

    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.push(5)

    println(s"Deleting value from top: ${stack1.pop()}")
    println(s"Element current at the top of the stack: ${stack1.top}")
  }
}
