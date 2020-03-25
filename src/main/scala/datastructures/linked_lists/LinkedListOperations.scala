package datastructures.linked_lists

object LinkedListOperations {

  def main(args: Array[String]): Unit = {

    val list1 = LinkedList()

    list1.insert(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(4)
    list1.insert(5)

    list1.remove()
    list1.remove()

    val idxOf1 =

    println(s"Index of '1': ${list1.searchValue(1)}")
    println(s"Index of '2': ${list1.searchValue(2)}")
    println(s"Index of '3': ${list1.searchValue(3)}")
    println(s"Index of '4': ${list1.searchValue(4)}")
    println(s"Index of '5': ${list1.searchValue(5)}")


  }
}
