/*
 * Course: COMP 2113 FA01, 2023
 * Assignment 1, Question 2
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-08-20
 * I certify that this code is my own.
 * I have not broken any rules concerning Academic Dishonesty.
*/

/* What this program does?
 * The program takes in a file provided by the user in the command line, converts it to integers and stores them in an arraylist. The arraylist is then passed through the insertion sort part of the code where it gets sorted and then printed.
 * How the insertion sort works?
 *  Starting an infinite while loop and then checking if the size of the arraylist is 0 or 1 and acting on it appropiately. If it passes through then it checks if the first number is greater than the second number. If it is then it moves the number back to the first numbers position and deletes the old number (thus swaping the numbers). In every other case it will check to see if we have reached the end of the list if not it will go to the next number and repeat the loop.
*/

import java.util.ArrayList;
import java.io.IOException;
import java.util.Scanner;

// Program to sort a list of numbers using insertion sort.
public class insertion_sort{
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
		// Insertion sort
		int n = 0;
			while(true){
				if(nums.size() == 0){
					System.out.println("");	
					break;
				}
				else if(nums.size() == 1){
					break;
				}
				else if((nums.get(n) > nums.get(n+1)) && n >= 0){
					nums.add(n , nums.get(n+1));
					nums.remove(n+2);
					if(n > 0){
						n--;
					}
				}
				else{
					if((n+2) >= nums.size()){
						break;
					}
					else{
						n++;
					}
				}
			}
		// Printing out the sorted list.
		for (int i : nums) {
			System.out.println(i);
		}
	}
}

