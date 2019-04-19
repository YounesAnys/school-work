/* ---------------- Definitions space ----------------- */



%Start AFTER

/* ------------------- Rules space -------------------- */
%%

^[a-zA-Z](\.[^@\.]+|[^@\.]*)*@[^@\.]+(\.[^@\.]+)+$	{printf("%s\n", yytext);}


.|\n					{} // default rule (always include to match all other strings)

%%

/* ----------------- User code space ------------------ */

main()
{
	yylex();
	return;
}