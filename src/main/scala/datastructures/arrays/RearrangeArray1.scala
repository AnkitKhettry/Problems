package datastructures.arrays

import java.io.{BufferedReader, InputStreamReader}
import java.util

import scala.collection.mutable

/*
Rearrange array such that arr[i] >= arr[j] if i is even and arr[i]<=arr[j] if i is odd and j < i
  Given an array of n elements. Our task is to write a program to rearrange the array such that elements at even
  positions are greater than all elements before it and elements at odd positions are less than all elements before it.
Example:
  Input : arr[] = {1, 2, 3, 4, 5, 6, 7}
  Output : 4 5 3 6 2 7 1
 */

object RearrangeArray1 {

  def main(args: Array[String]): Unit = {

    val br = new BufferedReader(new InputStreamReader(System.in))

    val input = br.readLine()
    val arrInt = input.split(" ").map(_.toInt)

    println("Rearranged: " + rearrange(arrInt).mkString(" ") )
  }

  def rearrange(arrInt: Array[Int]) : Array[Int] = {

    val sortedArrInt = arrInt.sorted
    val arrSize = sortedArrInt.size

    val oddPositions = sortedArrInt.slice(0, arrSize/2 + 1)
    val evenPositions = sortedArrInt.slice(arrSize/2 + 1, arrSize)

    println(sortedArrInt.mkString(" "))
    println(oddPositions.mkString(" "))
    println(evenPositions.mkString(" "))

    val rearrangedArr = mutable.ListBuffer[Int](sortedArrInt : _*)

    (0 until oddPositions.size).foreach{

      i =>
        rearrangedArr(i*2) = oddPositions(oddPositions.size - i - 1)
    }

    (0 until evenPositions.size).foreach{

      i =>
        rearrangedArr((i*2) + 1) = evenPositions(i)
    }

    rearrangedArr.toArray
  }

}