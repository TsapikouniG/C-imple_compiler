import sys
import copy


letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#file = open('', 'r')
file= open(sys.argv[1], 'r')


tokens_id=100
tokens_digit = 101
tokens_name=102
tokens_plus=103
tokens_minus=104
tokens_mult=105
tokens_mult=105
tokens_div=106
tokens_equal=107
tokens_greaterThan=108
tokens_greaterThanOrEq=109
tokens_lessThan=110
tokens_lessThanOrEq=111
tokens_diff=112
tokens_asgn=113
tokens_coma=114
tokens_fullStop=115
tokens_Qmark=116
tokens_leftParenthesis=117
tokens_rightParenthesis=118
tokens_leftBlock=119
tokens_rightBlock=120
tokens_leftBracket=121
tokens_rightBracket=122
tokens_program=123
tokens_if=124
tokens_switchcase=125
tokens_not=126
tokens_function=127
tokens_input=128
tokens_declare=129
tokens_else=130
tokens_forcase=131
tokens_and=132
tokens_procedure=133
tokens_print=134
tokens_while=135
tokens_incase=136
tokens_or=137
tokens_call=138
tokens_case=139
tokens_return=140
tokens_default=141
tokens_in=142
tokens_inout=143
tokens_EOF=144

state_start=0
state_dig= 1
state_letter=2
state_asgn=3
state_smaller=4
state_larger=5
state_rem=6

space=0
digit=1
letter=2
plusSign=3
minusSign=4
leftBlock=5
rightBlock=6
leftParenthesis=7
rightParenthesis=8
leftBracket=9
rightBracket=10
coma=11
questionMark=12
fullStop=13
colon=14
equal_sign=15
lessThan=16
greaterThan=17
comment=18
newLine=19
EOF=20
unexpected_character=21
multSign=22
divSign=23

UNEXPECTED_INPUT_ERROR= -1
UNEXPECTED_LETTER_ERROR=-2
ASIGNMENT_ERROR=-3
EOF_ERROR=-4
OUT_OF_BOUNDS_ERROR=-5

array_of_states=[
    #State:Start
    [state_start,state_dig,state_letter,tokens_plus,tokens_minus,tokens_leftBlock,tokens_rightBlock,tokens_leftParenthesis,tokens_rightParenthesis,tokens_leftBracket,tokens_rightBracket,tokens_coma,tokens_Qmark,tokens_fullStop,state_asgn,
     tokens_equal,state_smaller,state_larger,state_rem,state_start,tokens_EOF,UNEXPECTED_INPUT_ERROR,tokens_mult,tokens_div],
    #State:Dig
    [tokens_digit,state_dig,UNEXPECTED_LETTER_ERROR,tokens_digit,tokens_digit,tokens_digit,tokens_digit,tokens_digit,tokens_digit,tokens_digit,tokens_digit,tokens_digit,tokens_digit,tokens_digit,tokens_digit,tokens_digit,tokens_digit,
    tokens_digit,tokens_digit,tokens_digit,tokens_digit,UNEXPECTED_INPUT_ERROR,tokens_digit,tokens_digit],
    #State:Letter
    [tokens_id,state_letter,state_letter,tokens_id,tokens_id,tokens_id,tokens_id,tokens_id,tokens_id,tokens_id,tokens_id,tokens_id,tokens_id,tokens_id,tokens_id,tokens_id,tokens_id,tokens_id,tokens_id,tokens_id,tokens_id,UNEXPECTED_INPUT_ERROR
    ,tokens_id,tokens_id],
    #State:Assignment
    [ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR
    ,ASIGNMENT_ERROR,tokens_asgn,ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR,UNEXPECTED_INPUT_ERROR,ASIGNMENT_ERROR,ASIGNMENT_ERROR],
    #State:Smaller
    [tokens_lessThan,tokens_lessThan,tokens_lessThan,tokens_lessThan,tokens_lessThan,tokens_lessThan,tokens_lessThan,tokens_lessThan,tokens_lessThan,tokens_lessThan,tokens_lessThan,tokens_lessThan,tokens_lessThan,tokens_lessThan,
    tokens_lessThan,tokens_lessThanOrEq,tokens_lessThan,tokens_diff,tokens_lessThan,tokens_lessThan,tokens_lessThan,UNEXPECTED_INPUT_ERROR,tokens_lessThan,tokens_lessThan],
    #State:Larger
    [tokens_greaterThan,tokens_greaterThan,tokens_greaterThan,tokens_greaterThan,tokens_greaterThan,tokens_greaterThan,tokens_greaterThan,tokens_greaterThan,tokens_greaterThan,tokens_greaterThan,tokens_greaterThan,tokens_greaterThan,
    tokens_greaterThan,tokens_greaterThan,tokens_greaterThan,tokens_greaterThanOrEq,tokens_greaterThan,tokens_greaterThan,tokens_greaterThan,tokens_greaterThan,tokens_greaterThan,UNEXPECTED_INPUT_ERROR,tokens_greaterThan,tokens_greaterThan],
    #State:Rem
    [state_rem,state_rem,state_rem,state_rem,state_rem,state_rem,state_rem,state_rem,state_rem,state_rem,state_rem,state_rem,state_rem,state_rem,state_rem,state_rem,state_rem,state_rem,state_start,state_rem,EOF_ERROR,state_rem,
    state_rem,state_rem]]

