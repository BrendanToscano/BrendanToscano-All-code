/*
 * Course: COMP 2113 FA01, 2023
 * Assignment 1, Question 3
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-08-20
 * I certify that this code is my own.
 * I have not broken any rules concerning Academic Dishonesty.
*/

/* What does this program do?
 * It takes the values/text file provided by the user in the command line, converts all values to integers and then adds them to an array list.
 * It then checks the Arraylist to see if it is empty, sorted or not sorted.
*/

import java.util.ArrayList;
import java.util.Scanner;

// Program to check if file is sorted or not.
public class sort_check{
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);
		ArrayList<Integer> nums = new ArrayList<Integer>();
		try{
			// Running to the user specified file, converting to integer and adding the values to arraylist.
			while(true){
				nums.add(Integer.parseInt(scanner.nextLine()));
			}
		}
		catch(Exception e){
		}
		// Goes to list and checks if sorted.
		int n = 0;
		while(true){
			if(nums.size() == 0){
				System.out.println("Empty");
				break;
			}
			else if(nums.size() == 1){
				System.out.println("Sorted");
				break;
			}
			else if(nums.get(n) <= nums.get(n+1)){
				if((n+2) >= nums.size()){
					System.out.println("Sorted");
					break;
				}
				n++;
			}
			else{
				System.out.println("Not Sorted");
				break;	
			}
		}
	}
}
