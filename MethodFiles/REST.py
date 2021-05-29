import requests, openpyxl,json, re, traceback, logging

def readexcel(Excel_Location, Excel_Sheet_Name, Module_Name):
    data = {}
    print("Opening Excel")
    try:
        Excel_WorkBook = openpyxl.load_workbook(Excel_Location)
        print("Opened Excel")
    except Exception as error:
        print("Error in opening API Excel File")
        traceback.print_stack()

    try:
        for SheetName in Excel_WorkBook.worksheets:
            if SheetName.title == Excel_Sheet_Name:
                ActiveWorkSheet = Excel_WorkBook[SheetName.title]
                print("Title of Sheet = " + ActiveWorkSheet.title)
                RowLength = SheetName.max_row
                ColumnLength = SheetName.max_column
                for i in range(1, RowLength + 1):
                    RowContents = SheetName.cell(row=i, column=1)
                    print("Row " + str(RowContents.row) + " = " + str(RowContents.value))
                    if ((RowContents.value) == Module_Name):
                        print("Module Found : " + str(RowContents.value) + " in Row - " + str(
                            RowContents.row) + " of Worksheet - " + ActiveWorkSheet.title)
                    else:
                        continue

                    for j in range(1, ColumnLength + 1):
                        Response = dict()
                        ColumnContents = SheetName.cell(row=RowContents.row, column=j)
                        print(ColumnContents.value, end="" + "\n")

                        try:
                            API_Name = (SheetName["A" + str(RowContents.row)])
                            print(API_Name.value)
                            data['API'] = str(API_Name.value)
                            print(data['API'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            HTTP_Method = (SheetName["B" + str(RowContents.row)])
                            print(HTTP_Method.value)
                            data['HTTPMethod'] = str(HTTP_Method.value)
                            print(data['HTTPMethod'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Request_Protocol = (SheetName["C" + str(RowContents.row)])
                            print(Request_Protocol.value)
                            data['Protocol'] = str(Request_Protocol.value)
                            print(data['Protocol'] + "\n")
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Request_BaseURL = (SheetName["D" + str(RowContents.row)])
                            print("BaseURL = " + str(Request_BaseURL.value) + "\n")
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Request_RelativeURL = (SheetName["E" + str(RowContents.row)])
                            print("RelativeURL = " + str(Request_RelativeURL.value) + "\n")
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            data['URL'] = str(data['Protocol']) + "://" + str(Request_BaseURL.value) + str(Request_RelativeURL.value)
                            print(data['URL'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Body_Row = (SheetName["F" + str(RowContents.row)])
                            Body_Content = str(Body_Row.value)
                            print("Body = " + Body_Content + "\n")
                            data['Body'] = json.loads(Body_Content)
                            print(data['Body'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Header_Row = (SheetName["G" + str(RowContents.row)])
                            Header_Content = str(Header_Row.value)
                            print("Header = " + Header_Content + "\n")
                            data['Header'] = json.loads(Header_Content)
                            print(data['Header'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Cookie_Row = (SheetName["H" + str(RowContents.row)])
                            Cookie_Content = str(Cookie_Row.value)
                            print("Cookie = " + Cookie_Content + "\n")
                            data['Cookie'] = json.loads(Cookie_Content)
                            print(data['Cookie'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break
                        break
                    break
                    print(data)
                    Excel_WorkBook.close()

    except:
        print("Error in reading contents")
    return data


