package algorithms.searching

object BinarySearch {

  def main(args: Array[String]): Unit = {
    val arr1 = Array(1,2,3,4,5,6,7)
    println(bSearch(3, arr1))

    val arr2 = Array(55, 95, 121, 340)
    println(bSearch(242, arr2))

    val arr3 = Array(55, 95, 121, 340)
    println(bSearch(41, arr3))

    val arr4 = Array(55, 95, 121, 340)
    println(bSearch(441, arr4))
  }

  def bSearch(value: Int, arr: Array[Int]): Int = {

    var start = 0
    var end = arr.size - 1
    var mid = start + ((end-start)/2)

    while (end > start){

      val midVal = arr(mid)

      if (arr(end) == value)
        return end
      else if (arr(start) == value)
        return start
      else if (arr(mid) == value)
        return mid
      else{
        if ((end - start)<2)
          return -1
        if (value < midVal)
          end = mid
        else
          start = mid
        mid = start + ((end-start)/2)
      }
    }

    return -1
  }
}
