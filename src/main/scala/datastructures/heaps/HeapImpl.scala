package datastructures.heaps

import utils.EmptyHeapException

import scala.collection.mutable

//https://www.youtube.com/watch?v=WCm3TqScBM8

abstract class Heap(heap : mutable.ArrayBuffer[Int]) {

  val ROOT_INDEX = 0

  def insert(value: Int): Unit
  def removeTop() : Unit
  def getTopElement : Int = if (!heap.isEmpty) heap(ROOT_INDEX) else throw new EmptyHeapException()
  def isEmpty = heap.isEmpty

  def getParentIndex(childIdx: Int) = (childIdx-1)/2
  def getLeftChildIndex(parentIdx: Int) = (2 * parentIdx) + 1
  def getRightChildIndex(parentIdx: Int) = (2 * parentIdx) + 2

  def getParent(childIdx: Int) = heap(getParentIndex(childIdx))

  def swap(idx1: Int, idx2: Int) = {
    val temp = heap(idx1)
    heap(idx1) = heap(idx2)
    heap(idx2) = temp
  }

}

class MaxHeap(heap : mutable.ArrayBuffer[Int]) extends Heap(heap) {

  override def insert(value: Int): Unit = {

      heap.append(value)
      var currIdx: Int = heap.size - 1
      while(currIdx!=0 && value > getParent(currIdx))
      {
        swap(currIdx, getParentIndex(currIdx))
        currIdx = getParentIndex(currIdx)
      }
  }

  override def removeTop(): Unit = {

    if (heap.isEmpty) {
      throw new EmptyHeapException()
    }else if (heap.size==1){
      heap.remove(0)
      return
    }

    swap(ROOT_INDEX, heap.size-1)
    heap.remove(heap.size-1)

    var currIdx = ROOT_INDEX

    while ( ( heap(currIdx) < _getLeftChild(currIdx) ) || ( heap(currIdx) < _getRightChild(currIdx) ) )
    {
      if (_getLeftChild(currIdx) > _getRightChild(currIdx)){
        swap(currIdx, getLeftChildIndex(currIdx))
        currIdx = getLeftChildIndex(currIdx)
      }else{
        swap(currIdx, getRightChildIndex(currIdx))
        currIdx = getRightChildIndex(currIdx)
      }
    }

    def _getLeftChild(parentIdx: Int) =
      if ( heap.size>getLeftChildIndex(parentIdx) )
        heap(getLeftChildIndex(parentIdx))
      else Integer.MIN_VALUE

    def _getRightChild(parentIdx: Int) =
      if ( heap.size>getRightChildIndex(parentIdx) )
        heap(getRightChildIndex(parentIdx))
      else Integer.MIN_VALUE

  }
}

object MaxHeap{

  def apply() = new MaxHeap(new mutable.ArrayBuffer[Int]())
}