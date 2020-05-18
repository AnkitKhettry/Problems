package utils

class CycleFoundException(s: String) extends Exception{

  override def toString(): String = s"Cycle found in the graph : $s"
}
