import java.util.*;

public class RiderWageCaculations{
    public static void main(String...args){
        Scanner scanner = new Scanner(System.in);    
        List<Object> result = new ArrayList<>();
        
        String continueInput = "Y";
	

        while (continueInput.equalsIgnoreCase("Y")){

            System.out.println("Enter number of successful deliveries:");
            int successfulDeliveries = scanner.nextInt();
            scanner.nextLine();

            int ridersPayment = RidersWage.calculateRiderWage(successfulDeliveries);

	   
            String testResult = (successfulDeliveries >= 100) ? "Test Result (Successful)" : "Test Result (Failed)";
                
	    result.add("Delivery " + successfulDeliveries + " Test result (successful) : " + ridersPayment  );

            System.out.println("Do you want to enter more deliveries? (y/n)");
            continueInput = scanner.nextLine();
	    }

	    for (Object res : result) {
            System.out.println(res);
	   
        }
    }
}
