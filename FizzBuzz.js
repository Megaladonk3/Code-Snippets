	
	for (let i=1; i<=100; i++) //For loop
	{
		
		if (i%15 == 0) //1st if statement for multiples of 15 and printing FizzBuzz
			console.log("FizzBuzz" + " ");
		
		else if ((i%3) == 0) //2nd if statement for multiples of 3 and printing Fizz
			console.log("Fizz" + " ");			
		
		else if ((i%5) == 0) //3rd if statement for multiples of 5 and printing Buzz				
			console.log("Buzz" + " ");			
	
		else
			console.log(i + " ");			
	}