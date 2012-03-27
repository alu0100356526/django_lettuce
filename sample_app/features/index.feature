Feature: Rocking with lettuce and django
	
	Scenario: Simple Hello World
		Given I access the url "/home/"
		Then I see the header "Hello World"
