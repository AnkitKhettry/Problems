package datastructures.queues

import scala.collection.mutable

object QueueOperations {

  def main(args: Array[String]): Unit = {

    val queue1 = mutable.Queue[Int]()

    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    queue1.enqueue(4)
    queue1.enqueue(5)

    println(s"Removing first element in the queue: ${queue1.dequeue()}")
    println(s"Element at the front of the queue: ${queue1.front}")
  }
}