line = 1
def lex():
    global line

    tokens_string = ''
    current_state = state_start
    linecounter = line
    Arraylex = []

    while (current_state >= 0 and current_state <= 6):
        charinput = file.read(1)

        if (charinput == ' ' or charinput == '\t'):
            tokens_charinput = space
        elif (charinput in digit_list):
            tokens_charinput = digit
        elif (charinput in letter_list):
            tokens_charinput = letter
        elif (charinput == '+'):
            tokens_charinput = plusSign
        elif (charinput == '-'):
            tokens_charinput = minusSign
        elif (charinput == '{'):
            tokens_charinput = leftBlock
        elif (charinput == '}'):
            tokens_charinput = rightBlock
        elif (charinput == '('):
            tokens_charinput = leftParenthesis
        elif (charinput == ')'):
            tokens_charinput = rightParenthesis
        elif (charinput == '['):
            tokens_charinput = leftBracket
        elif (charinput == ']'):
            tokens_charinput = rightBracket
        elif (charinput == ','):
            tokens_charinput = coma
        elif (charinput == ';'):
            tokens_charinput = questionMark
        elif (charinput == '.'):
            tokens_charinput = fullStop
        elif (charinput == ':'):
            tokens_charinput = colon
        elif (charinput == '='):
            tokens_charinput = equal_sign
        elif (charinput == '<'):
            tokens_charinput = lessThan
        elif (charinput == '>'):
            tokens_charinput = greaterThan
        elif (charinput == '#'):
            tokens_charinput = comment
        elif (charinput == '\n'):
            linecounter  += 1
            tokens_charinput = newLine
        elif (charinput == ''):
            tokens_charinput = EOF
        elif (charinput == '*'):
            tokens_charinput = multSign
        elif (charinput == '/'):
            tokens_charinput = divSign
        else:
            tokens_charinput = unexpected_character

        current_state = array_of_states[current_state][tokens_charinput]
        if (len(tokens_string) < 30):
            if (current_state != state_start and current_state != state_rem):
                tokens_string += charinput
        else:
            current_state = OUT_OF_BOUNDS_ERROR

    if (current_state == tokens_id or current_state == tokens_digit or current_state == tokens_lessThan or current_state == tokens_greaterThan):
        if (charinput == '\n'):
            linecounter -= 1
        charinput = file.seek(file.tell() - 1, 0)
        tokens_string = tokens_string[:-1]

    if (current_state == tokens_digit):
        if (tokens_string.isdigit() >= pow(2, 32)):
                current_state = OUT_OF_BOUNDS_ERROR

    if (current_state == tokens_id):
        if (tokens_string == 'program'):
            current_state = tokens_program
        elif (tokens_string == 'if'):
            current_state = tokens_if
        elif (tokens_string == 'switchcase'):
            current_state = tokens_switchcase
        elif (tokens_string == 'not'):
            current_state = tokens_not
        elif (tokens_string == 'function'):
            current_state = tokens_function
        elif (tokens_string == 'input'):
            current_state = tokens_input
        elif (tokens_string == 'declare'):
            current_state = tokens_declare
        elif (tokens_string == 'else'):
            current_state = tokens_else
        elif (tokens_string == 'forcase'):
            current_state = tokens_forcase
        elif (tokens_string == 'and'):
            current_state = tokens_and
        elif (tokens_string == 'procedure'):
            current_state = tokens_procedure
        elif (tokens_string == 'print'):
            current_state = tokens_print
        elif (tokens_string == 'while'):
            current_state = tokens_while
        elif (tokens_string == 'incase'):
            current_state = tokens_incase
        elif (tokens_string == 'or'):
            current_state = tokens_or
        elif (tokens_string == 'call'):
            current_state = tokens_call
        elif (tokens_string == 'case'):
            current_state = tokens_case
        elif (tokens_string == 'return'):
            current_state = tokens_return
        elif (tokens_string == 'default'):
            current_state = tokens_default
        elif (tokens_string == 'in'):
            current_state = tokens_in
        elif (tokens_string == 'inout'):
            current_state = tokens_inout

    if (current_state == UNEXPECTED_INPUT_ERROR):
        print("UNEXPECTED_INPUT_ERROR,please enter a valid input")
    elif (current_state == UNEXPECTED_LETTER_ERROR):
        print("UNEXPECTED_LETTER_ERROR ,please enter digit as input.")
    elif (current_state == ASIGNMENT_ERROR):
        print("ASIGNMENT_ERROR ,the program expected an equal sign after colon.")
    elif (current_state == EOF_ERROR):
        print("EOF_ERROR , you forgot to close the comments before the end of the program ")
    elif (current_state == OUT_OF_BOUNDS_ERROR):
        print(" OUT_OF_BOUNDS_ERROR the input is out bounds or the input is over 30 characters.")

    Arraylex.append(current_state)
    Arraylex.append(tokens_string)
    Arraylex.append(linecounter)
    line = linecounter
    return Arraylex
#endiamesos kwdikas
global cFile

global listQuads
listQuads = []
countQuad = 1
counter = 1
tempDeclarationList = []

def nextQuad():
    global countQuad

    return countQuad

def genquad(op,x,y,z):
    global countQuad
    global listQuads

    list = []
    list.insert(0,nextQuad())
    list.insert(1,op)
    list.insert(2,x)
    list.insert(3,y)
    list.insert(4,z)
    countQuad+=1
    listQuads.append(list[:])

    return list

def newtemp():

    global counter
    global tempDeclarationList


    list = ['T_']
    list.append(str(counter))
    newlist ="".join(list)
    counter +=1
    tempDeclarationList += [newlist]

    ent = Entity()
    ent.type = 'TEMP'
    ent.name = newlist
    ent.tempVar.offset = computeOffset()
    newEntity(ent)

    return newlist

def emptylist():
    return []

def makelist(x):

    declarList = [x]

    return declarList

def merge(list1 , list2):

    totallist = []
    totallist += list1 + list2

    return totallist

def backpatch(list, z):


    global listQuads

    for i in list:
        for j in range(len(listQuads)):
             if listQuads[j][0] == i:
                listQuads[j][4] = z
    return

#pinakas symbolwn
class Argument():

    def __init__(self):
        self.name = ''
        self.parMode = ''
        self.type = 'Int'



class Entity():
    def __init__(self):
        self.name = ''
        self.type = ''
        self.variable = self.Variable()
        self.subprogram = self.SubProgram()
        self.parameter = self.Parameter()
        self.tempVar = self.TempVar()

    class Variable:
        def __init__(self):
            self.type = 'Int'
            self.intOffset = 0.

    class SubProgram:
        def __init__(self):
            self.type = ''
            self.startingQuad = 0
            self.frameLength = 0
            self.argumentList = []

    class Parameter:
        def __init__(self):
            self.parMode = ''
            self.intOffset = 0

    class TempVar:
        def __init__(self):
            self.type = 'Int'
            self.intOffset = 0
class Scope():
    def __init__(self):
        self.name = ''
        self.pointerEntityList = []
        self.nestingLevel = 0
        self.pointerEnclosingScope = None

def newScope(name):
    global upperComparingScope

    newscope = Scope()
    newscope.name = name
    newscope.pointerEnclosingScope = upperComparingScope

    if (upperComparingScope == None):
        newscope.nestingLevel = 0
    else:
        newscope.nestingLevel = upperComparingScope.nestingLevel + 1

    upperComparingScope = newscope

def deleteScope():
    global upperComparingScope

    deletedScope = upperComparingScope
    upperComparingScope = upperComparingScope.pointerEnclosingScope
    del deletedScope

