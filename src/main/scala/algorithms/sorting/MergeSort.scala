package algorithms.sorting

import scala.collection.mutable.ArrayBuffer

object MergeSort {

  def main(args: Array[String]): Unit = {

    val arr = Array(9, 8, 7, 6, 5, 4, 3, 2, 1)
    println(msort(arr).mkString(", "))
  }

  def msort(array: Array[Int]) : Array[Int] = {

    if (array.size > 1){
      merge( msort(array.slice(0, array.size/2)) , msort(array.slice(array.size/2, array.size)) )
    }
    else array
  }

  def merge(sortedArr1: Array[Int], sortedArr2: Array[Int]) : Array[Int]  = {

    val size1 = sortedArr1.size
    val size2 = sortedArr2.size
    var i = 0
    var j = 0

    val mergedArr = new ArrayBuffer[Int]()

    while( i<size1 && j<size2 ){

      if (sortedArr1(i) < sortedArr2(j)){
        mergedArr.append(sortedArr1(i))
        i=i+1
      }
      else{
        mergedArr.append(sortedArr2(j))
        j=j+1
      }
    }

    if (i<size1){

      (i until size1).foreach( ii=> mergedArr.append(sortedArr1(ii)) )

    }else if (j<size2){

      (j until size2).foreach( jj=> mergedArr.append(sortedArr2(jj)) )
    }

    mergedArr.toArray
  }

}
