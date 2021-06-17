import re

class injectionCondition:
    mysql_keyword = [r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"MySQL Query fail.*", r"SQL syntax.*MariaDB server"]
    postgre_keyword = [r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"Warning.*PostgreSQL"]
    microsoft_sql_server_keyword = [r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*odbc_.*", r"Warning.*mssql_", r"Msg \d+, Level \d+, State \d+", r"Unclosed quotation mark after the character string", r"Microsoft OLE DB Provider for ODBC Drivers"]
    microsoft_access_keyword = [r"Microsoft Access Driver", r"Access Database Engine", r"Microsoft JET Database Engine", r".*Syntax error.*query expression"]
    oracle_keyword = [r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Warning.*oci_.*", "Microsoft OLE DB Provider for Oracle"]
    idm_db2_keyword = [r"CLI Driver.*DB2", r"DB2 SQL error"]
    sqlite_keyword = [r"SQLite/JDBCDriver"]
    def __init__(self):
        self.after_hit=""
        self.keyword_internal_server_error=""
        self.check_body=""
        self.original_response=""
    
    def check_for_errors(self):
        print("in")
#================================== API didn't respond to injection =============================================
        self.check_body=self.check_body.lower()
        if self.after_hit.status_code == 200:
            print("The functionality didn't respond")
            if any(x in self.check_body for x in keyword_injection_hint):
            #search_sql_query = check_body.index(keyword_injection_hint)
            #if(search_sql_query):
                print("Query found")
                print(self.check_body[x.index():x.index()+35])
            else:
                print(search_sql_query)
        else:
            print("The functionality responded")
    
        if any(x in self.check_body for x in self.mysql_keyword):
            print("Maybe vulnerable to injection")
            print(self.check_body[x.index():x.index()+35])
        elif any(x in self.check_body for x in self.postgre_keyword):
            print("Maybe vulnerable to injection")
            print(self.check_body[x.index():x.index()+35])
        elif any(x in self.check_body for x in self.microsoft_sql_server_keyword):
            print("Maybe vulnerable to injection")
            print(self.check_body[x.index():x.index()+35])
        elif any(x in self.check_body for x in self.microsoft_access_keyword):
            print("Maybe vulnerable to injection")
            print(self.check_body[x.index():x.index()+35])
        elif any(x in self.check_body for x in self.oracle_keyword):
            print("Maybe vulnerable to injection")
            print(self.check_body[x.index():x.index()+35])
        elif any(x in self.check_body for x in self.idm_db2_keyword):
            print("Maybe vulnerable to injection")
            print(self.check_body[x.index():x.index()+35])
        elif any(x in self.check_body for x in self.sqlite_keyword):
            print("Maybe vulnerable to injection")
            print(self.check_body[x.index():x.index()+35])

#================================== Internal server Error =============================================
        search_server_error = re.search(self.keyword_internal_server_error,self.check_body)
        if self.after_hit.status_code == 500:
            print("SQL Injection found")
            #raise ApiError('GET /tasks/ {}'.format(after_hit.status_code))
        else:
            print("Your status code" + str(self.after_hit.status_code))
            if (search_server_error):
                print("SQL Injection found")
            else :
                print("Safe from this use case")
    
 #================================== Loading blank page =============================================   
        if self.original_response['ResponseBody'] and self.original_response['ResponseBody'] != ' ' and self.original_response['ResponseBody'] != '{}':
            if (not self.check_body) or (self.check_body == ' ') :
                print("A blank page loaded")
        elif ( not self.original_response['ResponseBody']) or (self.original_response['ResponseBody'] == ' ') or (self.original_response['ResponseBody'] == '{}') :
            print("The original was blank itself")
