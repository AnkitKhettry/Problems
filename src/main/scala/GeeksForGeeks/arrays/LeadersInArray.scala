package GeeksForGeeks.arrays

import scala.collection.mutable.ArrayBuffer


/**
  *  An element of array is leader if it is greater than or equal to all the elements to its right side.
  *  Also, the rightmost element is always a leader.
  *  Given an array of positive integers. Your task is to find the leaders in the array.
  */

object LeadersInArray {

  def main(args: Array[String]): Unit = {

    val arr = Array(16, 17, 4, 3, 5, 2)
    println(getLeaders(arr).mkString(","))
  }

  def getLeaders(array: Array[Int]): Array[Int] = {

    var i = array.size - 1
    var max = array(i)
    val leaders = ArrayBuffer[Int]()

    while (i>=0){
      if (array(i) >= max){

        max = array(i)
        leaders.prepend(array(i))
      }
      i = i-1
    }

    leaders.toArray
  }
}
