import cFunc
from cFunc import INCLUDE, HASH, INT, IDENT, LT, GT,PERIOD, MAIN, \
     LPAREN,RPAREN,LCURL,RCURL, IF, SWITCH, WHILE, DO, FOR, INT, EQ, RETURN, FLOAT, \
     TRUE, FALSE, STAR,PERCENT,NEQ, EQUAL, LT,LTE,SHIFTL,GT,GTE,SHIFTR, DBLBAR, DBLAMP, PLUS, MINUS,\
     SEMICOLON, FLOAT, DOUBLE, BOOL,SLASH,NUM,CHAR,AND,OR,ELSE,CASE,BREAK,DEFAULT,COLON
import symtab
def simpleC(src):
    global commset, loop, boolean, maxbool, maxloop, conditional, cases
    commset = 1
    conditional = 1
    maxbool = 0
    maxloop = 0
    cases = 1
    boolean = 1
    loop = 1
    cFunc.init(src)
    symtab.init()
    program()
def program(): #(import)* type main(){ (stmt)* returnStmt() }
    i = -1
    while i != cFunc.index:
        i = cFunc.index
        importStmt()
    if cFunc.s in {INT, FLOAT, BOOL, CHAR}: 
        cFunc.getSym()
        if cFunc.s == MAIN:
            cFunc.getSym()
            if cFunc.s == LPAREN:
                cFunc.getSym()
                if cFunc.s == RPAREN:
                    cFunc.getSym()
                    if cFunc.s == LCURL:
                        print('main:')
                        print()
                        cFunc.getSym()
                        i = -1
                        while i != cFunc.index:
                            i = cFunc.index
                            stmt()
                        returnStmt()
                        if cFunc.s == RCURL:
                            cFunc.getSym()
                            return
def importStmt():
    if cFunc.s == HASH:
        cFunc.getSym()
        if cFunc.s == INCLUDE:
            cFunc.getSym()
            code = 'fetch: '
            if cFunc.s == LT:
                cFunc.getSym()
                if cFunc.s == IDENT:
                    code = code + cFunc.val
                    cFunc.getSym()
                    if cFunc.s == PERIOD:
                        code = code + '.'
                        cFunc.getSym()
                        if cFunc.s == IDENT:
                            code = code + cFunc.val
                            cFunc.getSym()
                            if cFunc.s == GT:
                                cFunc.getSym()
                                print(code)
                                code = ''
                                return
def stmt():
    global value
    i = cFunc.index
    compstmt()
    if i == cFunc.index:
        returnStmt()
        if cFunc.s == SEMICOLON:
            cFunc.getSym()
    if i == cFunc.index:
        if cFunc.s == INT:#replace with entire type set
            cFunc.getSym()
            simpleloadstmt()
        elif cFunc.s == FLOAT:#replace with entire type set
            cFunc.getSym()
            simpleloadstmt()
        elif cFunc.s == DOUBLE:#replace with entire type set
            cFunc.getSym()
            simpleloadstmt()
    if i == cFunc.index:
        simplesetstmt()
def booleanStmt():
    global boolean, maxbool
    print('b' + str(boolean) + ':')
    boolTerm()
    if cFunc.s == OR:
        print('end b' + str(boolean))
        boolean = boolean + 1
        if boolean > maxbool:
            maxbool = boolean
        cFunc.getSym()
        booleanStmt()
    else:
        print('end b'+str(boolean))
    if boolean > maxbool:
        maxbool = boolean+1
def boolTerm():
    boolFact()
    if cFunc.s == AND:
        cFunc.getSym()
        boolTerm()
def boolFact():
    global boolean, maxbool
    comparison()
    if cFunc.s == MINUS:
        cFunc.getSym()
        boolFact()
    elif cFunc.s == LPAREN:
        goto = boolean
        boolean = boolean + 1
        if boolean > maxbool:
            maxbool = boolean
        cFunc.getSym()
        booleanStmt()
        if cFunc.s == RPAREN:
            print('end b'+str(boolean))
            cFunc.getSym()
            boolean = goto
            print('end b'+str(boolean))
