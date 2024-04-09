import java.util.Scanner;
 public class Loop4  {
   public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

int count = 0;
int passmark = 45;
int passes = 0;
int failed = 0;

     while (count <= 15) {
  System.out.println("Enter Score of Student: ");
     int score = input.nextInt();

  if (score >= passmark)  {
     passes = passes + 1;
  }
  else {
     failed = failed + 1;
 }
   count = count + 1;
   }
  System.out.printf("Total Student Passes: %d%n Total Student that Failed: %d%n", passes,failed);

}

}



