@Test 
public void testGetCustomer() {
	Customer aCustomer;
	String firstNameExpected;
	String firstNameActual;
	String lastNameExpected;
	String lastNameActual;

	aCustomer = table.getCustomer(2);
	assertNotNull(aCustomer);
	firstNameExpected = "John";
	firstNameActual = aCustomer.getGivenName();
	assertEquals(firstNameExpected, firstNameActual);
	lastNameExpected = "Doe";
	lastNameActual = aCustomer.getFamilyName();
	assertEquals(lastNameExpected, lastNameActual);

	jdbcModule.verifySQLStatementExecuted("SELECT * ");
}

@Test
public void testGetCustomer() {
	Customer aCustomer;
	String firstNameExpected;
	String firstNameActual;
	String lastNameExpected;
	String lastNameActual;

	aCustomer = table.getCustomer(2);
	assertNotNull(aCustomer);
	firstNameExpected = "John";
	firstNameActual = aCustomer.getGivenName();
	assertEquals(firstNameExpected, firstNameActual);
	lastNameExpected = "Doe";
	lastNameActual = aCustomer.getFamilyName();
	assertEquals(lastNameExpected, lastNameActual);
}

@Test
public void testGetCustomer() {
	Customer aCustomer;
	String firstNameExpected;
	String firstNameActual;
	String lastNameExpected;
	String lastNameActual;

	aCustomer = table.getCustomer(2);
	assertNotNull(aCustomer);
	firstNameExpected = "John";
	firstNameActual = aCustomer.getGivenName();
	assertEquals(firstNameExpected, firstNameActual);
	lastNameExpected = "Doe";
	lastNameActual = aCustomer.getFamilyName();
	assertEquals(lastNameExpected, lastNameActual);
}