def comparison():
    if cFunc.s == IDENT:
        v1 = cFunc.val
        cFunc.getSym()
        if cFunc.s == EQUAL:
            cFunc.getSym()
            if cFunc.s == IDENT:
                print('EQ: ' + str(v1) + ' '+ str(cFunc.val))
                cFunc.getSym()
            elif cFunc.s == NUM:
                print('EQ: ' + str(v1) + ' '+  str(cFunc.val))
                cFunc.getSym()
        elif cFunc.s == GT:
            cFunc.getSym()
            if cFunc.s == IDENT:
                print('GT: ' + str(v1) + ' '+ str(cFunc.val))
                cFunc.getSym()
            elif cFunc.s == NUM:
                print('GT: ' + str(v1) + ' '+  str(cFunc.val))
                cFunc.getSym()
        elif cFunc.s == LT:
            cFunc.getSym()
            if cFunc.s == IDENT:
                print('LT: ' + str(v1) + ' '+  str(cFunc.val))
                cFunc.getSym()
            elif cFunc.s == NUM:
                print('LT: ' + str(v1) + ' '+  str(cFunc.val))
                cFunc.getSym()
        elif cFunc.s == GTE:
            cFunc.getSym()
            if cFunc.s == IDENT:
                print('GTE: ' + str(v1) + ' '+  str(cFunc.val))
                cFunc.getSym()
            elif cFunc.s == NUM:
                print('GTE: ' + str(v1) + ' '+  str(cFunc.val))
                cFunc.getSym()
        elif cFunc.s == LTE:
            cFunc.getSym()
            if cFunc.s == IDENT:
                print('LTE: ' + str(v1) + ' '+  str(cFunc.val))
                cFunc.getSym()
            elif cFunc.s == NUM:
                print('LTE: ' + str(v1) + ' '+  str(cFunc.val))
                cFunc.getSym()
    if cFunc.s == NUM:
            v1 = cFunc.val
            cFunc.getSym()
            if cFunc.s == EQ:
                cFunc.getSym()
                if cFunc.s == EQ:
                    cFunc.getSym()
                    if cFunc.s == IDENT:
                        print('EQ: ' + str(v1) + ' '+ str(cFunc.val))
                        cFunc.getSym()
                    elif cFunc.s == NUM:
                        print('EQ: ' + str(v1) + ' '+  str(cFunc.val))
                        cFunc.getSym()
            elif cFunc.s == GT:
                cFunc.getSym()
                if cFunc.s == IDENT:
                    print('GT: ' + str(v1) + ' '+ str(cFunc.val))
                    cFunc.getSym()
                elif cFunc.s == NUM:
                    print('GT: ' + str(v1) + ' '+  str(cFunc.val))
                    cFunc.getSym()
            elif cFunc.s == LT:
                cFunc.getSym()
                if cFunc.s == IDENT:
                    print('LT: ' + str(v1) + ' '+  str(cFunc.val))
                    cFunc.getSym()
                elif cFunc.s == NUM:
                    print('LT: ' + str(v1) + ' '+  str(cFunc.val))
                    cFunc.getSym()
            elif cFunc.s == GTE:
                cFunc.getSym()
                if cFunc.s == IDENT:
                    print('GTE: ' + str(v1) + ' '+  str(cFunc.val))
                    cFunc.getSym()
                elif cFunc.s == NUM:
                    print('GTE: ' + str(v1) + ' '+  str(cFunc.val))
                    cFunc.getSym()
            elif cFunc.s == LTE:
                cFunc.getSym()
                if cFunc.s == IDENT:
                    print('LTE: ' + str(v1) + ' '+  str(cFunc.val))
                    cFunc.getSym()
                elif cFunc.s == NUM:
                    print('LTE: ' + str(v1) + ' '+  str(cFunc.val))
                    cFunc.getSym()
