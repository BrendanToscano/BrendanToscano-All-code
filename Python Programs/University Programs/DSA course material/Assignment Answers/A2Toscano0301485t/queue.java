/*
 * Course: COMP 2113 FA01, 2023
 * Assignment 2, Question 1
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-10-02
 * I certify that this code is my own.
 * I have not broken any rules concerning Academic Dishonesty.
 */
/*
Basic working of the code: -
- Starting the program and creating a array that is of length 5.
- Starting an infinite loop
- Checking to see if the list is full. If it is then the size will double
- Asking user if they want to push, pop, add, remove, display, end
- if push then it will push the user stated value next to the last value in the queue.
- if pop then it will pop the last item from the queue
- if add then will ask user the position they want to insert in (checks for conditions like in diagram). if
conditions are satisfied then it will ask the user for the item they want to insert.
- if remove then will ask user the position they want to remove from (checks for conditions like in diagram). if
conditions are satisfied then it will remove the item.
- if display then will display the queue to the user.
- if end then will end the program and close scanner.
- if the user enters an unexpected value will instruct user on what to enter.
- for all cases other than end the program will repeat till the user enters end
 */

/*
All possible edge cases have been accounted for:
- First edge case: When the user is prompted to enter(push,pop...). Here the program will prompt the user with instructions
and will restart the loop
- Second edge case: for pop and remove. In both cases it will check if there are items in the queue before executing. If
there are no elements in the queue it will tell the user that the queue is empty.
- Third edge case: In add and remove the user is prompted to enter an integer. Here if the user enters anything other than an
integer then the program will catch the exception and tell the user to enter an integer.
- Fourth edge case: The conditions in add and remove have been accounted for. All conditions are listed in the diagram.
 */

/*
Cases tested for:
Using pop and remove when queue is empty
Adding and removing from position 0 using add and remove
Adding and removing at the end of the queue
Adding and removing from the middle of the queue
Testing for more than 5 items and checking if the queue has doubled in size
Checking using negative numbers for add, remove
Checking out of queue range for add, remove
Checking for non-integer values in add, remove
*/

// In documentation when I say end of queue , I place where the last item is.
import java.util.Scanner;

public class queue {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String[] items_array = new String[5];
        // This variable is to keep track of the actual end of the queue with valid data.
        int n_end = 0;
        while(true) {
            // If the queue is full it will double its size.
            if(n_end == items_array.length){
                int i = 0;
                // New array double the size of the old array.
                String[] updated_array =new String[items_array.length * 2];
                // Adding all items from the old array to the new array
                for(String item : items_array){
                    updated_array[i] = item;
                    i++;
                }
                // Assigning old array to the new array with updated size
                items_array = updated_array;
                // Statement for marker will be printed
                System.out.println("Size of queue has doubled. Current size is " + items_array.length);
            }
            // Asking user if they want to push, pop, add, remove, display or end.
            System.out.println("Do you want to push(pu), pop(p), add(a), remove(r), display(d)? To end type \"end\".");
            String user_input = scan.nextLine();
            // Checking if user requested to push
            if(user_input.equals("push") || user_input.equals("pu")){
                // Asking user the item they want to store and adding it to the end of the queue.
                System.out.println("Enter the item you want to push");
                String pushed_item = scan.nextLine();
                items_array[n_end] = pushed_item;
                n_end++;
            }
            // Checking if user requested to pop
            else if(user_input.equals("pop") || user_input.equals(("p"))){
                // If queue is empty
                if(n_end == 0){
                    System.out.println("The queue is empty");
                }
                // Item from the end of the list is removed.
                else {
                    System.out.println("Item popped: " + items_array[n_end - 1]);
                    items_array[n_end - 1] = null;
                    n_end--;
                }
            }
            // Checking if user requested to add
            else if(user_input.equals("add") || user_input.equals("a")){
                // Asking user for a position they want to add to. Catching exception thrown if other than integer.
                System.out.println("Enter the position you want to add the item to (no negative numbers)(from 0)");
                int add_position;
                try {
                    add_position = Integer.parseInt(scan.nextLine());
                    }
                catch (Exception e){
                    System.out.println("Please enter a non-negative integer");
                    continue;
                }
                if(add_position == 0){
                    // If true will avoid running the else if statement below which gives error when 0.
                }
                // Checking if the number is range of queue, if negative number, if position before given position is empty.
                else if((add_position > n_end) || (add_position < 0) || ((items_array[add_position - 1]) == null)){
                    System.out.println("Try again with a different position");
                    continue;
                }
                System.out.println("Enter the item you want to push");
                String added_item = scan.nextLine();
				// Same as push
                if(add_position == 0 && n_end == 0){
                    items_array[n_end] = added_item;
                    n_end++;
                }
                else{
                    for(int i = (items_array.length - 1); i > add_position; i--){
                        items_array[i] = items_array[i - 1];
                    }
                    items_array[add_position] = added_item;
                    n_end++;
                }
            }
            // Checking if user requested to remove
            else if(user_input.equals("remove") || user_input.equals("r")){
                // If queue is empty
                if(n_end == 0){
                    System.out.println("The queue is empty");
                    continue;
                }
                // Asking user for a position they want to remove from. Catching exception thrown if other than integer.
                System.out.println("Enter the position you want to remove the item from (no negative numbers)(from 0)");
                int remove_position;
                try{
                    remove_position = Integer.parseInt(scan.nextLine());
                }
                catch (Exception e){
                    System.out.println("Please enter a non-negative integer");
                    continue;
                }
                // If user enters 0(same as pop)
                if(remove_position == 0){
                    System.out.println("Item removed: " + items_array[0]);
                    int n = 0;
                    for(int i = 0; i < (items_array.length - 1); i++) {
                        items_array[n] = items_array[n + 1];
                        n++;
                    }
                    n_end--;
                }
                // If user enter a value is greater than the position of the last value, less than 0, the position is empty or the position before the user stated position is empty.
                else if((remove_position > n_end) || (remove_position < 0) || ((items_array[remove_position - 1]) == null) || ((items_array[remove_position]) == null)){
                    System.out.println("Try again with a different position");
                }
                else{
                    System.out.println("Item removed: " + items_array[remove_position]);
                    for(int i = remove_position; i < (items_array.length - 1); i++){
                        items_array[i] = items_array[i + 1];
                    }
                    n_end--;
                }
            }
            // Checking if user requested to display
            else if(user_input.equals("display") || user_input.equals("d")){
                System.out.println("Items in Queue: ");
                for(int i = 0; i < n_end; i++){
                    System.out.println(items_array[i]);
                }
            }
            // Checking if user requested to end the program
            else if(user_input.equals("end")){
                break;
            }
            // Invalid user response
            else{
                System.out.println("Please ONLY enter \"push\" or \"pu\",  \"pop\" or \"p\", \"add\" or \"a\", \"remove\" or \"r\", \"display\" or \"d\", \"end\" ");
            }
        }
        // Closing scanner
        scan.close();
    }
}
