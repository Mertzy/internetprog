/* This class does the following:
1. private instance variables for ssn and weight
2. public instance variables for age and name
3. public methods called gainWeight(lbs), getSSN(), and getWeight()
4. a prototype method called birthday() that adds one to the age and returns the age after incrementing.

*/


Person = function(namer, ageness, inputSSN, weighter) {

    var ssn = inputSSN;
    var weight = weighter;
    this.age = ageness;
    this.name = namer;
    
    this.gainWeight = function(lbs) {
	
	weight = weight + lbs;

    }

    this.getSSN = function() {
	
	return ssn;

    }

    this.getWeight = function() {

	return weight;
    }

}

Person.prototype.birthday = function() {

    this.age = this.age + 1;
    return this.age;

}

