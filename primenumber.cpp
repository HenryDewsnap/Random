#include <iostream>

int main(){
	int currentval = 2;
	while (true){
		bool prime = true;
		for (int i=2;i<currentval;i++){
			if (currentval % i == 0){
				prime = false;
			}
		}
		if (prime == true){
			std::cout << currentval << " is prime" << std::endl;
		}
		currentval += 1;
	}		
}
