import java.util.Scanner;

public class IyaAfeezPizza{

private static final int SAPA_SIZE_SLICE = 4;
private static final int SMALL_MONEY_SLICE = 6;
private static final int BIG_BOYS_SLICE = 8;
private static final int ODOGWU_SLICE = 12;

private static final int sapaSize_PRICE_PER_BOX = 2000;
private static final int smallMoney_PRICE_PER_BOX = 2400;
private static final int bigBoys_PRICE_PER_BOX = 3000;
private static final int odogwu_PRICE_PER_BOX = 4200;


	public static int totalSlices  ;
        public static int pricePerBox  ;
	public static int numberOfPeople;

public static void main(String... a){
Scanner scanner = new Scanner(System.in);

System.out.print("ENTER NUMBER OF PEOPLE  ");
numberOfPeople = scanner.nextInt();
System.out.println("");



printPizzaType();
scanner.nextLine();

System.out.print("ENTER PIZZA TYPE ");
String pizzaType = scanner.nextLine().toUpperCase();



        switch (pizzaType) {
            case "SAPA_SIZE_SLICE":
                totalSlices = SAPA_SIZE_SLICE;
                pricePerBox = sapaSize_PRICE_PER_BOX;
                break;
            case "SMALL_MONEY_SLICE":
                totalSlices = SMALL_MONEY_SLICE;
                pricePerBox = smallMoney_PRICE_PER_BOX;
                break;
	    case "BIG_BOYS_SLICE" :
		totalSlices = BIG_BOYS_SLICE;
		pricePerBox = bigBoys_PRICE_PER_BOX;
		break;
	    case "ODOGWU_SLICE" :
		totalSlices = ODOGWU_SLICE;
		pricePerBox = odogwu_PRICE_PER_BOX;
		break;
            default:
                System.out.println("Invalid pizza type. Please choose from the available");
	}

	printSummary(numberOfPeople);



}
public static void printSummary(int numberOfPeople){

int numberOfBox = (numberOfPeople + totalSlices -1 ) / totalSlices;
int reminant = (numberOfBox * totalSlices) - numberOfPeople;
int totalPrice = numberOfBox * pricePerBox;

System.out.println("NUMBER OF BOX NEEDED IS " + numberOfBox + " boxes");
System.out.println("NUMBER OF LEFTOVER AFTER SLICING  " + reminant + " slices");
System.out.println("TOTAL PRICE = $ " + totalPrice);

}


	public static void printPizzaType(){
	String prompt = """
<<<<<<<<<< AVAILABLE PIZZA TYPE >>>>>>>>>>

* SAPA_SIZE_SLICE	* SMALL_MONEY_SLICE
* BIG_BOYS_SLICE	* ODOGWU_SLICE

""";
	System.out.print(prompt);

	}


}