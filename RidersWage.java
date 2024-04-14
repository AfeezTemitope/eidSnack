public class RidersWage{

public static int calculateRiderWage(int succesfulDeliveries){
	int basePay = 5000;
	int AmountPerParcel;

if ( succesfulDeliveries < 50){
AmountPerParcel = 160;
} else if  
(succesfulDeliveries >= 50 && succesfulDeliveries <= 59){
AmountPerParcel = 200;
} else if 
(succesfulDeliveries >= 60 && succesfulDeliveries <= 69){
AmountPerParcel = 250;
} else {
AmountPerParcel = 500;
}

return succesfulDeliveries * AmountPerParcel + basePay;
}
}