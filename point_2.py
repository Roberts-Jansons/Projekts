from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook, load_workbook
import time


def get_word_definition(word):
    driver = webdriver.Chrome()  # Make sure to use the appropriate driver for your browser

    try:
        #word=word.replace(" ","-")
        links=["https://www.oxfordlearnersdictionaries.com/definition/english/","https://www.dictionary.com/browse/"]
        i=0
        global a
        a=0
        not_found_defintion=True
        
        while not_found_defintion==True:
            link=links[i]+word
            driver.get(link)
            
            # Find the search input field and enter the word
            #search_box = driver.find_element("id", "q")
            #search_box.clear()
            #search_box.send_keys(word)
            #search_box.send_keys(Keys.RETURN)

            # Find the definition element and retrieve its text

            if i==0:
                try:
                    content = driver.find_element("class name", 'results')
                    a+=1
                    i+=1
                except:
                    definition_element = driver.find_element("class name", "def")
                    definition = definition_element.text
                    print("==============================",definition)
                    not_found_defintion=False   
                    return definition
        
            elif i==1:
                try:
                    content_other = driver.find_element("class name", 'E17D6zMGNMyhZ9DoRo9R')
                    a+=1
                    not_found_defintion=False
                except:
                    definition_element = driver.find_element("class name", "ESah86zaufmd2_YPdZtq")
                    definition = definition_element.text
                    not_found_defintion=False   
                    return definition

    finally:
        # Close the browser window
        driver.quit()

words_to_search=["unedited"]
def manually():
    words_to_search.clear()
    print("Ieraksti stop, lai beigtu.")
    while True:
        adding_word=input()
        if adding_word=="stop":
            break
        words_to_search.append(adding_word)
        
        

def upload():
    words_to_search.clear()
    file=input("What file needs to be opened?: ")

    #f = open(file, "r")
    #print(f.readline())
    #for x in f:
    #  print(x)

    print("Opening file")
    file="manually_testam.xlsx"

    wb=load_workbook(file)
    ws=wb.active
    max_row=ws.max_row
    s=[]
    #start=3
    #start=54 (preformance bonus)
    start=55
    for row in range(start,max_row+1):
        definition=(ws['C' + str(row)].value)
        if type(definition) is None:
            break
        words_to_search.append(definition)
        
    

   
def main():
    #choice=input("Kāda veidā gribi atrast vārdu definīcjas? Ja manuāli, ievadi input, bet, ja caur dokumentu - upload. ")
    choice=input("if want to write manually ievadi input, but, if want to use file - upload. ")
    #words_to_search=["unedited"]

    # working
    # words_to_search = ["transistor", "remote access", "integrated circuit", "semiconductor", "lattice", "collector", "source", "junction", "memory"]
    #words_to_search = ["optical memory", "flash memory", "marginal", "ferrous", "element", "compund", "mixtures", "nepetism", "salary", "wage", "employee benefits", "commission", "royalty", "performance bonus", "stock options", "system software", "operating system", "application programs", "booting", "user interface", "managing programs", "managinng memory", "coordinating taks", "configuring devices", "monitoring preformance", "file managment", "administering security", "controling network", "BIOS", "POST"]  # Add more words as needed

    if choice=="input" or choice=="upload":
        if choice=="input":
            print("manuāls teksts")
            manually()
        elif choice=="upload":
            print("no dokumenta")
            upload()


            #words_to_search=['System Software']

        #wb=load_workbook('manually.xlsx')
        #ws=wb.active
        #for row in range(22, 41):
        #    term=ws['C' + str(row)].value
        #    #words_to_search.append(term)     
        #wb.close()

        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        print("JĀNOLASA ŠĀDAS DEFINĪCIJAS:")
        print(words_to_search)
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")

       

    
        # Create a new Excel workbook and add a worksheet
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = "Word Definitions"

        # Add headers to the worksheet
        worksheet.append(["Word", "Definition","L"])

        words_and_definitions=[]
        
        for word in words_to_search:
            #print("Word=",word)
            word=word.replace(" ","-")
            #print("Word=",word)
            definition = get_word_definition(word)
            #if definition is None:
                #print(word," nav definīcijas")
            
            # Add word and definition to the worksheet
            worksheet.append([word, definition])
            
            #workbook.save("word_definitions.xlsx")
            
            #print(definition, "     ", word)
            print(word,"---",definition, a)
            #print(word,"---",definition,", definition type is ",type(definition))
        
        # Save the workbook to a file
        #workbook.save("word_definitions.xlsx")

        #time.sleep(5.5)
        #wb=load_workbook('word_definitions.xlsx')
        #ws=wb.active
        #max_row=ws.max_row
        #for row in range(2,max_row+1):
        #    defintion=(ws['B' + str(row)].value)
        #    if definition is str and defintion=="NoneType":      
        #        a=(ws['a' + str(row)].value)
        #        print(a," nav definīcijas")


    else:
        print("Incorrect input")

    
if __name__ == "__main__":
    main()
