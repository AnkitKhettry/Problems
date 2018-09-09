package leetcode

import org.scalatest.{FlatSpec, Matchers}

class TwoSumTest extends FlatSpec with Matchers{

  "twoSum" should "pass for correctness for input array [2, 7, 11, 15] and target '9'" in {

    import TwoSum._

    twoSum(Array(3,2,4),6) should be (Array(1,2))
    twoSum(Array(2,7,11,15),9) should be (Array(0,1))
    twoSum(Array(11,2,15,7),9) should be (Array(1,3))
  }
}
