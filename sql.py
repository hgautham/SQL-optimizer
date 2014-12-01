# -*- coding: utf-8 -*-
from pyparsing import Literal, CaselessLiteral, Word, Upcase, delimitedList, Optional, \
    Combine, Group, alphas, nums, alphanums, ParseException, Forward, oneOf, quotedString, \
    ZeroOrMore, restOfLine, Keyword

def test( str ):
    print str,"->"
    try:
        tokens = simpleSQL.parseString( str )
        print "tokens = ",        tokens
        print "tokens.columns =", tokens.columns
        print "tokens.tables =",  tokens.tables
        print "tokens.where =", tokens.where
        print "tokens.nestedcolumns =", tokens.nestedcolumns
        print "tokens.nestedtables =",  tokens.nestedtables
        print "tokens.nestedwhere =", tokens.nestedwhere
        print u'π', tokens.columns, "Select" , tokens.where , "(" , tokens.tables , ")"
    except ParseException, err:
        print " "*err.loc + "^\n" + err.msg
        print err
    print


# define SQL tokens
selectStmt = Forward()
selectToken = Keyword("select", caseless=True)
fromToken   = Keyword("from", caseless=True)
astoken  = Keyword("AS", caseless=True)

ident          = Word( alphas, alphanums + "_$" ).setName("identifier")
columnName     = Upcase( delimitedList( ident, ".", combine=True ) )
columnNameList = Group( delimitedList( columnName ) )
tableName      = Upcase( delimitedList( ident, ".", combine=True ) )
tableName2      = Upcase( delimitedList( ident, ".", combine=True ) )
tableAlias  = tableName + astoken + tableName2
tableNameList  = Group( delimitedList( tableAlias | tableName ) )

whereExpression = Forward()
and_ = Keyword("and", caseless=True)
or_ = Keyword("or", caseless=True)
in_ = Keyword("in", caseless=True)

E = CaselessLiteral("E")
binop = oneOf("= != < > >= <= eq ne lt le gt ge", caseless=True)
arithSign = Word("+-",exact=1)
realNum = Combine( Optional(arithSign) + ( Word( nums ) + "." + Optional( Word(nums) )  |
                                                         ( "." + Word(nums) ) ) + 
            Optional( E + Optional(arithSign) + Word(nums) ) )
intNum = Combine( Optional(arithSign) + Word( nums ) + 
            Optional( E + Optional("+") + Word(nums) ) )

columnRval = realNum | intNum | quotedString | columnName # need to add support for alg expressions
whereCondition = ZeroOrMore(
    ( columnName + binop + columnRval ) |
    ( columnName + in_ + "(" + delimitedList( columnRval ) + ")" ) |
    ( columnName + in_ + "(" + ZeroOrMore(selectToken + 
                   ( '*' | columnNameList ).setResultsName( "nestedcolumns" ) + 
                   fromToken + 
                   tableNameList.setResultsName( "nestedtables" ) + 
                   Optional( ZeroOrMore( CaselessLiteral("where") + whereExpression ), "" ).setResultsName("nestedwhere")) + ")" ) |
    ( "(" + whereExpression + ")" )
    )
whereExpression << whereCondition + ZeroOrMore( ( and_ | or_ ) + whereExpression ) 

# define the grammar
selectStmt      << ( selectToken + 
                   ( '*' | columnNameList ).setResultsName( "columns" ) + 
                   fromToken + 
                   tableNameList.setResultsName( "tables" ) + 
                   Optional( ZeroOrMore( CaselessLiteral("where") + whereExpression ), "" ).setResultsName("where") )

simpleSQL = selectStmt

# define Oracle comment format, and ignore them
oracleSqlComment = "--" + restOfLine
simpleSQL.ignore( oracleSqlComment )


test( "SELECT * from XYZZY, ABC" )
test( "select * from SYS.XYZZY" )
test( "Select A from Sys.dual" )
test( "Select A,B,C from Sys.dual" )
test( "Select A, B, C from Sys.dual" )
test( "Select A, B, C from Sys.dual, Table2   " )
test( "Xelect A, B, C from Sys.dual" )
test( "Select A, B, C frox Sys.dual" )
test( "Select" )
test( "Select &&& frox Sys.dual" )
test( "Select A from Sys.dual where a in ('RED','GREEN','BLUE')" )
test( "Select A from Sys.dual where a in ('RED','GREEN','BLUE') and b in (10,20,30)" )
test( "Select A,b from table1,table2 where table1.id = table2.id -- test out comparison operators" )
test("Select S.sname from Sailors AS S,Reserves AS R where S.sid=R.sid and R.bid=103")
test("SELECT S.sname FROM Sailors AS S, Reserves AS R, Boats AS B WHERE S.sid=R.sid AND R.bid=B.bid AND B.color='red'")
test("Select S.sname from Sailors AS S, Reserves AS R Where R.sid = S.sid and R.bid = 100 and S.rating > 5 and R.day = '8/9/09'")
test("SELECT S.sname FROM Sailors AS S WHERE S.sid IN ( SELECT R.sid FROM Reserve AS R WHERE R.bid = 103)")