def newEntity(object):
    global upperComparingScope

    upperComparingScope.pointerEntityList.append(object)

upperComparingScope = None


def newArgument(object):
    global upperComparingScope

    upperComparingScope.pointerEntityList[-1].subprogram.argumentList.append(object)

def computeOffset():
    global upperComparingScope

    counter = 0
    if (upperComparingScope.pointerEntityList != []):
        for i in (upperComparingScope.pointerEntityList):
            if ( i.type == 'PARAM' or i.type == 'VAR' or i.type == 'TEMP'):
                counter += 1
    intOffset = 12 + (counter * 4)

    return intOffset


def computeStartingQuad():
    global upperComparingScope

    pointerEnclosingScope = upperComparingScope.pointerEnclosingScope
    pointerEnclosingScope = pointerEnclosingScope.pointerEntityList[-1].subprogram.startingQuad
    pointerEnclosingScope = nextQuad()

def computeFramelength():
    global upperComparingScope

    pointerEnclosingScope =upperComparingScope.pointerEnclosingScope
    pointerEnclosingScope =pointerEnclosingScope.pointerEntityList[-1].subprogram.frameLength
    pointerEnclosingScope = computeOffset()

def addParameters():
    global upperComparingScope

    pointerEnclosingScope = upperComparingScope.pointerEnclosingScope
    pointerEnclosingScope =pointerEnclosingScope.pointerEntityList[-1].subprogram.argumentList
    for j in pointerEnclosingScope:
        ent = Entity()
        ent.name = j.name
        ent.type = 'PARAM'
        ent.parameter.parMode = j.parMode
        ent.parameter.intOffset = computeOffset()
        newEntity(ent)


def SymbolBoardPrint():
    global upperComparingScope

    print("------------------------------------------------------------------------------------------------------------")
    sc = upperComparingScope
    while sc != None:
        print("scope: " + "name:" + sc.name + " nestingLevel:" + str(sc.nestingLevel))
        for i in sc.pointerEntityList:
            if (i.type == 'VAR'):
                print("\tentity: "+ " name:" + i.name + "--" + "type:" + i.type + "--" + "variable-type:" + i.variable.type + "--" + "offset:" + str(i.variable.intOffset))
            elif (i.type == 'TEMP'):
                print("\tentity: " + " name:" + i.name + "--" + "type:" + i.type + "--" + "temp-type:" + i.tempVar.type + "--" + "offset:" + str(i.tempVar.intOffset))
            elif (i.type == 'SUBPR'):
                if (i.subprogram.type == 'Function'):
                    print("\tentity: " + " name:" + i.name + "--" + "type:" + i.type + "--" + "function-type:" + i.subprogram.type + "--" + "startQuad:" + str(i.subprogram.startingQuad) + "--" + "frameLength:" + str(i.subprogram.frameLength))
                    for j in i.subprogram.argumentList:
                        print("\t\targument: " + " name:" + j.name + "--" + "type:" + j.type + "--" + "parMode:" + j.parMode)
                elif (i.subprogram.type == 'Procedure'):
                    print("\tentity: " + " name:" + i.name + "==" + "type:" + i.type + "--" + "procedure-type:" + i.subprogram.type + "--" + "startQuad:" + str(i.subprogram.startingQuad) + "--" + "frameLength:" + str(i.subprogram.frameLength))
                    for j in i.subprogram.argumentList:
                        print("\t\targument: " + "--" + "type:" + j.type + "--" + "parMode:" + j.parMode)
            elif (i.type == 'PARAM'):
                print("\tentity: "+ "--" + "type:" + i.type + "--" + "mode:" + i.parameter.parMode + "--" + "offset:" + str(i.parameter.intOffset))
        sc = sc.pointerEnclosingScope

    print("------------------------------------------------------------------------------------------------------------")
#final code
acsTest = open('ascTest.asm','w')
def connector(v):
    global upperComparingScope

    sc = upperComparingScope #i = entity
    while sc != None:
        for i in sc.pointerEntityList:
            if (i.name == v):
                return (sc, i)
        sc = sc.enclosingScope

    print("Error! No connection between scope-entity " + str(v))

def gnlvcode(v):
    global ascTest
    global upperComparingScope
    global intOffset

    ascTest.write('lw to, -4(sp) ')
    (sc1,i1)=connector(v)

    times=-1
    temp=upperComparingScope.nestingLevel-sc1.nestingLevel
    times=times+temp
    while times!=0:
        ascTest.write('lw t0,-4(t0)')
        times=times-1
    ascTest.write('addi $t0,$t0, -%d' %(intOffset))

def loadvr(v,reg):

    global ascTest
    global upperComparingScope

    (sc1,i1)=connector(v)
    if(v.isDigit()):
        ascTest.write('li tr%d,%s' % (reg,v))
    else:
        if (sc1.nestingLevel==0 and i1.type=='TEMP'):
            ascTest.write('lw tr,-%d(gp)' % (i1.variable.intOffset))
        elif (sc1.nestingLevel==0 and i1.type=='VAR'):
            ascTest.write('lw tr,-%d(gp)' %(i1.variable.intOffset))
        elif sc1.nestingLevel == upperComparingScope.nestingLevel:
            if (i1.type=='VAR'): #local variable
                ascTest.write('lw tr,-%d(sp)' %(i1.variable.intOffset))
            elif (i1.type=='PARAM' and i1.parameter.parMode=='CV'):
                ascTest.write('lw tr,-%d(sp)' %(i1.parameter.intOffset))
            elif (i1.type=='TEMP'):
                ascTest.write('lw tr,-%d(sp)' %(i1.tempVar.intOffset))
            elif (i1.type=='PARAM' and i1.parameter.parMode=='REF'):
                ascTest.write('lw t0,-%d(sp)' %(i1.parameter.intOffset))
                ascTest.write('lw tr,(t0)')

