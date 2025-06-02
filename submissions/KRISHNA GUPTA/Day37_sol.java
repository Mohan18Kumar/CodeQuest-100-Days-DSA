import java.util.*;
public class Day37_sol {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int[]tree=new int[3];

        System.out.print("Input:");
        for (int i=0; i<3; i++)
        {
            tree[i]=sc.nextInt();
        }
        System.out.print("Output:");
        printTnorder(tree,0);
        sc.close();

    }

    static void printTnorder(int [] tree, int index)
    {
        if (index >= tree.length || tree[index] == 0) 
        {
            return; 
        }
        printTnorder(tree, 2*index+1);
        System.out.print(tree[index]+" ");
        printTnorder(tree, 2*index+2);

}
    
}
