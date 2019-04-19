/* ---------------- Definitions space ----------------- */



/* ------------------- Rules space -------------------- */
%%
^aa(a|b)*$				{printf("Token1: %s\n", yytext);}
^(a|b)*aaa(a|b)*$			{printf("Token2: %s\n", yytext);}
^(a|b)*aa(a|b)*$			{printf("Token3: %s\n", yytext);}
^((a|b)(a|b))*$			{printf("Token4: %s\n", yytext);}
^b*(b*ab*ab*)*$			{printf("Token5: %s\n", yytext);}
^((a|b)(a|b)(a|b)(a|b)(a|b))*$	{printf("Token6: %s\n", yytext);}
^(b*|ab+|ab*ab)*(ab*|aab*|[:blank:])$	{printf("Token7: %s\n", yytext);}


.|\n					{} // default rule (always include to match all other strings)

%%

/* ----------------- User code space ------------------ */

main()
{
	yylex();
	return;
}