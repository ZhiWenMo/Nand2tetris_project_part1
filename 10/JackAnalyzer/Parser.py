from Tokenizer import JackTokenizer, mark_up_symbol
from Tokenizer import KEYWORD, SYMBOL, IDENTIFIER, INT_CONST, STRING_CONST


class CompilationEngine:
    def __init__(self, input_file_path, output_file_path):
        """Creates a new compilation engine with the given input and output.
        """
        self.jacktokenizer = JackTokenizer(input_file_path)
        self.writer = open(output_file_path, "w")
        self.jacktokenizer.hasMoreTokens()

    def compile(self):
        self.CompileClass()

    def CompileClass(self):
        self.writer.write("<class>\n")
        self.writer.write("\t" + "<keyword>" +
                          self.jacktokenizer.keyWord() + "</keyword>\n")
        self.jacktokenizer.hasMoreTokens()
        self.writer.write("\t" + "<identifier>" +
                          self.jacktokenizer.identifier() + "</identifier>\n")
        self.jacktokenizer.hasMoreTokens()
        self.writer.write(
            "\t" + "<symbol>" + mark_up_symbol(self.jacktokenizer.symbol()) + "</symbol>\n")
        self.jacktokenizer.hasMoreTokens()
        # enter classVarDec
        while self.jacktokenizer._current_token in ["static", "field"]:
            self.CompileClassVarDec()
        # enter subroutineDec
        while self.jacktokenizer._current_token in ["constructor", "function", "method"]:
            self.CompileSubroutine()
        self.writer.write(
            "\t" + "<symbol>" + mark_up_symbol(self.jacktokenizer.symbol()) + "</symbol>\n")
        self.writer.write("</class>\n")

    def CompileClassVarDec(self):
        if self.jacktokenizer._current_token not in ["static", "field"]:
            return
        else:
            self.writer.write("\t<classVarDec>\n")
            self.writer.write("\t\t"+"<keyword> " +
                              self.jacktokenizer.keyWord() + " </keyword>\n")
            self.jacktokenizer.hasMoreTokens()
            if self.jacktokenizer.tokenType() is KEYWORD:
                self.writer.write("\t\t"+"<keyword> " +
                                  self.jacktokenizer.keyWord() + " </keyword>\n")
            else:
                self.writer.write(
                    "\t\t"+"<identifier> " + self.jacktokenizer.identifier() + " </identifier>\n")
            self.jacktokenizer.hasMoreTokens()
            self.writer.write(
                "\t\t"+"<identifier> " + self.jacktokenizer.identifier() + " </identifier>\n")
            self.jacktokenizer.hasMoreTokens()

            # enter (',', varName)*
            while self.jacktokenizer.symbol() == ",":
                self.writer.write("\t\t" + "<symbol> " +
                                  self.jacktokenizer.symbol() + " </symbol>\n")
                self.jacktokenizer.hasMoreTokens()
                self.writer.write(
                    "\t\t"+"<identifier> " + self.jacktokenizer.identifier() + " </identifier>\n")
                self.jacktokenizer.hasMoreTokens()

            self.writer.write("\t\t" + "<symbol> " +
                              self.jacktokenizer.symbol() + " </symbol>\n")

            self.jacktokenizer.hasMoreTokens()

            self.writer.write("\t</classVarDec>\n")

    def CompileSubroutine(self):
        if self.jacktokenizer._current_token not in ["constructor", "function", "method"]:
            return
        else:
            self.writer.write("\t" + "<subroutineDec>\n")
            self.writer.write("\t\t" + "<keyword>" +
                              self.jacktokenizer.keyWord() + "</keyword>\n")

            self.jacktokenizer.hasMoreTokens()

            if self.jacktokenizer.tokenType() is KEYWORD:
                self.writer.write("\t\t" + "<keyword>" +
                                  self.jacktokenizer.keyWord() + "</keyword>\n")
            else:
                self.writer.write(
                    "\t\t"+"<identifier> " + self.jacktokenizer.identifier() + " </identifier>\n")

            self.jacktokenizer.hasMoreTokens()
            self.writer.write(
                "\t\t"+"<identifier> " + self.jacktokenizer.identifier() + " </identifier>\n")

            self.jacktokenizer.hasMoreTokens()
            self.writer.write("\t\t"+"<symbol> " +
                              self.jacktokenizer.symbol() + " </symbol>\n")

            # enter param list

            self.jacktokenizer.hasMoreTokens()
            self.CompileParameterList()

            self.writer.write("\t\t"+"<symbol> " +
                              self.jacktokenizer.symbol() + " </symbol>\n")

            # enter subroutineBody

            self.jacktokenizer.hasMoreTokens()
            self.writer.write("\t\t"+"<subroutineBody>\n")
            self.writer.write("\t\t"+"<symbol> " +
                              self.jacktokenizer.symbol() + " </symbol>\n")

            # varDec*
            self.jacktokenizer.hasMoreTokens()
            while self.jacktokenizer.keyWord() == "var":
                self.CompileVarDec()

            # statements
            self.CompileStatements()

            self.writer.write("\t\t"+"<symbol> " +
                              self.jacktokenizer.symbol() + " </symbol>\n")
            self.writer.write("\t\t"+"</subroutineBody>\n")

            self.writer.write("\t" + "</subroutineDec>\n")

            self.jacktokenizer.hasMoreTokens()

    def CompileParameterList(self):
        if self.jacktokenizer.tokenType() is SYMBOL:
            self.writer.write("\t\t"+"<parameterList>\n")
            self.writer.write("\t\t"+"</parameterList>\n")
            return

        self.writer.write("\t\t"+"<parameterList>\n")
        # type
        if self.jacktokenizer.tokenType() is KEYWORD:
            self.writer.write("\t\t\t"+"<keyword>" +
                              self.jacktokenizer.keyWord() + "</keyword>\n")
        else:
            self.writer.write("\t\t\t"+"<identifier>" +
                              self.jacktokenizer.identifier() + "</identifier>\n")

        self.jacktokenizer.hasMoreTokens()
        self.writer.write("\t\t\t"+"<identifier>" +
                          self.jacktokenizer.identifier() + "</identifier>\n")

        self.jacktokenizer.hasMoreTokens()

        while self.jacktokenizer.symbol() == ",":
            self.writer.write("\t\t\t"+"<symbol> " +
                              self.jacktokenizer.symbol() + " </symbol>\n")
            self.jacktokenizer.hasMoreTokens()

            if self.jacktokenizer.tokenType() is KEYWORD:
                self.writer.write("\t\t\t"+"<keyword>" +
                                  self.jacktokenizer.keyWord() + "</keyword>\n")
            else:
                self.writer.write(
                    "\t\t\t"+"<identifier>" + self.jacktokenizer.identifier() + "</identifier>\n")

            self.jacktokenizer.hasMoreTokens()
            self.writer.write("\t\t\t"+"<identifier>" +
                              self.jacktokenizer.identifier() + "</identifier>\n")

            self.jacktokenizer.hasMoreTokens()

        self.writer.write("\t\t"+"</parameterList>\n")

    def CompileVarDec(self):
        self.writer.write("\t"+"<varDec>\n")
        self.writer.write("\t\t"+"<keyword>" +
                          self.jacktokenizer.keyWord()+"</keyword>\n")
        self.jacktokenizer.hasMoreTokens()
        if self.jacktokenizer.tokenType() is KEYWORD:
            self.writer.write("\t\t"+"<keyword>" +
                              self.jacktokenizer.keyWord() + "</keyword>\n")
        else:
            self.writer.write("\t\t"+"<identifier>" +
                              self.jacktokenizer.identifier() + "</identifier>\n")

        self.jacktokenizer.hasMoreTokens()
        self.writer.write("\t\t"+"<identifier>" +
                          self.jacktokenizer.identifier() + "</identifier>\n")

        self.jacktokenizer.hasMoreTokens()
        while self.jacktokenizer.symbol() == ",":
            self.writer.write("\t\t"+"<symbol>" +
                              self.jacktokenizer.symbol() + "</symbol>\n")
            self.jacktokenizer.hasMoreTokens()
            self.writer.write("\t\t"+"<identifier>" +
                              self.jacktokenizer.identifier() + "</identifier>\n")
            self.jacktokenizer.hasMoreTokens()

        self.writer.write("\t\t"+"<symbol>" +
                          self.jacktokenizer.symbol() + "</symbol>\n")

        self.writer.write("\t"+"</varDec>\n")
        self.jacktokenizer.hasMoreTokens()

    def CompileStatements(self):
        self.writer.write("\t"+"<statements>\n")
        while self.jacktokenizer.keyWord() in ["let", "if", "while", "do", "return"]:
            if self.jacktokenizer.keyWord() == "let":
                self.CompileLet()

            if self.jacktokenizer.keyWord() == "if":
                self.CompileIf()

            if self.jacktokenizer.keyWord() == "while":
                self.CompileWhile()

            if self.jacktokenizer.keyWord() == "do":
                self.CompileDo()

            if self.jacktokenizer.keyWord() == "return":
                self.CompileReturn()

        self.writer.write("\t"+"</statements>\n")

    def CompileDo(self):
        self.writer.write("\t\t"+"<doStatement>\n")
        self.writer.write("\t\t\t" + "<keyword>" +
                          self.jacktokenizer.keyWord() + "</keyword>" + "\n")
        # subroutineCall
        self.jacktokenizer.hasMoreTokens()
        self.writer.write("\t\t\t" + "<identifier>" +
                          self.jacktokenizer.identifier() + "</identifier>" + "\n")

        self.jacktokenizer.hasMoreTokens()
        if self.jacktokenizer.symbol() == ".":
            self.writer.write("\t\t\t" + "<symbol>" +
                              self.jacktokenizer.symbol() + "</symbol>" + "\n")
            self.jacktokenizer.hasMoreTokens()
            self.writer.write("\t\t\t" + "<identifier>" +
                              self.jacktokenizer.identifier() + "</identifier>" + "\n")
            self.jacktokenizer.hasMoreTokens()
            self.writer.write("\t\t\t" + "<symbol>" +
                              self.jacktokenizer.symbol() + "</symbol>" + "\n")
            self.jacktokenizer.hasMoreTokens()
            self.CompileExpressionList()
            self.writer.write("\t\t\t" + "<symbol>" +
                              self.jacktokenizer.symbol() + "</symbol>" + "\n")

        else:
            self.writer.write("\t\t\t" + "<symbol>" +
                              self.jacktokenizer.symbol() + "</symbol>" + "\n")
            self.jacktokenizer.hasMoreTokens()
            self.CompileExpressionList()
            self.writer.write("\t\t\t" + "<symbol>" +
                              self.jacktokenizer.symbol() + "</symbol>" + "\n")

        self.jacktokenizer.hasMoreTokens()
        self.writer.write("\t\t\t" + "<symbol>" +
                          self.jacktokenizer.symbol() + "</symbol>" + "\n")

        self.jacktokenizer.hasMoreTokens()
        self.writer.write("\t\t"+"</doStatement>\n")

    def CompileLet(self):
        self.writer.write("\t\t"+"<letStatement>\n")
        self.writer.write("\t\t\t" + "<keyword>" +
                          self.jacktokenizer.keyWord() + "</keyword>" + "\n")
        self.jacktokenizer.hasMoreTokens()
        self.writer.write("\t\t\t" + "<identifier>" +
                          self.jacktokenizer.identifier() + "</identifier>" + "\n")
        self.jacktokenizer.hasMoreTokens()
        # handle index
        if self.jacktokenizer.symbol() == "[":
            self.writer.write("\t\t\t" + "<symbol>" +
                              self.jacktokenizer.symbol() + "</symbol>" + "\n")
            self.jacktokenizer.hasMoreTokens()
            self.CompileExpression()
            self.writer.write("\t\t\t" + "<symbol>" +
                              self.jacktokenizer.symbol() + "</symbol>" + "\n")
            self.jacktokenizer.hasMoreTokens()

        self.writer.write("\t\t\t" + "<symbol>" +
                          self.jacktokenizer.symbol() + "</symbol>" + "\n")

        self.jacktokenizer.hasMoreTokens()
        self.CompileExpression()
        self.writer.write("\t\t\t" + "<symbol>" +
                          self.jacktokenizer.symbol() + "</symbol>" + "\n")
        self.jacktokenizer.hasMoreTokens()

        self.writer.write("\t\t"+"</letStatement>\n")

    def CompileWhile(self):
        self.writer.write("\t\t"+"<whileStatement>\n")
        self.writer.write("\t\t\t" + "<keyword>" +
                          self.jacktokenizer.keyWord() + "</keyword>" + "\n")
        self.jacktokenizer.hasMoreTokens()
        self.writer.write("\t\t\t" + "<symbol>" +
                          self.jacktokenizer.symbol() + "</symbol>" + "\n")
        self.jacktokenizer.hasMoreTokens()
        self.CompileExpression()
        self.writer.write("\t\t\t" + "<symbol>" +
                          self.jacktokenizer.symbol() + "</symbol>" + "\n")
        self.jacktokenizer.hasMoreTokens()
        self.writer.write("\t\t\t" + "<symbol>" +
                          self.jacktokenizer.symbol() + "</symbol>" + "\n")
        self.jacktokenizer.hasMoreTokens()
        self.CompileStatements()
        self.writer.write("\t\t\t" + "<symbol>" +
                          self.jacktokenizer.symbol() + "</symbol>" + "\n")
        self.jacktokenizer.hasMoreTokens()
        self.writer.write("\t\t"+"</whileStatement>\n")

    def CompileReturn(self):
        self.writer.write("\t\t"+"<returnStatement>\n")
        self.writer.write("\t\t\t" + "<keyword>" +
                          self.jacktokenizer.keyWord() + "</keyword>" + "\n")

        # expression?
        self.jacktokenizer.hasMoreTokens()
        if self.jacktokenizer.tokenType() in [INT_CONST, STRING_CONST, IDENTIFIER] or self.jacktokenizer.keyWord() in ["true", "false", "null", "this"] or self.jacktokenizer.symbol() in ["(", "-", "~"]:
            self.CompileExpression()

        self.writer.write("\t\t\t" + "<symbol>" +
                          self.jacktokenizer.symbol() + "</symbol>" + "\n")
        self.jacktokenizer.hasMoreTokens()

        self.writer.write("\t\t"+"</returnStatement>\n")

    def CompileIf(self):
        self.writer.write("\t\t"+"<ifStatement>\n")
        self.writer.write("\t\t\t" + "<keyword>" +
                          self.jacktokenizer.keyWord() + "</keyword>" + "\n")

        self.jacktokenizer.hasMoreTokens()
        self.writer.write("\t\t\t" + "<symbol>" +
                          self.jacktokenizer.symbol() + "</symbol>" + "\n")

        self.jacktokenizer.hasMoreTokens()
        self.CompileExpression()

        self.writer.write("\t\t\t" + "<symbol>" +
                          self.jacktokenizer.symbol() + "</symbol>" + "\n")

        # '{' statements '}'
        self.jacktokenizer.hasMoreTokens()
        self.writer.write("\t\t\t" + "<symbol>" +
                          self.jacktokenizer.symbol() + "</symbol>" + "\n")
        self.jacktokenizer.hasMoreTokens()
        self.CompileStatements()
        self.writer.write("\t\t\t" + "<symbol>" +
                          self.jacktokenizer.symbol() + "</symbol>" + "\n")

        # ('else' '{' statements '}')?
        self.jacktokenizer.hasMoreTokens()

        if self.jacktokenizer.keyWord() == 'else':
            self.writer.write("\t\t\t" + "<keyword>" +
                              self.jacktokenizer.keyWord() + "</keyword>" + "\n")
            self.jacktokenizer.hasMoreTokens()
            self.writer.write("\t\t\t" + "<symbol>" +
                              self.jacktokenizer.symbol() + "</symbol>" + "\n")
            self.jacktokenizer.hasMoreTokens()
            self.CompileStatements()
            self.writer.write("\t\t\t" + "<symbol>" +
                              self.jacktokenizer.symbol() + "</symbol>" + "\n")
            self.jacktokenizer.hasMoreTokens()

        self.writer.write("\t\t"+"</ifStatement>\n")

    def CompileExpression(self):
        op = ["+", "-", "*", "/", "&", "|", "<", ">", "="]
        self.writer.write("\t\t"+"<expression>\n")

        self.CompileTerm()

        while self.jacktokenizer._current_token in op:
            self.writer.write("\t\t\t\t" + "<symbol>" +
                              mark_up_symbol(self.jacktokenizer.symbol()) + "</symbol>"+"\n")
            self.jacktokenizer.hasMoreTokens()
            self.CompileTerm()

        self.writer.write("\t\t"+"</expression>\n")

    def CompileTerm(self):
        self.writer.write("\t\t\t"+"<term>\n")

        # LL(2)
        if self.jacktokenizer.tokenType() is IDENTIFIER:
            last_indentifier = self.jacktokenizer.identifier()
            self.jacktokenizer.hasMoreTokens()

            if self.jacktokenizer.symbol() == "[":
                self.writer.write("\t\t\t\t" + "<identifier>" +
                                  last_indentifier + "</identifier>" + "\n")
                self.writer.write("\t\t\t\t" + "<symbol>" +
                                  self.jacktokenizer.symbol() + "</symbol>" + "\n")
                self.jacktokenizer.hasMoreTokens()
                self.CompileExpression()
                self.writer.write("\t\t\t\t" + "<symbol>" +
                                  self.jacktokenizer.symbol() + "</symbol>" + "\n")
            elif self.jacktokenizer.symbol() == ".":
                self.writer.write("\t\t\t\t" + "<identifier>" +
                                  last_indentifier + "</identifier>" + "\n")
                self.writer.write("\t\t\t" + "<symbol>" +
                                  self.jacktokenizer.symbol() + "</symbol>" + "\n")
                self.jacktokenizer.hasMoreTokens()
                self.writer.write("\t\t\t" + "<identifier>" +
                                  self.jacktokenizer.identifier() + "</identifier>" + "\n")
                self.jacktokenizer.hasMoreTokens()
                self.writer.write("\t\t\t" + "<symbol>" +
                                  self.jacktokenizer.symbol() + "</symbol>" + "\n")
                self.jacktokenizer.hasMoreTokens()
                self.CompileExpressionList()
                self.writer.write("\t\t\t" + "<symbol>" +
                                  self.jacktokenizer.symbol() + "</symbol>" + "\n")

            elif self.jacktokenizer.symbol() == "(":
                self.writer.write("\t\t\t\t" + "<identifier>" +
                                  last_indentifier + "</identifier>" + "\n")
                self.writer.write("\t\t\t" + "<symbol>" +
                                  self.jacktokenizer.symbol() + "</symbol>" + "\n")
                self.jacktokenizer.hasMoreTokens()
                self.CompileExpressionList()
                self.writer.write("\t\t\t" + "<symbol>" +
                                  self.jacktokenizer.symbol() + "</symbol>" + "\n")
            else:
                self.writer.write("\t\t\t\t" + "<identifier>" +
                                  last_indentifier + "</identifier>" + "\n")

                self.writer.write("\t\t\t"+"</term>\n")
                return

        # '(' expression ')'
        if self.jacktokenizer.symbol() == "(":
            self.writer.write("\t\t\t\t" + "<symbol>" +
                              self.jacktokenizer.symbol() + "</symbol>" + "\n")
            self.jacktokenizer.hasMoreTokens()
            self.CompileExpression()
            self.writer.write("\t\t\t\t" + "<symbol>" +
                              self.jacktokenizer.symbol() + "</symbol>" + "\n")

        # integerConstant
        if self.jacktokenizer.tokenType() is INT_CONST:
            self.writer.write("\t\t\t\t" + "<integerConstant>" +
                              self.jacktokenizer.intVal() + "</integerConstant>"+"\n")

        # stringConstant
        if self.jacktokenizer.tokenType() is STRING_CONST:
            self.writer.write("\t\t\t\t" + "<stringConstant>" +
                              self.jacktokenizer.stringVal() + "</stringConstant>"+"\n")

        # keywordConstant
        if self.jacktokenizer.keyWord() in ["true", "false", "null", "this"]:
            self.writer.write("\t\t\t\t" + "<keyword>" +
                              self.jacktokenizer.keyWord() + "</keyword>"+"\n")

        # UnaryOp term
        if self.jacktokenizer.symbol() in ["-", "~"]:
            self.writer.write("\t\t\t\t" + "<symbol>" +
                              self.jacktokenizer.symbol() + "</symbol>"+"\n")
            self.jacktokenizer.hasMoreTokens()
            self.CompileTerm()
            self.writer.write("\t\t\t"+"</term>\n")
            return

        self.writer.write("\t\t\t"+"</term>\n")

        self.jacktokenizer.hasMoreTokens()

    def CompileExpressionList(self):
        self.writer.write("\t\t\t"+"<expressionList>\n")
        if self.jacktokenizer.tokenType() in [INT_CONST, STRING_CONST, IDENTIFIER] or self.jacktokenizer.keyWord() in ["true", "false", "null", "this"] or self.jacktokenizer.symbol() in ["(", "-", "~"]:
            self.CompileExpression()

        while self.jacktokenizer._current_token == ",":
            self.writer.write("\t\t\t\t" + "<symbol>" +
                              self.jacktokenizer.symbol() + "</symbol>"+"\n")
            self.jacktokenizer.hasMoreTokens()
            self.CompileExpression()

        self.writer.write("\t\t\t"+"</expressionList>\n")
