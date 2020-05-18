package GeeksForGeeks.arrays

import scala.collection.mutable.ArrayBuffer

/**
  * https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0/?track=md-arrays&batchId=144
  */
object KadanesAlgorithm {

  def main(args: Array[String]): Unit = {

    println(findMaxSum( Array(1, 2, 3, -2, 5) ))
    println(findMaxSum( Array(-1, -2, -3, -4) ))
  }

  def findMaxSum(array: Array[Int]): Int ={

    val size = array.size
    val subArraySum = ArrayBuffer.fill( size, size )(0)

    var maxSum = Integer.MIN_VALUE

    (0 until size).foreach{
      x =>
        subArraySum(0)(x) = array(x)
        maxSum = Math.max(maxSum, array(x))
    }

    (2 to size).foreach{
      numElements =>
        val k = numElements - 1
        (numElements to size).foreach{
          arrayIdx =>
            val i = arrayIdx - 1

            subArraySum(k)(i) = array(i) + subArraySum(k-1)(i-1)

            if (subArraySum(k)(i) > maxSum) maxSum = subArraySum(k)(i)
        }
    }

    return maxSum
  }
}