def storerv(reg,v):
    global ascTest
    global upperComparingScope


    (sc1,i1)=connector(v)

    if (sc1.nestingLevel==0 and i1.type=='TEMP'):
        ascTest.write('sw tr,-%d(gp)' % (i1.variable.intOffset))
    elif (sc1.nestingLevel==0 and i1.type=='VAR'):
        ascTest.write('sw tr,-%d(gp)' %(i1.variable.intOffset))
    elif sc1.nestingLevel == upperComparingScope.nestingLevel:
        if (i1.type=='VAR'):
            ascTest.write('sw tr,-%d(sp)' %(i1.variable.intOffset))
        elif (i1.type=='PARAM' and i1.parameter.parMode=='CV'):
            ascTest.write('sw tr,-%d(sp)' %(i1.parameter.intOffset))
        elif (i1.type=='TEMP'):
            ascTest.write('sw tr,-%d(sp)' %(i1.tempVar.intOffset))
        elif (i1.type=='PARAM' and i1.parameter.parMode=='REF'):
            ascTest.write('sw t0,-%d(sp)' %(i1.parameter.intOffset))
            ascTest.write('sw tr,(t0)')
    elif sc1.nestingLevel < upperComparingScope.nestingLevel:
        if i1.type == 'VAR':
            gnlvcode(v)
            ascTest.write('sw tr,(t0)' )
        elif i1.type == 'PARAM' and i1.parameter.parModede == 'CV':
            gnlvcode(v)
            ascTest.write('sw tr,(t0)' )
        elif i1.type == 'PARAM' and i1.parameter.parMode == 'REF':
            gnlvcode(v)
            ascTest.write('lw t0,(t0)')
            ascTest.write('sw tr,(t0)')

def lastCheck():
    global upperComparingScope
    global listQuads
    global ascTest

    for i in range(len(listQuads)): #Parsing all available Quads
        ascTest.write('L%d:' %(listQuads[i][0]))

        if (listQuads[i][1] == 'Jump'):
            ascTest.write('b L' + str(listQuads[i][4]))
        elif (listQuads[i][1] == '='):
            loadvr(listQuads[i][2],1)
            loadvr(listQuads[i][3],2)
            ascTest.write('beq, t1,t2,label'+str(listQuads[i][4]))
        elif (listQuads[i][1] == '<'):
            loadvr(listQuads[i][2], 1)
            loadvr(listQuads[i][3], 2)
            ascTest.write('blt, t1,t2,label' + str(listQuads[i][4]))
        elif (listQuads[i][1] == '>'):
            loadvr(listQuads[i][2], 1)
            loadvr(listQuads[i][3], 2)
            ascTest.write('bgt, t1,t2,label' + str(listQuads[i][4]))
        elif (listQuads[i][1] == '<='):
            loadvr(listQuads[i][2], 1)
            loadvr(listQuads[i][3], 2)
            ascTest.write('ble, t1,t2,label' + str(listQuads[i][4]))
        elif (listQuads[i][1] == '>='):
            loadvr(listQuads[i][2], 1)
            loadvr(listQuads[i][3], 2)
            ascTest.write('bge, t1,t2,label' + str(listQuads[i][4]))
        elif (listQuads[i][1] == '<>'):
            loadvr(listQuads[i][2], 1)
            loadvr(listQuads[i][3], 2)
            ascTest.write('bne, t1,t2,label' + str(listQuads[i][4]))
        elif (listQuads[i][1] == ':='):
            loadvr(listQuads[i][2],1)
            storerv(1,listQuads[i][4])
        elif (listQuads[i][1] == '+'):
            loadvr(listQuads[i][2],1)
            loadvr(listQuads[i][3], 2)
            ascTest.write('add t1,t1,t2')
            storerv(1,listQuads[i][4])
        elif (listQuads[i][1] == '-'):
            loadvr(listQuads[i][2], 1)
            loadvr(listQuads[i][3], 2)
            ascTest.write('sub t1,t1,t2')
            storerv(1, listQuads[i][4])
        elif (listQuads[i][1] == '*'):
            loadvr(listQuads[i][2], 1)
            loadvr(listQuads[i][3], 2)
            ascTest.write('mul t1,t1,t2')
            storerv(1, listQuads[i][4])
        elif (listQuads[i][1] == 'div'):
            loadvr(listQuads[i][2], 1)
            loadvr(listQuads[i][3], 2)
            ascTest.write('div t1,t1,t2')
            storerv(1, listQuads[i][4])
        elif (listQuads[i][1]=='retv'):
            loadvr(listQuads[i][2],1)
            ascTest.write('lw t0,-8(sp)')
            ascTest.write('sw t1,(t0)')