def compstmt():
    global loop, boolean, maxbool, maxloop, conditional
    if cFunc.s == IF:#FIX THIS
        condid = conditional
        conditional = conditional + 1
        cFunc.getSym()
        if cFunc.s == LPAREN:
            cFunc.getSym()
            print('cond' + str(condid) + 'a:')
            booleanStmt()
            boolean = maxbool + 1
            if cFunc.s == RPAREN:
                cFunc.getSym()
                if cFunc.s == LCURL:
                    cFunc.getSym()
                    i = -1
                    while i != cFunc.index:
                        i = cFunc.index
                        stmt()
                    if cFunc.s == RCURL:
                        cFunc.getSym()
                        print('end cond' + str(condid) + 'a')
                        if cFunc.s == ELSE:
                            print('fls: cond' + str(condid) + 'b')
                            print('cond'+str(condid)+'b:')              
                            cFunc.getSym()
                            if cFunc.s == LCURL:
                                cFunc.getSym()
                                i = -1
                                while i != cFunc.index:
                                    i = cFunc.index
                                    stmt()
                                if cFunc.s == RCURL:
                                    cFunc.getSym()
                                    print('end cond' + str(condid) + 'b')
    elif cFunc.s == SWITCH:#Finish This
        cFunc.getSym()
        if cFunc.s == LPAREN:
            cFunc.getSym()
            if cFunc.s == IDENT:
                print('set: s ' + cFunc.val)
                cFunc.getSym()
                if cFunc.s == RPAREN:
                    cFunc.getSym()
                    if cFunc.s == LCURL:
                        cFunc.getSym()
                        i = -1
                        while i != cFunc.index:
                            i = cFunc.index
                            case()
                        i = cFunc.index
                        default()
                        if i != cFunc.index:
                            if cFunc.s == RCURL:
                                cFunc.getSym()
                                return
    elif cFunc.s == WHILE:
        loopid = loop
        loop = loop + 1
        cFunc.getSym()
        print('iter' + str(loopid) + ':')
        if cFunc.s == LPAREN:
            cFunc.getSym()
            i = cFunc.index
            print('while:')
            booleanStmt()
            if i != cFunc.index:
                if cFunc.s == RPAREN:
                    cFunc.getSym()
                    if cFunc.s == LCURL:
                        cFunc.getSym()
                        i = -1
                        while i != cFunc.index:
                            i = cFunc.index
                            stmt()
                        if cFunc.s == RCURL:
                            cFunc.getSym()
                            print('jump: iter'+str(loopid))
                            return
    elif cFunc.s == DO:
        loopid = loop
        loop = loop + 1
        cFunc.getSym()
        print('run' + str(loopid) + ':')
        print()
        if cFunc.s == LCURL:
            cFunc.getSym()
            i = -1
            while i != cFunc.index:
                i = cFunc.index
                stmt()
            if cFunc.s == RCURL:
                cFunc.getSym()
                if cFunc.s == WHILE:
                    cFunc.getSym()
                    print('if:')
                    if cFunc.s == LPAREN:
                        cFunc.getSym()
                        i = cFunc.index
                        booleanStmt()
                        if i!= cFunc.index:
                            if cFunc.s == RPAREN:
                                cFunc.getSym()
                                if cFunc.s == SEMICOLON:
                                    cFunc.getSym()
                                    print('jump run' + str(loopid))
                                    return
    elif cFunc.s == FOR:
        loopid = loop
        code = 'iter ' + str(loopid) + ':'
        loop = loop + 1
        print(code)
        cFunc.getSym()
        if cFunc.s == LPAREN:
            cFunc.getSym()
            i = cFunc.index
            print('start:')
            stmt()
            if cFunc.s != i:
                print('while: ')
                booleanStmt()
                boolean = maxbool
                if cFunc.s == SEMICOLON:
                    cFunc.getSym()
                    reassign()
                    if cFunc.s == RPAREN:
                        cFunc.getSym()
                        print()
                        if cFunc.s == LCURL:
                            cFunc.getSym()
                            i = -1
                            while i != cFunc.index:
                                i = cFunc.index
                                stmt()
                            if cFunc.s == RCURL:
                                cFunc.getSym()
                                print('jump: iter'+str(loopid))
                                print()
                                return
def case():
    global cases
    if cFunc.s == CASE:
        c = cases
        cases = cases + 1
        cFunc.getSym()
        if cFunc.s == IDENT or cFunc.s == NUM:
            print('c' + str(c) + ': s ' + str(cFunc.val))
            cFunc.getSym()
            if cFunc.s == COLON:
                cFunc.getSym()
                i = cFunc.index
                stmt()
                while i != cFunc.index:
                    i = cFunc.index
                    stmt()
                brkstmt()
                print('end c'+str(c))
def brkstmt():
    if cFunc.s == BREAK:
        cFunc.getSym()
        if cFunc.s == SEMICOLON:
            cFunc.getSym()
