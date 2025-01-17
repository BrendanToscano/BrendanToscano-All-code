/*
 * Course: COMP 2113 FA01, 2023
 * Assignment 1, Question 1
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-08-20
 * I certify that this code is my own.
 * I have not broken any rules concerning Academic Dishonesty.
*/

/* What this program does?
 * It takes 3 values specified by the user from the command line and converts all of them to int. If there are less or more than 3 values it instructs the user on how to use the program.
 * The values are then used to generate random numbers a user specified number of times and a user specified range and prints them out.
*/

import java.util.Random;

// Program to generate random numbers.
public class generate_nums{
	public static void main(String[] args){
		// Checking if there are 3 user specified values in the command line.
		if(args.length == 3){
			// Converting the user specified values to integer.
			int num = Integer.parseInt(args[0]);
			int min_value = Integer.parseInt(args[1]);
			int max_value = Integer.parseInt(args[2]);
			Random rand = new Random();
			// Generating random numbers from user specified range, a user specified number of times.
			for(int i = 0; i < num; i++){
				System.out.println(rand.nextInt(max_value - min_value + 1) + min_value);
			}
		}
		// Telling user what to do if unexpected values returned.
		else{
			System.out.println("User Instructions: java generate_nums <num> <min_value> <max_value>");
		}
	}
}
