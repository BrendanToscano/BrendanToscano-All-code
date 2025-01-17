/*
 * Course: COMP 2103 FA01, 2023
 * Assignment 7, Question 1
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-11-27
 * I certify that this code is my own.
 * I have not broken any rules concenring Academic Dishonesty.
*/
/*
What does this program do?
The program reads the file and stores it in a student struct. It stores the id, name and marks of the student.
The marks consist of the midterm mark and the assignment scores of 8 assignments.
The program can also display the students. It can also find a student by the ID.
The program will calcualte the average of the total class marks.
The program will calculates the average of everyones assignment or midterm depending on the number specified by the user.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 8:02 - 8:09
// Creating the student Struct.
typedef struct{
    int id;
    char name[50];
    int marks[10];
} Student;


// 8:09 - 11:38
// To read all data from the file to the student struct.
int readCSV(const char* filename, Student* student, int* numStudents){
    FILE *file;
    char line[1000];
    char *token, *temp;
    int count = 0;
    
    // Opening the file with error handling.
    if((file = fopen(filename, "r")) == NULL){
        fprintf(stderr, "Error opening file.\n");
        exit(EXIT_FAILURE);
    }
    
    // Reading till the end of the csv file.
    while(fgets(line, 1000, file) != NULL){
        
        // Reading the first line using strtok till ,
        if((token = strtok(line, ",")) == NULL)
            continue;
        // Converting to int using strtol.
        student[count].id = strtol(token, &temp, 10);
        
        // Reading the second line using strtok till ,
        if((token = strtok(NULL, ",")) == NULL)
            break;
        // Copying token to student name.
        strcpy(student[count].name, token) ;
        
        // For all marks.
        for(int i = 0; i < 10; i++){
            if((token = strtok(NULL, ",")) == NULL)
                break;
            student[count].marks[i] = strtol(token, &temp, 10);
        }
        // Next line
        token = strtok(NULL, "\n");
        count++;
        
        // running till count is bigger than the num of the students in the file.
        if (count < *numStudents)
            break;
    }
    *numStudents = count;
        
    fclose(file);
    
    return count;
}

// 11:38 - 11:55
// To display the student information.
void displayStudent(Student* student){
    int mark;
    printf("Student ID: %d, Name: %s, Midterm: %d, ", (*student).id, (*student).name, (*student).marks[0]);
    // Printing assignment marks from 1 - 8
    for (int i = 1; i < 9; i++){
        mark = (*student).marks[i];
        // -1 means no grade.
        if (mark == -1)
            printf("Assignment %d: No Grade, ", i);
        else
            printf("Assignment %d: %d, ", i, mark);
    }
    printf("\n");
}

// 12:22 - 12:48
// To calcuate the total marks of the class.
float calculateClassMark(Student* students, int numStudents){
    float total = 0;
    
    // Assuming 20% is the midterm grade.
    for(int i = 1; i < numStudents; i++){
        float student = 0;
        
        if(students[i].marks[0] != -1){
            student += students[i].marks[0] * 0.2;
        }
        
        // Assuming 80% is assignment grade split between 8 assignments.
        for(int j = 1; j < 9; j++){
            if(students[i].marks[j] != -1){
                student += students[i].marks[j] * (0.8/8);
            }
        }
        total += student;
    }
    return total/(numStudents-1);
}

// 12:48 - 1:25
// Calculate the grade of a specific midterm or assignment.
float calculateAverageMark(Student* students, int numStudents, int classIndex){
    int mark = 0, numOfMarks = 0;
    float total = 0, avg = 0;
    // Get the assignment grade for all students and addign them up.
    for(int i = 1; i < numStudents; i++){
        mark = students[i].marks[classIndex];
        if (mark != -1){
            total += mark;
            numOfMarks++;
        }
    }
    if(numOfMarks == 0){
        return 0;
    }
    avg = (double)total/numOfMarks;
    return avg;
}
        

// 1:25 - 1:58
// Searching for student with their student id and returning the student data.
Student* searchStudent(Student* students, int numStudents, int targetID){
    for(int i = 1; i < numStudents; i++){
        if (students[i].id == targetID){
            return &students[i];
        }
    }
    printf("Student ID not found.\n");
    return NULL;
}


// 11:55 - 3:08
int main(){
    // Assuming there are no more than 500 students in the csv file. Change value if more.
    Student students[500];
    Student* student;
    int numStudents = 0;
    char option;
    int targetID, classIndex;
    float mark;
    
    numStudents = readCSV("StudentCSV1.csv", students, &numStudents);
    
    while(1){
        printf("a) Display all students.\n");
        printf("b) Calculate Class Mark.\n");
        printf("c) Calculate Average Mark.\n");
        printf("d) Search student with student ID.\n");
        printf("e) Quit.\n");
        printf("Select between a, b, c, d and e: ");
        
        scanf(" %c", &option);
        
        if(option == 'a'){
            printf("Student Info:\n");
            // Printing every students data.
            for(int i = 1; i < numStudents; i++){
                displayStudent(&students[i]);
            }
        }
        else if(option == 'b'){
            mark = calculateClassMark(students, numStudents);
            printf("Average class total is %lf\n", mark);
        }
        else if(option == 'c'){
            printf("Enter 0 for midterm average and 1-8 for each Assignment average: ");
            if(scanf("%d", &classIndex) != 1){
                exit(EXIT_FAILURE);
            }
            // Checkign if the classIndex is between 0 and 9
            if(classIndex < 0 || classIndex > 9){
                exit(EXIT_FAILURE);
            }
            mark = calculateAverageMark(students, numStudents, classIndex);
            printf("Average Mark of Midterm/Assignment %d is %lf\n", classIndex, mark);
        }
        else if(option == 'd'){
            printf("Enter the Student ID you want to search: ");
            if(scanf("%d", &targetID) != 1){
                exit(EXIT_FAILURE);
            }
            else{
                // Will check if student was found or not.
                student = searchStudent(students, numStudents, targetID);
                if (student != NULL){
                    displayStudent(student);
                }
            }
        }
        else if(option == 'e'){
            exit(EXIT_SUCCESS);
        }
        else{
            printf("Invalid Choice.\n");
            exit(EXIT_FAILURE);
        }
    
    }
}
