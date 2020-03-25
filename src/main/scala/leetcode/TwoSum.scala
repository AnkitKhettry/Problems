package leetcode

import utils.NoSolutionException

/**
  * Given an array of integers, return indices of the two numbers such that they add up to a specific target.
  * You may assume that each input would have exactly one solution, and you may not use the same element twice.
  *
  * Example:
  * Given nums = [2, 7, 11, 15], target = 9,
  * Because nums[0] + nums[1] = 2 + 7 = 9,
  * return [0, 1].
  */

//The solution is BAD. Time complexity : n^2.
// This can be done in nlog(n) by sorting the array, taking the elements one by one and performing a binary search on the remainder.
object TwoSum {

  /**
    * @param nums   Given nums
    * @param target Target Sum
    * @return       Required indices
    */
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {

    (0 until nums.size-1).foreach{
      i =>
        //val idx = binarySearch(sortedNums, i+1, size-1, (target-sortedNums(i)) )
        val idx = linearSearch(nums, (target-nums(i)), i+1)
        if (idx!= -1)
          return Array(i, idx)
    }

    throw new NoSolutionException()
  }


  /**
    *
    * @param arr Input array ref
    * @param target target to search
    * @return either index of target int or '-1'
    */
  def linearSearch(arr: Array[Int], target: Int, startIdx: Int): Int = {

    (startIdx until arr.size).foreach{

      i =>
        if (arr(i)==target)
          return i
    }
    return -1
  }
}
