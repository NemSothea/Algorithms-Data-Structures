import Foundation

/*
 * Complete the 'staircase' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

func staircase(n: Int) -> Void {
    // Write your code here
    
    for i in 1...n {
        let space = String(repeating: " ", count: n - 1)
        let hase = String(repeating: "#", count: i)
        print(space + hase)
    }
   
    
}
print(staircase(n: 6))
