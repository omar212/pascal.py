# Brian Wu
# Pascal Compiler written in Python
# brianwu02@gmail.com

"""List of Tokens
RESERVERED_WORDS:
    

IDENTIFIERS:

OPERATORS:
    arithmetic: + - * / Div Mod
    logical: not and or xor shl shr << >>
    boolean: not and or xor
    string: 
    set: 
        + : Union
        - : Difference
        >< : Symmetric Difference
        <= : contains
        include : include an element in the set
        exclude : exclude an element from the set
        in: check whether an element is in the set
    relational:
        = : equal
        <> : Not Equal
        < : strictly less than
        > : strictly greater than
        <= : less than or equal
        >= : greater than or equal
        in : Element of

    class:

seperators: white_space, new_line
constants: float, integer, literal


Literals:
    Integer (TK_INTLIT, value)
    Real (TK_REALLIT, index -> real table)
    Chars (TK_INTLIB | TK_CHARLIT, index -> string table)
    Strings (TK_STRLIT, index -> string table)

Keywords (individual type, --)
Identifiers (TK_ID, --, curname)
EOL? EOF? (TK_EOF, --)

TOKEN:
    int curtoken;
    int curtokenvalue;
    string curname;
    curfile;
    curline;
    curcol;

(TK_ID, --, curvalue) where -- is TK_A_VAR, index -> symtable

use LL parser style.
"""

class Token:
    """ A token object"""
    def __init__(self, tk_val, tk_type, line_num, line_index, state, name):
        """all tokens must have these values"""
        
        self.tk_value = tk_val
        self.tk_type = tk_type
        self.line_number = line_num
        self.line_index = line_index
        self.creation_state = state
        self.name = name

    def get_type(self):
        """returns the type of token"""
        return self.tk_type

    def get_value(self):
        """returns the value of the token"""
        return self.tk_value

    def get_name(self):
        """returns the current name of the token"""
        return self.name

    def get_current_file(self):
        """returns the current file the token is in.
        does not make sense yet. multiple files i guess?"""
        return str(self.current_file)

    def get_line_number(self):
        """returns the line of the token"""
        return self.line_number

    def get_line_index(self):
        """returns the index with respect to line"""
        return self.line_index

    def get_creation_state(self):
        return self.creation_state

    def is_unary_operator(self):
        """ UnaryOperator --> '+' | '-' """
        accepted = ['+', '-']
        if self.tk_value in accepted:
            return True
        return False

    def is_mult_operator(self):
        """  MultOperator --> '*' | '/' | div | mod | and """
        accepted = ['*', '/', 'div', 'mod', 'and']
        if self.tk_value in accepted:
            return True
        return False

    def is_add_operator(self):
        """  AddOperator --> '+' | '-' | or """
        accepted = ['+', '-', 'or']
        if self.tk_value in accepted:
            return True
        return False

    def is_relation_operator(self):
        """ Relation --> '=' | '<>' | '<' | '>' | '<=' | '>=' | in """
        accepted = ['=', '<>', '<', '>', '<=', '>=', 'in']
        if self.tk_value in accepted:
            return True
        return False

    def is_io_operator(self):
        """ read, readln, write, writeln"""
        accepted = ['TK_READ', 'TK_READLN', 'TK_WRITELN', 'TK_WRITE']
        if self.tk_type in accepted: # fix this later to value? dunno.
            return True
        return False

    def __repr__(self):
        """ prety print the token here. do not need extra dbug info, hurst my eyes"""
        """
        tk_str = "{ TK_TYPE: [%s] TK_VAL: [%s] Line: %s Ind: %s State: %s}" % (
                self.get_type(),
                self.get_value(),
                self.get_line_number(),
                self.get_line_index(),
                self.get_creation_state()
                )
        """

        tk_str = "{TK_TYPE: %s TK_VAL: %s }" % (
                self.get_type(),
                self.get_value()
                )

        return tk_str
