/*
 * Course: COMP 2113 FA01, 2023
 * Assignment 4, Question 1
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-10-16
 * I certify that this code is my own.
 * I have not broken any rules concenring Academic Dishonesty.
*/
/*
What does this program do?
The program has 5 methods : -insertValue, size(node), depth(node), depthTraverse, breathTraverse
Insert value will insert a value depending on whether it is larger or smaller than the parent value.
Suppose the value is greater than the parent value it will be put to the right and if the value is
smaller than the parent value it will be put towards the left.

sized is a recursive function that will keep incrementing the value and return it once it reaches the
end of the tree. size will print it out and call sized.

depth will find out how many nodes away it is from the root.

depthTraverse in this case is in order so it will start printing the values of the nodes from the left
till it reaches the right of the tree. It should return the values in order if insert value was used.

breathtraverse will start printing the values from the top then print each section of the tree from left
to right.

Not required by question method:-
getNode inserts all values into an array list in the same form as breathTraverse and using the values in
the arraylist will return a node at a user specified position.
 */
import java.util.ArrayList;
public class BinarySearchTree {
    Node root;
    public void insertValue(int value){
        // Initializing new node and setting values
        Node node = new Node();
        node.data = value;
        node.left = null;
        node.right = null;
        node.parent = null;

        // Checking if a root exists and setting its value if not
        if(root == null){
            root = node;
            System.out.println("The root has been set with value " + value);
        }
        else{
            Node current = root;
            while(true){
                // When node data is less than the parent node.
                if(node.data < current.data){
                    if(current.left == null){
                        current.left = node;
                        current.left.parent = current;
                        System.out.println("Value \"" + value + "\" inserted to the left");
                        break;
                    }
                    else{
                        current = current.left;
                    }
                }
                // For when the node data is greater or equal to the parent node.
                else{
                    if(current.right == null){
                        current.right = node;
                        current.right.parent = current;
                        System.out.println("Value \"" + value + "\" inserted to the right");
                        break;
                    }
                    else{
                        current = current.right;
                    }
                }
            }
        }
    }
    // Creating a recursive function to determine the size of the tree from any node.
    public void size(Node node){
        // printing out the size of the node returned from the recursive function
        System.out.println("The size is " + sized(node));
    }
    private int sized(Node node){
        // Checking if user given node is null
        if(node == null){
            return 0;
        }
        else{
            return sized(node.left) + 1 + sized(node.right);
        }
    }
    public void depth(Node node){
        int depth = 0;
        // Following the path back till the root
        while(node != null && node != root){
            depth++;
            node = node.parent;
        }
        System.out.println("The depth from your specified node is " + depth);
    }
    public void depthTraverse(){
        Node traverse = root;
        // Creating an array list to store visited nodes
        ArrayList<Node> pastValues = new ArrayList<Node>();
        // Checking if the bst is empty
        if(root == null){
            System.out.println("THe BST is empty");
            return;
        }
        System.out.println("Depth first traverse of the BST (in order):-");
        while(true){
            // Going left if the node is not in the arraylist
            while(traverse.left != null && !pastValues.contains(traverse.left)){
                // Setting the node to current node
                traverse = traverse.left;
            }
            // If the current node is not in already visted array list
            if(!pastValues.contains(traverse)){
                System.out.println(traverse.data);
                pastValues.add(traverse);
            }
            // Going right if the node is not in the arraylist
            if(traverse.right != null && !pastValues.contains(traverse.right)){
                // Setting the node to current node
                traverse = traverse.right;
            }
            // Going back to parent if both left and right are done
            else if (traverse.parent != null){
                traverse = traverse.parent;
            }
            else{
                break;
            }
        }
    }
    public void breadthTraverse(){
        Node traverse = root;
        // Creating an array list to store visited nodes
        ArrayList<Node> usedNode = new ArrayList<Node>();
        // Checking if user given node is null
        if(root == null){
            System.out.println("THe BST is empty");
            return;
        }
        System.out.println("Breath first traverse of the BST:-");
        usedNode.add(root);
        while(true){
            // Will repeat till there is nothing in arraylist.
            if(usedNode.isEmpty()){
                break;
            }
            // Getting the current value printing it then removing it.
            traverse = usedNode.get(0);
            System.out.println(traverse.data);
            usedNode.remove(0);
            // Going left and adding that value to the arraylist
            if(traverse.left != null){
                usedNode.add(traverse.left);
            }
            // Going right and adding the value to the arraylist
            if(traverse.right != null){
                usedNode.add(traverse.right);
            }
        }
    }
    /*
    The question doesn't require this but I don't understand how
    for depth(node) we are suppose to get the exact node we want to traverse till.
    Basically when the user enter a position it will return the node at that position using a
    similar logic to breath first traverse.
    */
    public Node getNode(int position){
        Node traverse = root;
        ArrayList<Node> usedNode = new ArrayList<Node>();
        ArrayList<Node> nodes = new ArrayList<Node>();
        if(root == null){
            return root;
        }
        usedNode.add(root);
        while(true){
            if(usedNode.isEmpty()){
                break;
            }
            traverse = usedNode.get(0);
            nodes.add(traverse);
            usedNode.remove(0);
            if(traverse.left != null){
                usedNode.add(traverse.left);
            }
            if(traverse.right != null){
                usedNode.add(traverse.right);
            }
        }
        if(position >= nodes.size() || position < 0){
            System.out.println("Out of range value will return root");
            return root;
        }
        else{
            return nodes.get(position);
        }
    }

}
