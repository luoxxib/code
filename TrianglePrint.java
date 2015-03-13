/**
 * @(#)ch3.java
 * @author 
 * @version 1.00 2014/11/6
 * 打印三角形
 */

public class ch3 {
        
    /**
     * Creates a new instance of <code>ch3</code>.
     */
    public ch3() {
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int num = 7;
        int nrow = 0;
        int pos = 0;
        for(int i = 0; i < num; i++){
        	if(i < num/2.0){
        		nrow = num - i * 2;
        		pos = i;
        	}	
        	else{
        		nrow = nrow + 2;
        		pos = pos - 1;
        	}
        	for(int k = 0; k < pos; k++)
        		System.out.print(" ");
        	for(int j = 0; j < nrow; j++){
        		
        		System.out.print("*");
        	}
        	System.out.print("\n");
        }
    }
}