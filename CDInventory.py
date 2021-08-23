#------------------------------------------#
# Title: CDInventory.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# JMagat, 2021-Aug-15, Modified file to use functions
#  moving code from the main loop to the class as functions
#  cd_addition, cd_deletion, write_file and cd_data
# JMagat, 2021-Aug-21, Modified file to add error handling and use of binary data for storage 
#------------------------------------------#

import pickle

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.dat'  # data storage file, previously a txt file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    # TODOne add functions for processing here

    @staticmethod 
    def cd_addition(strID, strTitle, strArtist, table): 

        """Function to manage user input and add to the dictionary list

        Processes user data and formats it into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.
        User data of CD information is collected and added as a row in the dictionary list.
        The table is appended to include the additional row in the dictionary list.

        Args:
            ID (string): this is the CD ID entered by the user
            Title (string): this is the CD's title
            Artist (string): this is the Artist of the CD
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        try:
            intID = int(strID)
            dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
            table.append(dicRow)
        except ValueError as e:
            print('That is not valid CD ID!')
            print('Build in error info:')
            print(type(e), e, e._doc_, sep='\n')
        except Exception as e:
            print('There was a general error')
            print('Build in error info:')  
            print(type(e), e, e._doc_, sep='\n')       


    @staticmethod 
    def cd_deletion(table): 

        """Function to manage user input and delete items from the dictionary list

        Processes user data that identifies the CD to be deleted and deletes from the  2D table
        (list of dicts). The user identifies the CD ID to be deleted, and all data associated with the ID
        is deleted.

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """      
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')



class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table): ## Previously this was reading in a txt file, converted to .dat file.
        """Function to read binary data file

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtimeable

        Returns:
            data (Binary data file): Creates binary data file
            
        Raises:
            FileNotFoundError: Text file does not exist
            Exception: Any exception  
            
        """
        ## Loads binary data
        try:
            table.clear()    # this clears existing data and allows to load data from file
            with open(file_name, 'rb') as objFile:
                data = pickle.load(objFile) # Note: load () loads one line of data
            return data
            for line in data:
                table.append(line)
            objFile.close()
        ## Added Error handling
        except FileNotFoundError as e:
            print('Text file does not exist')
            print('Build in error info:')
            print(type(e), e, e._doc_, sep='\n')
        except Exception as e:
            print('There was a general error')
            print('Build in error info:')  
            print(type(e), e, e._doc_, sep='\n')    
            

    @staticmethod
    def write_file(file_name, table): ## Previously being saved as a txt file, now saving as binary file.
        # TODOne Add code here
        """Function to save current CD Inventory list as binary data

        Args:
            file_name (string): name of file to write data to
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
            
        Raises:
            FileNotFoundError: Text file does not exist
            Exception: Any exception
        
        """ 
        ## Save binary data
        try:
            with open(file_name, 'wb') as objFile:
                pickle.dump(table, objFile)
        ## Added Error Handling
        except FileNotFoundError as e:
            print('Text file does not exist')
            print('Build in error info:')
            print(type(e), e, e._doc_, sep='\n')
        except Exception as e:
            print('There was a general error')
            print('Build in error info:')  
            print(type(e), e, e._doc_, sep='\n')      
        
    

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    # TODOne add I/O functions as needed
 
    @staticmethod
    def cd_data():

        """Function to collect CD Data from the user: CD ID, Album, Artist

        Args:
            None.

        Returns:
            strID (string): this is the CD ID entered by the user
            strTitle (string): this is the CD's title
            strArtist (string): this is the Artist of the CD      
        
        Raises:
            ValueError: When value entered is not a number
            Exception: Any exceptions

        """        
        ## Add Error handling
        try:
            strID = input('Enter ID: ').strip()
            strTitle = input('What is the CD\'s title? ').strip()
            strArtist = input('What is the Artist\'s name? ').strip()
            return strID, strTitle, strArtist
        except ValueError as e:
            print('That is not valid CD ID!')
            print('Build in error info:')
            print(type(e), e, e._doc_, sep='\n')
        except Exception as e:
            print('There was a general error')
            print('Build in error info:')  
            print(type(e), e, e._doc_, sep='\n')
            
# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)
print('Successfully read CDInventory.dat file')

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # TODOne move IO code into function
        strID, strTitle, strArtist = IO.cd_data()

        # 3.3.2 Add item to the table
        # TODOne move processing code into function
        DataProcessor.cd_addition(strID, strTitle, strArtist, lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        ## Added Error Handling
        try:
            intIDDel = int(input('Which ID would you like to delete? ').strip())
        except ValueError as e:
            print('That is not valid CD ID!')
            print('Build in error info:')
            print(type(e), e, e._doc_, sep='\n')
        except Exception as e:
            print('There was a general error')
            print('Build in error info:')  
            print(type(e), e, e._doc_, sep='\n')       
        

        # 3.5.2 search thru table and delete CD
        # TODOne move processing code into function
        DataProcessor.cd_deletion(lstTbl) 
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TODOne move processing code into function
            FileProcessor.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




