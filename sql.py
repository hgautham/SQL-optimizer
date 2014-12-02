# -*- coding: utf-8 -*-
from pyparsing import Literal, CaselessLiteral, Word, Upcase, delimitedList, Optional, \
    Combine, Group, alphas, nums, alphanums, ParseException, Forward, oneOf, quotedString, \
    ZeroOrMore, restOfLine, Keyword 
def flatten(foo):
    for x in foo:
        if hasattr(x, '__iter__'):
            for y in flatten(x):
                yield y
        else:
            yield x
            
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
        wherevals = list()
        wherevals = tokens.where.asList()
        tablevals = tokens.tables.asList()
        tablevalsloop = tokens.tables.asList()
        node4 = []
        node5 = []
        print tablevals
        aliasloop = list()
        if 'AS' not in tablevals:
            node3 = tablevals[0]
            if len(tablevals)>1:
                node4 = tablevals[1]
        if len(tablevals)>1:
            while 'AS' in tablevalsloop:
                pos = tablevalsloop.index('AS')
                aliasloop.append(tablevalsloop[pos+1])
                tablevalsloop = tablevalsloop[pos+1:]
            print aliasloop
            if 'AS' in tablevals:
                node3 = aliasloop[0]
                if len(aliasloop)>1:
                    node4 = aliasloop[1]
                tablevals = aliasloop
                if len(aliasloop)>2:
                    tablevals = aliasloop[0] , aliasloop[1] , "(" + aliasloop[2] + ")"
                    node5 = aliasloop[2]
        tablevals = 'x'.join(tablevals)
        if len(wherevals)>1:
            wherevals = flatten(wherevals)
            wherevals = ' '.join(wherevals)
            wherevals = wherevals.replace("where","")
        projectvals = tokens.columns 
        projectvals = projectvals[0]
        print "PROJECT", projectvals , "(" , "SELECT" , wherevals , "(" , tablevals , ")" , ")"
        relalg = "PROJECT", projectvals , "(" , "SELECT" , wherevals , "(" , tablevals , ")" , ")"
        relalg = flatten(relalg)
        relalg = ' '.join( relalg)
        print relalg
        cross = conditionstmt.searchString( wherevals )
        cross = cross.asList()
        cross = [var for var in cross if var]
        print cross
        node1 = "PROJECT", projectvals
        node1 = flatten(node1)
        node1 = ' '.join(node1)
        node2 = "SELECT" , wherevals
        node2 = flatten(node2)
        node2 = ' '.join(node2)
        cross = 'x'
        if len(node5)==0:
            print "node1[ label = " , '"' , node1 , '"' , "]" "node2[ label =" , '"' , node2 , '"' , "]" "node3[label = " , '"' , node3 , '"' "]" , "cross[ label =" , '"' , "&#215;" , '"' , "]"
        if len(node5)>0:
           print "node1[ label = " , '"' , node1 , '"' , "]" "node2[ label =" , '"' , node2 , '"' , "]" "node3[label = " , '"' , node3 , '"' "]" , "cross2[ label =" , '"' , "&#215;" , '"' , "]" , "cross1[ label =" , '"' , "&#215;" , '"' , "]"
           print "node1->node2" , "node2->cross2"  , "cross2->node5" , "cross2->cross1" , "cross1->node3" , "cross1->node4"
        if len(node4)>0:
            print "node4[ label = " , '"' , node4 , '"' , "]"
        if len(node5)>0:
            print "node5[ label = " , '"' , node5 , '"' , "]"   
        if len(node5)==0:
            print "node1->node2" , "node2->cross"  , "cross->node3"
        if len(node4)>0 and len(node5)==0:
            print "cross->node4"

        
    except ParseException, err:
        print " "*err.loc + "^\n" + err.msg
        print err
    print


# define SQL tokens
selectStmt = Forward()
condition = Forward()
treegram = Forward()
comps = Forward()
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

condition << ( ZeroOrMore (columnName + binop + columnName) )

simpleSQL = selectStmt
conditionstmt = condition



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
