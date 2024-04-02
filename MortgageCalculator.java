import java.util.Scanner;
 public class MortgageCalculator {
   public static void main(String[] args) {
      Scanner input = new Scanner(System.in);

       int noOfMonthsInAYear = 12;
       int Percentage = 100;

      System.out.println("Enter the principal amount ");
         int principalAmount = input.nextInt();

      System.out.println("Enter the annual interest rate ");
          double userInput = input.nextDouble();

      System.out.println("Enter the duration in years "); 
           double numOfYears = input.nextDouble();

           double noOfYears = 12 * numOfYears;

          double rate = userInput/100;

          double monthlyRate = rate/12;

          double monthBase = 1 + monthlyRate;

          double base = Math.pow(monthBase,noOfYears);
       
         double numb1 = (principalAmount * monthlyRate) ;

         double numb2 = (base - 1);

         double monthlyPayment = numb1 * base  / numb2;

          System.out.printf("The monthly payment is %.2f", monthlyPayment);

}

}




    

   

