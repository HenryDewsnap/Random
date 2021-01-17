using System;

class program{
	public static void Main(){
		int CurrentVal = 2;
		while (true){
			bool Prime = true;
			for(int i=2;i<CurrentVal;i++){
				if (CurrentVal%i == 0){
					Prime = false;
				}
			}
			if (Prime == true){
				Console.WriteLine($"{CurrentVal} Is Prime");
			}
			CurrentVal += 1;
		}
	}
}
