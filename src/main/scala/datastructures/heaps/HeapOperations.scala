package datastructures.heaps

object HeapOperations {

  def main(args: Array[String]): Unit = {

    val maxHeap = MaxHeap()
    maxHeap.insert(1)
    maxHeap.insert(2)
    maxHeap.insert(3)
    maxHeap.insert(4)
    maxHeap.insert(5)
    maxHeap.insert(6)
    maxHeap.insert(7)
    maxHeap.insert(8)

    println("Max element: "+maxHeap.getTopElement)

    while(!maxHeap.isEmpty){
      print(s"${maxHeap.getTopElement} ")
      maxHeap.removeTop()
    }
  }
}