# Syntaktikos Analyths
def syntax_an():
    global line
    global lexarray
    lexarray = []
    lexarray = lex()
    line = lexarray[2]

    def program():
        global line
        global lexarray

        if(lexarray[0] == tokens_program):
            lexarray = lex()
            line = lexarray[2]

            if(lexarray[0] == tokens_id):
                ID = lexarray[1]
                lexarray = lex()
                line = lexarray[2]

                block(ID,1)

                if(lexarray[0] == tokens_fullStop):
                    lexarray = lex()
                    line = lexarray[2]

                else:
                    print("Every program has to end with a fullstop" , line)
                    exit(-1)

            else:
                print("There is no name of the program", line)
                exit(-1)

        else:
            print("program has to be the starting symbol", line)
            exit(-1)

    def block(name,flag):
        global lexarray
        global line

        if(lexarray[0] == tokens_leftBlock):
            lexarray =lex()
            line = lexarray[2]
            newScope(name)

            if(flag!=1):
                addParameters()

            declarations()

            subprograms()

            genquad('begin_block',name,'_','_')

            blockstatements()

            if(lexarray[0] == tokens_rightBlock):
                lexarray = lex()
                line = lexarray[2]

            if(flag == 1):
                genquad('halt', '_', '_', '_')
            else:
                computeFramelength()

            genquad('end_block', name, '_', '_')

            print("Symbol Board:")
            SymbolBoardPrint()
            #lastCheck()
            deleteScope()
            print("The last scope is deleted")

        else:
            print("Problem with the symbol left block",line)
            exit(-1)

        return

    def declarations():
        global lexarray
        global line

        while(lexarray[0] == tokens_declare):
            lexarray = lex()
            line = lexarray[2]

            varlist()

            if(lexarray[0] == tokens_Qmark):
                lexarray = lex()
                line = lexarray[2]
            else:
                print("Problem with the questionmark at the end of varlist",line)
                exit(-1)

        return

    def varlist():
        global lexarray
        global line

        if(lexarray[0] == tokens_id):
            name = lexarray[1];
            line = lexarray[2]

            i = Entity()
            i.type = 'VAR'
            i.name = lexarray[1]
            i.variable.intOffset = computeOffset()
            newEntity(i)

            lexarray = lex()
        while(lexarray[0] == tokens_coma):
                    lexarray = lex()
                    line = lexarray[2]

                    if(lexarray[0] == tokens_id):
                        name = lexarray[1]
                        line = lexarray[2]

                        i = Entity()
                        i.type = 'VAR'
                        i.name = lexarray[1]
                        i.variable.intOffset = computeOffset()
                        newEntity(i)

                        lexarray = lex()
                    else:
                         print("Problem with the coma in the keyword id",line)
                         exit(-1)

        return

    def subprograms():
        global line
        global lexarray

        while(lexarray[0] == tokens_function or lexarray[0] == tokens_procedure):

            subprogram()

        return

    def subprogram():
        global line
        global lexarray

        if(lexarray[0] == tokens_function):
            lexarray = lex()
            line = lexarray[2]

            if(lexarray[0] == tokens_id):
                ID = lexarray[1]
                line = lexarray[2]

                i = Entity()
                i.type = 'SUBPR'
                i.name = lexarray[1]
                i.variable.intOffset = computeOffset()
                newEntity(i)

                lexarray = lex()
                if(lexarray[0] == tokens_leftParenthesis):
                            lexarray = lex()
                            line = lexarray[2]

                            formalparlist()

                            if(lexarray[0] == tokens_rightParenthesis):
                                lexarray = lex()
                                line = lexarray[2]

                                block(ID,0)
                            else:
                                print("Problem with the right parenthesis in ", line)
                                exit(-1)

                else:
                        print("Problem with the left parentesis in ", line)
                        exit(-1)

            else:
                    print("Problem with the id in", line)
                    exit(-1)

        elif(lexarray[0] == tokens_procedure):
                lexarray = lex()
                line = lexarray[2]

                if(lexarray[0] == tokens_id):
                    ID = lexarray[1]
                    line = lexarray[2]

                    i = Entity()
                    i.type = 'SUBPR'
                    i.name = lexarray[1]
                    i.subprogram.type = 'Procedure'
                    newEntity(i)

                    lexarray = lex()
                    if(lexarray[0] == tokens_leftParenthesis):
                            lexarray = lex()
                            line = lexarray[2]

                            formalparlist()

                            if(lexarray[0] == tokens_rightParenthesis):
                                lexarray = lex()
                                line = lexarray[2]

                                block(ID,0)

                            else:
                                print("Problem with the right parenthesis in  ", line)
                                exit(-1)

                    else:
                        print("Problem with the left parentesis in", line)
                        exit(-1)

                else:
                     print("Problem with the id in", line)
                     exit(-1)
        else:
            print("Problem with the procedure in", line )
            exit(-1)

    def formalparlist():
        global lexarray
        global line

        formalparitem()

        while(lexarray[0] == tokens_coma):
            lexarray = lex()
            line = lexarray[2]

            formalparitem()

        return

    def formalparitem():
        global line
        global lexarray

        if(lexarray[0] == tokens_in):
            lexarray = lex()
            line = lexarray[2]

            if (lexarray[0] == tokens_id):
                line = lexarray[2]

                j = Argument()
                j.name = lexarray[0]
                j.parMode = 'CV'
                newArgument(j)

                lexarray = lex()
            else:
                print("Problem with the id in" ,line)
                exit(-1)

        elif(lexarray[0] == tokens_inout):
            lexarray = lex()
            line = lexarray[2]

            if (lexarray[0] == tokens_id):

                line = lexarray[2]

                j = Argument()
                j.name = lexarray[0]
                j.parMode = 'REF'
                newArgument(j)

                lexarray = lex()

            else:
                print("Problem with the id in",line)
                exit(-1)

        else:
            print("Problem with the tokens_inout in " , line)
            exit(-1)

    def statements():
        global lexarray
        global line

        if (lexarray[0] == tokens_leftBlock):
            lexarray = lex()
            line = lexarray[2]

            statement()

            while (lexarray[0] == tokens_Qmark):
                lexarray = lex()
                line = lexarray[2]

                statement()

            if (lexarray[0] == tokens_rightBlock):
                lexarray = lex()
                line = lexarray[2]

            else:
                print("Problem with the block in the statement function", line)
                exit(-1)
        else:

            statement()
            if (lexarray[0] == tokens_Qmark):
                lexarray = lex()
                line = lexarray[2]

            else:
                print("Problem with thw Qmark in statement function", line)
                exit(-1)


    def blockstatements():
        global lexarray
        global line

        statement()

        while(lexarray[0] == tokens_Qmark):
            lexarray = lex()
            line = lexarray[2]

            statement()
        return

    def statement():
        global lexarray
        global line

        if(lexarray[0] == tokens_id):
            assignStat()

        elif(lexarray[0] == tokens_if):
            ifStat()

        elif(lexarray[0] == tokens_while):
            whileStat()

        elif(lexarray[0] == tokens_switchcase):
            switchcaseStat()

        elif(lexarray[0] == tokens_forcase):
            forcaseStat()

        elif(lexarray[0] == tokens_incase):
            incaseStat()

        elif(lexarray[0] == tokens_call):
            callStat()

        elif(lexarray[0] == tokens_return):
            returnStat()

        elif(lexarray[0] == tokens_input):
            inputStat()

        elif(lexarray[0] == tokens_print):
            printStat()

        return

    def assignStat():
        global lexarray
        global line

        if(lexarray[0] == tokens_id):
            IDplace = lexarray[1]
            lexarray = lex()
            line = lexarray[2]

            if(lexarray[0] == tokens_asgn):
                lexarray = lex()
                line = lexarray[2]

                Eplace = expression()
                genquad(':=',Eplace,'_',IDplace) #p1

            else:
                print("Problem in the assigment statement " ,line)
                exit(-1)

        else:
            print("Problem in the  id of the assigment statement ", line)
            exit(-1)

    def ifStat():
        global lexarray
        global line

        if(lexarray[0] == tokens_if):
            lexarray = lex()
            line = lexarray[2]

            if(lexarray[0] == tokens_leftParenthesis):
                lexarray = lex()
                line = lexarray[2]

                conditionlist = condition()
                backpatch(conditionlist[0],nextQuad()) #p1

                if(lexarray[0] == tokens_rightParenthesis):
                    lexarray = lex()
                    line = lexarray[2]

                    statements()
                    iflist = makelist(nextQuad()) #p2
                    genquad('jump','_','_','_') #p2
                    backpatch(conditionlist[1],nextQuad()) #p2
                    elsepart()
                    backpatch(iflist,nextQuad()) #p3
                else:
                    print("Problem in the right parenthesis in the if statement  ", line)
                    exit(-1)

            else:
                print("Problem in the left parenthesis in the if statement  ", line)
                exit(-1)

        else:
            print("Problem in the if statement ", line)
            exit(-1)


    def elsepart():
        global line
        global lexarray

        if(lexarray[0] == tokens_else):
            lexarray = lex()
            line = lexarray[2]

            statements()

        return

    def whileStat():
        global line
        global lexarray

        if(lexarray[0] == tokens_while):
            lexarray = lex()
            line = lexarray[2]

            if(lexarray[0] == tokens_leftParenthesis):
                lexarray = lex()
                line = lexarray[2]

                conQuad = nextQuad() #p0
                conditionlist = condition()
                backpatch(conditionlist[0],nextQuad()) #p1

                if(lexarray[0] == tokens_rightParenthesis):
                    lexarray = lex()
                    line = lexarray[2]

                    statements()
                    genquad('jump','_','_',conQuad) #p2
                    backpatch(conditionlist[1],nextQuad()) #p2

                else:
                    print("Problem in the right parenthesis in while statement ", line)
                    exit(-1)

            else:
                print("Problem in the left parenthesis in the while  statement ", line)
                exit(-1)

        else:
            print("Problem in the in the while statement ", line)
            exit(-1)

    def switchcaseStat():
        global line
        global lexarray

        if(lexarray[0] == tokens_switchcase):
            lexarray = lex()
            line = lexarray[2]
            exitList = emptylist() #p0

            while(lexarray[0] == tokens_case):
                lexarray = lex()
                line = lexarray[2]

                if(lexarray[0] == tokens_leftParenthesis):
                   lexarray = lex()
                   line = lexarray[2]

                   conditionList = condition()
                   backpatch(conditionList[0],nextQuad()) #p1

                   if(lexarray[0] == tokens_rightParenthesis):
                       lexarray = lex()
                       line = lexarray[2]

                       statements()
                       t = makelist(nextQuad())  # p2
                       genquad('jump', '_', '_', '_')  # p2
                       exitList = merge(exitList, t)  # p2
                       backpatch(conditionList[1], nextQuad())  # p2

                   else:
                       print("Problem in the right parenthesis in the switch statement ", line)
                       exit(-1)

                else:
                    print("Problem in the left parenthesis in the switch statement", line)
                    exit(-1)

            if(lexarray[0] == tokens_default):
                lexarray = lex()
                line = lexarray[2]

                statements()
                backpatch(exitList, nextQuad())  # p3

            else:
                print("Problem in the default  in the switch statement", line)
                exit(-1)

        else:
            print("Problem  in the switch statement", line)
            exit(-1)

    def forcaseStat():
        global line
        global lexarray

        if (lexarray[0] == tokens_forcase):
            lexarray = lex()
            line = lexarray[2]
            firstCondQuad = nextQuad() #p1

            while (lexarray[0] == tokens_case):
                lexarray = lex()
                line = lexarray[2]

                if (lexarray[0] == tokens_leftParenthesis):
                    lexarray = lex()
                    line = lexarray[2]

                    conditionList = condition()
                    backpatch(conditionList[0],nextQuad()) #p2

                    if (lexarray[0] == tokens_rightParenthesis):
                        lexarray = lex()
                        line = lexarray[2]

                        statements()
                        genquad('jump','_','_',firstCondQuad) #p3
                        backpatch(conditionList[1],nextQuad()) #p3
                        
                    else:
                        print("Problem in the right parenthesis in the forcase statement ", line)
                        exit(-1)

                else:
                    print("Problem in the left parenthesis in the forcase statement", line)
                    exit(-1)

            if (lexarray[0] == tokens_default):
                lexarray = lex()
                line = lexarray[2]

                statements()

            else:
                print("Problem in the default  in the forcase statement", line)
                exit(-1)

        else:
            print("Problem  in the forcase statement", line)
            exit(-1)

    def incaseStat():
        global line
        global lexarray

        if (lexarray[0] == tokens_incase):
            lexarray = lex()
            line = lexarray[2]

            flag = newtemp() #p1
            firstCondQuad = nextQuad() #p1
            genquad(':=','0','_',flag) #p1

            while (lexarray[0] == tokens_case):
                lexarray = lex()
                line = lexarray[2]

                if (lexarray[0] == tokens_leftParenthesis):
                    lexarray = lex()
                    line = lexarray[2]

                    conditionList = condition()
                    backpatch(conditionList[0],nextQuad()) #p2

                    if (lexarray[0] == tokens_rightParenthesis):
                        lexarray = lex()
                        line = lexarray[2]

                        statements()
                        genquad(':=','1','_',flag) #p3
                        backpatch(conditionList[1],nextQuad()) #p3
    
                    else:
                        print("Problem int the right parenthesis in the incase  statement", line)
                        exit(-1)

                else:
                    print("Problem int the left parenthesis in the incase  statement", line)
                    exit(-1)

            genquad('=', '1', flag, firstCondQuad) #p4

        else:
            print("Problem in the incase  statement", line)
            exit(-1)

    def returnStat():
        global line
        global lexarray

        if(lexarray[0] == tokens_return):
            lexarray = lex()
            line = lexarray[2]

            if(lexarray[0] == tokens_leftParenthesis):
                lexarray = lex()
                line = lexarray[2]

                Eplace = expression()
                genquad('retv',Eplace,'_','_') #p1

                if(lexarray[0] == tokens_rightParenthesis):
                    lexarray = lex()
                    line = lexarray[2]

                else:
                    print("Problem in the right parenthesis in the return statement", line)
                    exit(-1)

            else:
                print("Problem in the left parenthesis in the return statement", line)
                exit(-1)

        else:
            print("Problem in the return statement", line)
            exit(-1)

    def callStat():
        global line
        global lexarray

        if (lexarray[0] == tokens_call):
            lexarray = lex()
            line = lexarray[2]

            if (lexarray[0] == tokens_id):
                id = lexarray[1]
                lexarray = lex()
                line = lexarray[2]

                if (lexarray[0] == tokens_leftParenthesis):
                    lexarray = lex()
                    line = lexarray[2]

                    actualparlist()
                    genquad('call',id,'_','_')

                    if (lexarray[0] == tokens_rightParenthesis):
                        lexarray = lex()
                        line = lexarray[2]

                    else:
                        print("Problem in the right parenthesis in the call statement", line)
                        exit(-1)

                else:
                    print("Problem in the left parenthesis in the call statement", line)
                    exit(-1)

            else:
                print("Problem in the id in the call statement", line)
                exit(-1)

        else:
            print("Problem in the call statement", line)
            exit(-1)

    def printStat():
        global line
        global lexarray

        if (lexarray[0] == tokens_print):
            lexarray = lex()
            line = lexarray[2]

            if (lexarray[0] == tokens_leftParenthesis):
                lexarray = lex()
                line = lexarray[2]

                Eplace = expression()
                genquad('out',Eplace,'_','_') #p2

                if (lexarray[0] == tokens_rightParenthesis):
                    lexarray = lex()
                    line = lexarray[2]

                else:
                    print("Problem in the right parenthsesis in the print statement", line)
                    exit(-1)

            else:
                print("Problem in the left parenthsesis in the print statement", line)
                exit(-1)

        else:
            print("Problem in the print statement ", line)
            exit(-1)

    def inputStat():
        global line
        global lexarray

        if (lexarray[0] == tokens_input):
            lexarray = lex()
            line = lexarray[2]

            if (lexarray[0] == tokens_leftParenthesis):
                lexarray = lex()
                line = lexarray[2]

                if (lexarray[0] == tokens_id):
                    IDplace = lexarray[1]
                    genquad('inp',IDplace,'_','_') #p1
                    lexarray = lex()
                    line = lexarray[2]

                    if (lexarray[0] == tokens_rightParenthesis):
                        lexarray = lex()
                        line = lexarray[2]

                    else:
                        print("Problem in the right parenthsesis in the input statement", line)
                        exit(-1)

                else:
                    print("Problem in the id in the input statement", line)
                    exit(-1)

            else:
                print("Problem in the left parenthsesis in the input statement", line)
                exit(-1)

        else:
            print("Problem in the input statement ", line)
            exit(-1)

    def actualparlist():
        global line
        global lexarray

        actualparitem()

        while(lexarray[0] == tokens_coma):
            lexarray = lex()
            line = lexarray[2]

            actualparitem()

        return

    def actualparitem():
        global line
        global lexarray

        if (lexarray[0] == tokens_in):
            lexarray = lex()
            line = lexarray[2]

            a = expression()
            genquad('par',a,'CV','_')

        elif(lexarray[0] == tokens_inout):
            lexarray = lex()
            line = lexarray[2]

            if (lexarray[0] == tokens_id):
                b = lexarray[1]
                lexarray = lex()
                line = lexarray[2]

                genquad('par',b,'REF','_')

            else:
                print("Problem in the id in the actualparitem statement", line)
                exit(-1)

        else:
            print("Problem in the 'in': by value or 'inout' by reference in actualparitem stetement", line)
            exit(-1)

    def condition():
        global line
        global lexarray

        Btrue = []
        Bfalse = []
        Q1list = boolterm()
        Btrue = Q1list[0] #p1
        Bfalse = Q1list[1] #p1

        while(lexarray[0] == tokens_or):
            lexarray = lex()
            line = lexarray[2]

            backpatch(Bfalse,nextQuad()) #p2
            Q2list = boolterm()
            Btrue = merge(Btrue, Q2list[0]) #p3
            Bfalse = Q2list[1]#p3

        return Btrue, Bfalse

    def boolterm():
        global line
        global lexarray

        Qtrue =[]
        Qfalse = []
        R1list = boolfactor()
        Qtrue = R1list[0] #p1
        Qfalse = R1list[1] #p1

        while (lexarray[0] == tokens_and):
            lexarray = lex()
            line = lexarray[2]

            backpatch(Qtrue,nextQuad()) #p2
            R2list = boolfactor()
            Qfalse = merge(Qfalse,R2list[1])#p3
            Qtrue = R2list[0]#p3

        return Qtrue,Qfalse

    def boolfactor():
        global line
        global lexarray

        Rtrue = []
        Rfalse = []
        if (lexarray[0] == tokens_not):
            lexarray = lex()
            line = lexarray[2]

            if (lexarray[0] == tokens_leftBracket):
                lexarray = lex()
                line = lexarray[2]

                Blist = condition()
                Rtrue = Blist[1]
                Rfalse = Blist[0]

                if (lexarray[0] == tokens_rightBracket):
                    lexarray = lex()
                    line = lexarray[2]

                else:
                    print("Problem with the right bracket  in boolfactor statement", line)
                    exit(-1)

            else:
                print("Problem with the left bracket in boolfactor statement ", line)
                exit(-1)

        elif(lexarray[0] == tokens_leftBracket):
            lexarray = lex()
            line = lexarray[2]

            Blist = condition()
            Rtrue = Blist[0] #P1
            Rfalse = Blist[1]#P1
            if (lexarray[0] == tokens_rightBracket):
                lexarray = lex()
                line = lexarray[2]

            else:
                print("Problem with the bracket in boolfactor statement", line)
                exit(-1)

        else:
            E1place = expression()
            relop = REL_OP()
            E2place = expression()

            Rtrue = makelist(nextQuad()) #P1
            genquad(relop,E1place,E2place,'_')
            Rfalse = makelist(nextQuad())
            genquad('jump','_','_','_')

        return Rtrue,Rfalse

    def expression():
        global lexarray
        global line

        optionalSign()
        T1place = term()

        while(lexarray[0] == tokens_plus or lexarray[0] == tokens_minus):
            plusOrminus = ADD_OP()
            T2place = term()

            w = newtemp()#p1
            genquad(plusOrminus,T1place,T2place,w)#p1
            T1place = w#p1


        Eplace = T1place 
                          
        return Eplace

    def term():
        global line
        global lexarray

        F1place = factor()

        while(lexarray[0] == tokens_mult or lexarray[0] == tokens_div):
            multOrdiv = MUL_OP()
            F2place = factor()

            w = newtemp() #p1
            genquad(multOrdiv,F1place,F2place,w) #p1
            F1place = w #p1

        Tplace = F1place #p2
        return Tplace

    def factor():
        global line
        global lexarray

        if (lexarray[0] == tokens_digit):
            Fplace = lexarray[1]
            lexarray = lex()
            line = lexarray[2]

        elif(lexarray[0] == tokens_leftParenthesis):
            lexarray = lex()
            line = lexarray[2]

            Eplace = expression()
            Fplace = Eplace


            if (lexarray[0] == tokens_rightParenthesis):
                lexarray = lex()
                line = lexarray[2]

            else:
                print("Problem with the right parenthesis in factor statement",line)
                exit(-1)

        elif(lexarray[0] == tokens_id):
            id = lexarray[1]
            lexarray = lex()
            line = lexarray[2]

            Fplace = idtail(id)

        else:
            if (lexarray[0] == tokens_rightParenthesis):
                lexarray = lex()
                line = lexarray[2]

        return Fplace

    def idtail(name):
        global line
        global lexarray

        if (lexarray[0] == tokens_leftParenthesis):
            lexarray = lex()
            line = lexarray[2]

            actualparlist()
            w = newtemp()
            genquad('par',w,'ret','_')
            genquad('call',name,'_','_')

            if (lexarray[0] == tokens_rightParenthesis):
                lexarray = lex()
                line = lexarray[2]
                return w

            else:
                print("Problem with the parenthesis in ", line)
                exit(-1)
        else:
            return name


    def optionalSign():
        global line
        global lexarray

        if(lexarray[0] == tokens_plus or lexarray[0] == tokens_minus):
            ADD_OP()

        return

    def REL_OP():
        global line
        global lexarray

        if (lexarray[0] == tokens_equal):
            relop = lexarray[1]
            lexarray = lex()
            line = lexarray[2]

        elif(lexarray[0] == tokens_lessThanOrEq):
            relop = lexarray[1]
            lexarray = lex()
            line = lexarray[2]

        elif (lexarray[0] == tokens_greaterThanOrEq):
            relop = lexarray[1]
            lexarray = lex()
            line = lexarray[2]

        elif (lexarray[0] == tokens_greaterThan):
            relop = lexarray[1]
            lexarray = lex()
            line = lexarray[2]

        elif (lexarray[0] == tokens_lessThan):
            relop = lexarray[1]
            lexarray = lex()
            line = lexarray[2]

        elif (lexarray[0] == tokens_diff):
            relop = lexarray[1]
            lexarray = lex()
            line = lexarray[2]

        else:
            print("Problem with symbols in REL_OP",line)
            exit(-1)

        return relop

    def ADD_OP():
        global line
        global lexarray

        if (lexarray[0] == tokens_plus):
            plusOrminus = lexarray[1]
            lexarray = lex()
            line = lexarray[2]

        elif (lexarray[0] == tokens_minus):
            plusOrminus = lexarray[1]
            lexarray = lex()
            line = lexarray[2]

        else:
            print("Problem with symbols in ADD_OP", line)
            exit(-1)

        return plusOrminus

    def MUL_OP():
        global line
        global lexarray

        if (lexarray[0] == tokens_mult):
            multOrdiv = lexarray[1]
            lexarray = lex()
            line = lexarray[2]

        elif (lexarray[0] == tokens_div):
            multOrdiv = lexarray[1]
            lexarray = lex()
            line = lexarray[2]

        else:
            print("Problem with symbols in MULL_OP", line)
            exit(-1)

        return multOrdiv

    program()

    print("End of program")

    return

