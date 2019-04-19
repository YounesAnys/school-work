import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

/**
 * Assignment 3 Solution. Implementation of a recursive descent parser for an LL(1) grammar
 * @author Hussein Al Osman
 */

public class RecursiveDescentParsing {

	private String token = " ";  //stores the value of the current token
	private BufferedReader br;

	/**
	 * Constructor
	 * @param filepath
	 */
	public RecursiveDescentParsing(File inputFile){

		try {

			br = new BufferedReader(new FileReader(inputFile));

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	/**
	 * Read one token for the input file
	 * @return the latest read token
	 */
	public String getNextToken(){
		String line = "";

		try {

			line = br.readLine();

		}
		catch (IOException e) {
			e.printStackTrace();
		}

		return line!=null?line: "";
	}


	/**
	 * This method starts the parsing operations
	 * @return true if there are not syntax errors and false otherwise
	 */
	public boolean parse(){

		token = getNextToken();

		// Process the program non-terminal and THEN check if the last token is the dollar sign (end of stream symbol)
		if (!program() || !token.equals("$")){
			return false;
		}
		else {
			return true;
		}
	}

	/**
	 * Handle the following grammar rule:
	 * <program> ::= begin <statement_list> end
	 * @return true if the corresponding grammar rule is respected and false otherwise
	 */
	public boolean program(){

		// the program terminal must start with a begin terminal
		if(token.equals("begin")) {
			// we have a match, get next token
			token = getNextToken();

			// process the statment_list non-terminal
			if(!statementList()){
				// somewhere while processing the statment_list non-terminal, we had a syntax error
				return false;
			}
			else{
				if (token.equals("end")){
					// we have a match, get next token
					token = getNextToken();
					return true;
				}
				else {
					// the end terminal is missing
					return false;
				}
			}
		}
		else {
			// the begin terminal is missing
			return false;
		}
	}


	/**
	 * Handle the following grammar rule:
	 * <statement_list> ::= <statement> ; <statement_list�>
	 * @return true if the corresponding grammar rule is respected and false otherwise
	 */
	public boolean statementList(){

		// process the statement non-terminal
		if(!statement()){

			// somewhere while processing the statement non-terminal, we had a syntax error
			return false;
		}
		else if(token.equals(";")){
			// we have a match, get next token
			token = getNextToken();

			// process the statment_list' non-terminal
			return statementListPrime();
		}
		else{
			// we are missing the ; terminal
			return false;
		}
	}


	/**
	 * Handle the following grammar rules:
	 * <statement_list�> ::= <statement_list>
	 * <statement_list�> ::= epsilon
	 * @return true if the corresponding grammar rules are respected and false otherwise
	 */
	public boolean statementListPrime(){

		// process the statment_list non-terminal
		statementList();

		// always return true since we have an epsilon rule
		return true;

	}

	/**
	 * Handle the following grammar rule:
	 * <statement> ::= id = <expression>
	 * @return true if the corresponding grammar rule is respected and false otherwise
	 */
	public boolean statement(){

		// the statement rule must start with an id terminal
		if(token.equals("id")){

			// we have a match, get next token
			token = getNextToken();

				if(token.equals("=")){

					// we have a match, get next token
					token = getNextToken();

					// process the expression non-terminal
					return expression();
				}
				else {
					// we are missing the = terminal
					return false;
				}
		}
		else {

			// we are missing the id terminal
			return false;
		}
	}


	/**
	 * Handle the following grammar rule:
	 * <expression> ::= <factor> <expression�>
	 * @return true if the corresponding grammar rule is respected and false otherwise
	 */
	public boolean expression(){

		// process the factor non-terminal
		if(!factor()){

			// somewhere while processing the factor non-terminal, we had a syntax error
			return false;
		}
		else{
			// process the expression' non-terminal
			return expressionPrime();
		}
	}


	/**
	 * Handle the following grammar rules:
	 * <expression�> ::= + <factor>
	 * <expression�> ::= - <factor>
	 * <expression�> ::= epsilon
	 * @return true if the corresponding grammar rules are respected and false otherwise
	 */
	public boolean expressionPrime(){

		// the expression' rule must start with the + or - terminal (otherwise, it would be the epsilon rule)
		if(token.equals("+")){
			// we have a match, get next token
			token = getNextToken();

			// process the factor non-terminal
			return factor();
		}
		else if(token.equals("-")){

			// we have a match, get next token
			token = getNextToken();

			// process the factor non-terminal
			return factor();
		}
		else{

			// return true since we have an epsilon rule
			return true;
		}
	}


	/**
	 * Handle the following grammar rules:
	 * <factor> ::= id
	 * <factor> ::= num
	 * @return true if the corresponding grammar rules are respected and false otherwise
	 */
	public boolean factor(){

		// the factor rule must start with the id or num
		if (token.equals("id")) {
			// we have a match, get next token
			token = getNextToken();
			return true;
		}
		else if (token.equals("num")) {
			// we have a match, get next token
			token = getNextToken();
			return true;
		}
		else{
			// we are missing the id or num terminals
			return false;
		}
	}


	/**
	 * Main method that create an instance of the RecursiveDescentParsing class and starts the parsing operations
	 * @param args
	 */
	public static void main(String [] args){

		if (args.length > 0){
			String filepath = args[0];

			File file = new File(filepath);

			// Check is the specified path belongs to a file
			if (file.isFile()){
				RecursiveDescentParsing parser = new RecursiveDescentParsing(file);

				// Parse the input file
				boolean success = parser.parse();

				// Display results
				if (success){
					System.out.println("SUCCESS: the code has been successfully parsed");
				}
				else {
					System.out.println("ERROR: the code contains a syntax mistake");
				}
			}
			else {
				// In case the specified argument does not correspond to a valid file path
				System.err.println("Specified file path is invalid");
			}
		}
		else {
			// No input file has been specified
			System.err.println("USAGE: Specify the path of the input file as an argument");
		}

	}
}
