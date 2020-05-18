package misc_problems
import org.scalatest.{FlatSpec, Matchers}

class DAGPathsResolverTest extends FlatSpec with Matchers{

  "DAGPathResolver" should "return the set of all possible paths for a given sample DAG" in {

    val fileName = "src/test/resources/misc_problems/DAGPathResolverTest/sample_DAG.txt"

    val setOfPaths = DAGPathsResolver.run(fileName)
    setOfPaths.size should be (5)
    setOfPaths should contain("0 -> 1 -> 3")
    setOfPaths should contain("0 -> 1 -> 5")
    setOfPaths should contain("0 -> 2 -> 5")
    setOfPaths should contain("6 -> 2 -> 5")
    setOfPaths should contain("4")
  }
}