def createIntFile():
    global  ListQuads

    f = open('TestInt.int', 'w')

    for i in range(len(listQuads)):
        quad = listQuads[i]
        f.write(str(quad[0]))
        f.write("  ")
        f.write(str(quad[1]))
        f.write("  ")
        f.write(str(quad[2]))
        f.write("  ")
        f.write(str(quad[3]))
        f.write("  ")
        f.write(str(quad[4]))
        f.write("\n")
    f.close()

def createCfile():
    global listQuads

    h = open('TestC.c','w')
    h.write('int main(){\n\t')

    for i in range(len(listQuads)):
        if (listQuads[i][1] == '+'):
            h.write('L_' +str(i+1) + ': ' + listQuads[i][4] + '='+ listQuads[i][2] + '+' + listQuads[i][3] + '; \n\t')
        elif(listQuads[i][1] == '-'):
            h.write('L_' + str(i + 1) + ': ' + listQuads[i][4] + '=' + listQuads[i][2] + '-' + listQuads[i][3] + '; \n\t')
        elif(listQuads[i][1] == '*'):
            h.write('L_' + str(i + 1) + ': ' + listQuads[i][4] + '=' + listQuads[i][2] + '*' + listQuads[i][3] + '; \n\t')
        elif (listQuads[i][1] == '/'):
            h.write('L_' + str(i + 1) + ': ' + listQuads[i][4] + '=' + listQuads[i][2] + '/' + listQuads[i][3] + '; \n\t')
        elif (listQuads[i][1] == '=='):
            h.write('L_'+str(i+1)+': '+'if ('+listQuads[i][2]+'=='+listQuads[i][3]+') goto L_'+str(listQuads[i][4])+';\n\t')
        elif (listQuads[i][1] == '>'):
            h.write('L_'+str(i+1)+': '+'if ('+listQuads[i][2]+'>'+listQuads[i][3]+') goto L_'+str(listQuads[i][4])+';\n\t')
        elif(listQuads[i][1] == '>='):
            h.write('L_'+str(i+1)+': '+'if ('+listQuads[i][2]+'>='+listQuads[i][3]+') goto L_'+str(listQuads[i][4])+';\n\t')
        elif (listQuads[i][1] == '<'):
            h.write('L_'+str(i+1)+': '+'if ('+listQuads[i][2]+'<'+listQuads[i][3]+') goto L_'+str(listQuads[i][4])+';\n\t')
        elif (listQuads[i][1] == '<='):
            h.write('L_'+str(i+1)+': '+'if ('+listQuads[i][2]+'<='+listQuads[i][3]+') goto L_'+str(listQuads[i][4])+';\n\t')
        elif (listQuads[i][1] == '<>'):
            h.write('L_'+str(i+1)+': '+'if ('+listQuads[i][2]+'!='+listQuads[i][3]+') goto L_'+str(listQuads[i][4])+';\n\t')
        elif (listQuads[i][1] == ':='):
            h.write('L_' + str(i + 1) + ': ' + listQuads[i][4] + '= ' + listQuads[i][2] + ';\n\t ')
        elif (listQuads[i][1] == 'jump'):
            h.write('L_' + str(i + 1) + ': ' + 'goto L_' +str(listQuads[i][4]) + '; \n\t')
        elif (listQuads[i][1] == 'begin_block'):
            h.write('L_' + str(i + 1) + ': \n\t')
        elif (listQuads[i][1] == 'out'):
            h.write('L_'+str(i+1)+': '+'printf (\"' + listQuads[i][2]+'= %d\', '+listQuads[i][2]+');\n\t')
        elif (listQuads[i][1] == 'halt'):
            h.write('L_' + str(i + 1) + ': {}\n\t')

    h.write('\n}')
    h.close()

syntax_an()
createIntFile()
createCfile()
















