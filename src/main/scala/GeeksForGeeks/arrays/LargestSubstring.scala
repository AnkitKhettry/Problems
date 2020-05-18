package GeeksForGeeks.arrays

object LargestSubstring {

  def main(args: Array[String]): Unit = {

    println(getLargestSubstring("aabccccccdeeefghijjjjjjjjjjk"))
  }

  def getLargestSubstring(str: String): Int ={

    if (str.isEmpty)
      return 0

    var i = 1
    var currentElem = str.charAt(0)
    var max = 1
    var currentCount = 1
    val size = str.size
    while(i<size){

      if (currentElem == str.charAt(i)){

        currentCount = currentCount+1
        max = Math.max(currentCount, max)
      }else{

        currentElem = str(i)
        currentCount = 1
      }
      i = i+1
    }
    return max
  }
}
