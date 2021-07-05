import re 

class injectionCondition:
    mysql_keyword = [r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"MySQL Query fail.*", r"SQL syntax.*MariaDB server"]
    postgre_keyword = [r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"Warning.*PostgreSQL"]
    microsoft_sql_server_keyword = [r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*odbc_.*", r"Warning.*mssql_", r"Msg \d+, Level \d+, State \d+", r"Unclosed quotation mark after the character string", r"Microsoft OLE DB Provider for ODBC Drivers"]
    microsoft_access_keyword = [r"Microsoft Access Driver", r"Access Database Engine", r"Microsoft JET Database Engine", r".*Syntax error.*query expression"]
    oracle_keyword = [r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Warning.*oci_.*", "Microsoft OLE DB Provider for Oracle"]
    idm_db2_keyword = [r"CLI Driver.*DB2", r"DB2 SQL error"]
    sqlite_keyword = [r"SQLite/JDBCDriver"]
    keyword_internal_server_error = "Internal Server Error"
    keyword_injection_hint = "select"
    keyword_hint=["show "," top "," distinct "," from "," from dual"," where "," group by "," order by "," having "," limit "," offset "," union all "," rownum as ","(case "]
    def __init__(self):
        self.check_body=""
        self.after_hit=""
        self.original_response=""
        #self.after_hit_res=""
        self.flag=0
        self.check_done=0
        self.category=""
        self.response_time=0.0
        self.original_response_time=0.0
#================================ Error statements in response ===================================    
    def check_for_statement(self):
        self.check_done=1
        try:
            if self.check_body.index(self.keyword_injection_hint):
                print("Vulnerable")
                self.flag=self.flag+1
                search_sql_query = self.check_body.index(self.keyword_injection_hint)
                print("ket's gp")
                print(search_sql_query)
                if(search_sql_query):
                    index1 =search_sql_query
                    index2 = search_sql_query+35
                    print(self.check_body[index1:index2])
            elif (x for x in self.mysql_keyword if(x in self.check_body)):
                print("Maybe vulnerable to injection")
                print(self.mysql_keyword)
                print(self.check_body[x.index():x.index()+35])
                self.flag=self.flag+1
                #raise Exception
            elif (x for x in self.postgre_keyword if(x in elf.check_body)):
                print("Maybe vulnerable to injection")
                print(self.check_body[x.index():x.index()+35])
                self.flag=self.flag+1
            elif (x for x in self.microsoft_sql_server_keyword if(x in elf.check_body)):
                print("Maybe vulnerable to injection")
                print(self.check_body[x.index():x.index()+35])
                self.flag=self.flag+1
            elif (x for x in self.microsoft_access_keyword if(x in elf.check_body)):
                print("Maybe vulnerable to injection")
                self.flag=self.flag+1
                print(self.check_body[x.index():x.index()+35])
            elif (x for x in self.oracle_keyword if(x in elf.check_body)):
                print("Maybe vulnerable to injection")
                self.flag=self.flag+1
                print(self.check_body[x.index():x.index()+35])
            elif (x for x in self.idm_db2_keyword if(x in elf.check_body)):
                print("Maybe vulnerable to injection")
                self.flag=self.flag+1
                print(self.check_body[x.index():x.index()+35])
            elif (x for x in self.sqlite_keyword if(x in elf.check_body)):
                print("Maybe vulnerable to injection")
                print(self.check_body[x.index():x.index()+35])
                self.flag=self.flag+1
            else:
                print("No statements")
        except:
            print("error")    
# ================================================= Error based ==========================================
    def error_check(self):
        self.check_done=0
    #================================== API didn't respond to injection =============================================
        self.check_body=self.check_body.lower()
        if self.after_hit.status_code == 200:
            print("The functionality didn't respond")
            self.flag=self.flag+1
            try:
                self.check_for_statement()
                if self.flag > 1:
                    return 1
                        #raise ("Sql Query spoted")
                else:
                    print("Couldn't snif")
                        #return 1
            except Exception as error:
                print("No query")
            print("Outta here")
            #return 1
        else:
            print("The functionality respond")

# --------------------------------------- Check common error messages ------------------------------------------------    
        if self.check_done != 1:
            self.check_for_statement()

#================================== Internal server Error =============================================
        print("Or here")
        search_server_error = re.search(self.keyword_internal_server_error,self.check_body)
        if self.after_hit.status_code == 500:
            print("SQL Injection found")
            self.flag=self.flag+1
            #raise ApiError('GET /tasks/ {}'.format(after_hit.status_code))
        else:
            print("Your status code" + str(self.after_hit.status_code))
            if (search_server_error):
                print("SQL Injection found")
                self.flag=self.flag+1
            else :
                print("Safe from this use case")
    
 #================================== Loading blank page =============================================   
        print("or it is here")
        print(self.original_response)
        if self.original_response['ResponseBody'] and self.original_response['ResponseBody'] != ' ' and self.original_response['ResponseBody'] != '{}':
            if (not self.check_body) or (self.check_body == ' ') :
                print("A blank page loaded")
                self.flag=self.flag+1
        elif (not self.original_response['ResponseBody']) or (self.original_response['ResponseBody'] == ' ') or (self.original_response['ResponseBody'] == '{}') :
            print("The original was blank itself")
       

        print(self.flag)
#============================================= TIME CHECK=========================================
    def time_check(self):
        print("original response")
        print(self.original_response_time)
        print("After hit response")
        print(self.response_time)

#==================================== Category wise check =======================================
    def check_for_errors(self):
        if self.category == "Time":
            self.time_check()
        else:
            self.error_check()

        
'''

if __name__ =="__main__":
    object2=injectionCondition()
    object2.check_for_errors()
 if self.original_response['ResponseHeader'] != self.after_hit_res['ResponseHeader']:
            contains_digit = any(map(str.isdigit, self.after_hit_res['ResponseHeader']))
            print("Type is")
            print(type(self.after_hit_res['ResponseHeader']))
            if contains_digit:
                print("digit is")
                print(contains_digit)
                self.flag=1
                print("Headers are different have a look")
                print(self.after_hit_res['ResponseHeader'])
                return 1
'''