def default():
    global cases
    if cFunc.s == DEFAULT:
        c = cases
        cases = cases + 1
        cFunc.getSym()
        if cFunc.s == COLON:
            print('c' + str(c) + ': s s') 
            cFunc.getSym()
            i = cFunc.index
            stmt()
            while i != cFunc.index:
                i = cFunc.index
                stmt()
            print('end c'+str(c))
def reassign():
    global commset
    if cFunc.s == IDENT:
        i = cFunc.val
        a = symtab.find(i)
        if a == -1:
            raise(Exception)
        cFunc.getSym()
        if cFunc.s == EQ:
            cFunc.getSym()
            print('set: ' + str(i) + ' e' +str(commset))
            print('e'+str(commset) +':')
            expr()
            print('end e' + str(commset))
            commset = commset + 1
def simplesetstmt():
    if cFunc.s == IDENT:
        var = cFunc.val
        cFunc.getSym()
        if cFunc.s == EQ:
            cFunc.getSym()
            print('set: ' + str(var) + ' ' + str(expr()))
            if cFunc.s == SEMICOLON:
                cFunc.getSym()
    else:
        expr()
def simpleloadstmt():
    if cFunc.s == IDENT:
        var = cFunc.val
        cFunc.getSym()
        if cFunc.s == EQ:
            cFunc.getSym()
            e = expr()
            symtab.newObj((var,e))
            print('load: ' + var + ' ' + str(e))
            if cFunc.s == SEMICOLON:
                cFunc.getSym()
    else:
        expr()
def expr():
    t = term()
    if cFunc.s == PLUS:
        cFunc.getSym()
        t2 = term()
        print("sum: " + str(t) + ' ' + str(t2))
    if cFunc.s == MINUS:
        cFunc.getSym()
        t2 = term()
        print("min: " + str(t) + ' ' + str(t2))
    return t
def term():
    t = factor()
    if cFunc.s == STAR:
        cFunc.getSym()
        t2 = factor()
        print("mul: " + str(t) + ' ' + str(t2))
    if cFunc.s == SLASH:
        cFunc.getSym()
        t2 = factor()
        print("div: " + str(t) + ' ' + str(t2))
    return t
def factor():
    if cFunc.s == NUM:
        val = cFunc.val
        print('get: ' + str(val))
        cFunc.getSym()
        return val
    if cFunc.s == IDENT:
        val = cFunc.val
        print('get: ' + str(val))
        cFunc.getSym()
        return val
    elif cFunc.s == LPAREN:
        cFunc.getSym()
        e = expr()
        if cFunc.s == RPAREN:
            cFunc.getSym()
            return e
def returnStmt():
    global commset
    code = ''
    if cFunc.s == RETURN:
        cFunc.getSym()
        code = code + 'ret: e' + str(commset)
        print(code)
        print('e'+str(commset)+':')
        expr()
        print('end e'+str(commset))
        commset = commset+1

print("TEST 1:")
simpleC('''#include <OhiMark.h>
int main(){
int a = 4;
int b = 6;
int c = 0;
double x = 0.1;
double y = 1.4;
while(a < b && b >= c || b < c){
a = a + 1;
}
do{
x = x / 2;
}while (x >= y);
b = 9;
return 0;
}''')
print()
print("TEST 2:")
print()
simpleC('''
#include <SomebodyOnceToldMe.h>
#include <CanIHaveOneHundredPlease.h>
int main(){
int c = 1;
int d = 1;
for(c = 7; c < 100; c = c + 1){
d = d + c;
}
int h = 0;
for(g = 20; g < 200; g = g + 8){
for(a = 1; a < 2; a = a + 1){
h = h + a * g;
}
}
return h;
}''')

print()
print("TEST 3:")
print()
simpleC('''
int main(){
int a = 4;
int b = 3;
int c = 10;
int y = 1;
double g = 3.2;
if(a < b){
x = x + 1;
}
else{
if(a == b){
x = x + 11;
}
else{
a = a + 2;
}
}
return g;
}''')
print()
print("TEST 4:")
print()
simpleC('''
int main(){
switch(b){
case 1:
a = b - 1;
case 2:
b = a * 8;
default:
a = 0;
b = 0;
}
return 0;
}''')
