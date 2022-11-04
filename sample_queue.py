# sample_two.py
#https://wiki.wxpython.org/How%20to%20create%20a%20list%20control%20with%20a%20SQLite%20database%20%28Phoenix%29

# Authors      : Beppe and Guldo
#                Updated and improved for wxPython Phoenix by Ecco
# Date (d/m/y) : 31/09/2007 (v0.0.1)
#                15/06/2020 (v0.0.3)
# Version      : 0.0.3
# Web          : Python-it.org  
# Description  : Shows some wx.ListCtrl utilities.
#                Correct mode for Insert, Update and Delete
#                record in a SQLite 3 database.
#                How to call a function of a frame from
#                another frame.
#                It use Northwind database ah ah ah !!!
#                Enjoy yourself !

import sys
import os
import time 
import sqlite3
import re
import wx
import wx.lib.mixins.inspection
import wx.lib.mixins.listctrl as listmix

AppTitle = "List of employees (sort)"
iEmployees = 0

ID_LIST = wx.NewIdRef()

# class MyConnection
# class MyInsertDlg
# class MyUpdateDlg
# class MyListCtrl
# class MyFrame
# class MyApp

#-------------------------------------------------------------------------------


class MyConnection(object):
    """
    ...
    """    
    def __init__(self):

        #------------
        
        # Return database folder.
        self.database_dir = wx.GetApp().GetDatabaseDir()

        # Loading "northwind" file.  
        #dbFile = os.path.join(self.database_dir, "northwind.db")
        dbFile = os.path.join(self.database_dir, "queue.db")
        print(dbFile)
        #------------
        
        # Create/connect to a permanent file database.
        # For temporary testing you can use memory only.
        # Open a connection to a DB in RAM :
        # self.con = lite.connect(":memory:")  
        self.con = sqlite3.connect(dbFile, isolation_level=None,
                                   detect_types=sqlite3.PARSE_DECLTYPES)

        # Establish the cursor, needed to execute the connected db.       
        self.cur = self.con.cursor()

        try:
            # Create/execute a table (ex : Employees) : 
            self.cur.execute("""CREATE TABLE IF NOT EXISTS Employees (
                                             EmployeeID INTEGER PRIMARY KEY,
                                             Surname TEXT,
                                             Firstname TEXT,
                                             Phone TEXT,
                                             Email TEXT)
                             """)
        
        except sqlite3.OperationalError:
            wx.LogMessage("Can not create the database, "
                          "maybe because it already exists ?")
            return
            
        # Important if you make changes to the database commits
        # current data to the db file (data is persistant now).
        self.con.commit()

    #-----------------------------------------------------------------------

    def OnQuery(self, sSQL):
        """
        Execute a query passed in the argument from the main frame.
        """

        self.cur.execute(sSQL)
        # Here create the recordset.
        # It's a list of a list...
        rsRecordSet = self.cur.fetchall()
        
        return rsRecordSet


    def OnQueryParameter(self, sSQL, sParameter):
        """
        ...
        """

        Parameter =(sParameter, )
      
        self.cur.execute(sSQL, Parameter)
        rsRecordSet = self.cur.fetchall()
            
        return rsRecordSet
        

    def OnQueryUpdate(self, sSQL, sParameter):   
        """
        ...
        """

        self.cur.execute(sSQL, sParameter)
        rsRecordSet = self.cur.fetchall()
            
        return rsRecordSet


    def OnSqliteVersion(self):
        """
        Returns SQLite version.
        """

        self.cur.execute("SELECT SQLITE_VERSION()")

        version = self.cur.fetchone()
       
        return version


    def OnCloseDb(self):
        """
        Disconnect database connection.
        """

        # Disconnect from server.
        self.cur.close()
        self.con.close()
        
#-------------------------------------------------------------------------------

class MyInsertDlg(wx.Dialog):
    """
    ...
    """
    def __init__(self, caller_dlgInsert, title=""):
        wx.Dialog.__init__(self,
                           parent=caller_dlgInsert,
                           id=-1,
                           title="")

        #------------
        
        self.caller = caller_dlgInsert

        #------------

        # Return icons folder.
        self.icons_dir = wx.GetApp().GetIconsDir()

        #------------

        # Simplified init method.
        self.ConnectDb()
        self.SetProperties()
        self.CreateCtrls()
        self.BindEvents()
        self.DoLayout()

    #---------------------------------------------------------------------------

    def ConnectDb(self):
        """
        Connection to the database. 
        """

        # Instance from Class MyConnection.       
        self.con = MyConnection()

        
    def SetProperties(self):
        """
        Set the frame properties (title, icon, size...).
        """

        # Setting some frame properties.
        frameIcon = wx.Icon(os.path.join(self.icons_dir,
                                         "icon_wxWidgets.ico"),
                            type=wx.BITMAP_TYPE_ICO)
        self.SetIcon(frameIcon)


    def CreateCtrls(self):
        """
        Create some controls for my frame.
        """

        # wx.Font(pointSize, family, style, weight, underline, faceName)
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetWeight(wx.BOLD)

        #------------
        
        # Widgets.       
        self.panel = wx.Panel(self)

        #--
        
        self.stSurname = wx.StaticText(self.panel, -1, "Surname_ :")
        self.stSurname.SetForegroundColour("gray")
        self.stSurname.SetFont(font)

        self.txSurname = wx.TextCtrl(self.panel, -1, "", size=(230, -1))

        #--
        
        self.stFirstname = wx.StaticText(self.panel, -1, "First name :")
        self.stFirstname.SetForegroundColour("gray")
        self.stFirstname.SetFont(font)

        self.txFirstname = wx.TextCtrl(self.panel, -1, "", size=(230, -1))

        #--

        message  = "- Max chars : 2."
        
        self.stPhone = wx.StaticText(self.panel, -1, "Phone :")
        self.stPhone.SetForegroundColour("gray")
        self.stPhone.SetFont(font)
        
        self.txPhone1 = wx.TextCtrl(self.panel, -1, "", size=(35, -1),
                                    style=wx.TE_CENTRE)
        self.txPhone1.SetMaxLength(2)
        self.txPhone1.SetForegroundColour("gray")
        self.txPhone1.SetBackgroundColour("yellow")
        self.txPhone1.SetFont(font)
        
        self.hyphen1 = wx.StaticText(self.panel, -1, "-")
        
        self.txPhone2 = wx.TextCtrl(self.panel, -1, "", size=(35, -1),
                                    style=wx.TE_CENTRE)
        self.txPhone2.SetMaxLength(2)
        
        self.hyphen2 = wx.StaticText(self.panel, -1, "-")
        
        self.txPhone3 = wx.TextCtrl(self.panel, -1, "", size=(35, -1),
                                    style=wx.TE_CENTRE)
        self.txPhone3.SetMaxLength(2)
        
        self.hyphen3 = wx.StaticText(self.panel, -1, "-")
        
        self.txPhone4 = wx.TextCtrl(self.panel, -1, "", size=(35, -1),
                                    style=wx.TE_CENTRE)
        self.txPhone4.SetMaxLength(2)
        
        self.hyphen4 = wx.StaticText(self.panel, -1, "-")
        
        self.txPhone5 = wx.TextCtrl(self.panel, -1, "", size=(35, -1),
                                    style=wx.TE_CENTRE)
        self.txPhone5.SetMaxLength(2)
        
        #--
        
        self.stEmail = wx.StaticText(self.panel, -1, "Email :")
        self.stEmail.SetForegroundColour("gray")
        self.stEmail.SetFont(font)
        
        self.txEmail = wx.TextCtrl(self.panel, -1, "", size=(230, -1))

        #--
        
        self.StaticSizer = wx.StaticBox(self.panel, -1, "")

        #--
        
        self.bntSave = wx.Button(self.panel, -1, "&Save")
        self.bntSave.SetToolTip("Save !")

        self.bntClose = wx.Button(self.panel, -1, "&Close")
        self.bntClose.SetToolTip("Close !")


    def BindEvents(self):
        """
        Bind all the events related to my frame.
        """

        self.txSurname.Bind(wx.EVT_TEXT, self.OnUpperCaseText)
        self.txFirstname.Bind(wx.EVT_TEXT, self.OnCapitalizeCaseText)
        self.txEmail.Bind(wx.EVT_TEXT, self.OnLowerCaseText)

        self.txPhone1.Bind(wx.EVT_CHAR, self.OnChar)
        self.txPhone2.Bind(wx.EVT_CHAR, self.OnChar)
        self.txPhone3.Bind(wx.EVT_CHAR, self.OnChar)
        self.txPhone4.Bind(wx.EVT_CHAR, self.OnChar)
        self.txPhone5.Bind(wx.EVT_CHAR, self.OnChar)
        
        self.Bind(wx.EVT_BUTTON, self.OnSave, self.bntSave)
        self.Bind(wx.EVT_BUTTON, self.OnExit, self.bntClose)

        self.Bind(wx.EVT_CLOSE, self.OnExit)


    def DoLayout(self):
        """
        Do layout.
        """

        # Sizers.
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        textSizer = wx.FlexGridSizer(cols=2, vgap=5, hgap=5)
        textSizer.AddGrowableCol(1)
        
        buttonSizer = wx.StaticBoxSizer(self.StaticSizer, wx.VERTICAL)
        
        # Assign widgets to sizers.

        # textSizer.
        textSizer.Add(self.stSurname, 0, wx.ALIGN_CENTER_VERTICAL)
        textSizer.Add(self.txSurname, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)
        
        textSizer.Add(self.stFirstname, 0, wx.ALIGN_CENTER_VERTICAL)
        textSizer.Add(self.txFirstname, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)

        textSizer.Add(self.stPhone, 0, wx.ALIGN_CENTER_VERTICAL)
        
        ctrlSizer = wx.BoxSizer(wx.HORIZONTAL)
        ctrlSizer.Add(self.txPhone1, 1, wx.EXPAND)
        ctrlSizer.Add(self.hyphen1, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        ctrlSizer.Add(self.txPhone2, 1, wx.EXPAND)
        ctrlSizer.Add(self.hyphen2, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        ctrlSizer.Add(self.txPhone3, 1, wx.EXPAND)
        ctrlSizer.Add(self.hyphen3, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        ctrlSizer.Add(self.txPhone4, 1, wx.EXPAND)
        ctrlSizer.Add(self.hyphen4, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        ctrlSizer.Add(self.txPhone5, 1, wx.EXPAND)

        textSizer.Add(ctrlSizer, 1, wx.EXPAND)       
        textSizer.Add(self.stEmail, 0, wx.ALIGN_CENTER_VERTICAL)
        textSizer.Add(self.txEmail, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)
     
        # buttonSizer.
        buttonSizer.Add(self.bntSave)
        buttonSizer.Add((5, 5), -1)
        buttonSizer.Add(self.bntClose)
       
        # Assign to mainSizer the other sizers.  
        mainSizer.Add(textSizer, 0, wx.ALL, 10)
        mainSizer.Add(buttonSizer, 0, wx.ALL, 10)
        
        # Assign to panel the mainSizer.
        self.panel.SetSizer(mainSizer)
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)

        
    def FieldsControl(self):
        """
        ...
        """
        
        if len(self.txSurname.GetValue()) == 0:
                wx.MessageBox('ATTENTION !\nThe "Surname" field is empty !',
                              AppTitle,
                              wx.OK | wx.ICON_INFORMATION)
                
                self.txSurname.SetFocus()
                
                return 0

        elif len(self.txFirstname.GetValue()) == 0:
                wx.MessageBox('ATTENTION !\nThe "First name" field is empty !',
                              AppTitle,
                              wx.OK | wx.ICON_INFORMATION)
                
                return 0

        elif len(self.txPhone1.GetValue()) < 2:
                wx.MessageBox('ATTENTION !\nThe "Phone" field is empty or icomplete !',
                              "Phone number",
                              wx.OK | wx.ICON_INFORMATION)
                
                return 0

        elif len(self.txPhone2.GetValue()) < 2:
                wx.MessageBox('ATTENTION !\nThe "Phone" field is empty or icomplete !',
                              "Phone number",
                              wx.OK | wx.ICON_INFORMATION)
                
                return 0

        elif len(self.txPhone3.GetValue()) < 2:
                wx.MessageBox('ATTENTION !\nThe "Phone" field is empty or icomplete !',
                              "Phone number",
                              wx.OK | wx.ICON_INFORMATION)
                
                return 0

        elif len(self.txPhone4.GetValue()) < 2:
                wx.MessageBox('ATTENTION !\nThe "Phone" field is empty or icomplete !',
                              "Phone number",
                              wx.OK | wx.ICON_INFORMATION)
                
                return 0

        elif len(self.txPhone5.GetValue()) < 2:
                wx.MessageBox('ATTENTION !\nThe "Phone" field is empty or icomplete !',
                              "Phone number",
                              wx.OK | wx.ICON_INFORMATION)
                
                return 0
            
        elif len(self.txEmail.GetValue()) == 0:
                wx.MessageBox('ATTENTION !\nThe "Email" field is empty !',
                              AppTitle,
                              wx.OK | wx.ICON_INFORMATION)
                
                return 0
            

    def OnSave(self, event):
        """
        ...
        """
        
        if self.FieldsControl() == 0:
            
            return
        
        else:
            sMessage = "Save new employee data ?"
            dlgAsk = wx.MessageDialog(None,
                                      sMessage,
                                      AppTitle,
                                      wx.YES_NO | wx.ICON_QUESTION)
            
            retCode = dlgAsk.ShowModal()
            
            if (retCode == wx.ID_YES):                
                sSurname = str(self.txSurname.GetValue())
                sFirstname = str(self.txFirstname.GetValue())
                #--            
                value1 = str(self.txPhone1.GetValue())
                value2 = str(self.txPhone2.GetValue())
                value3 = str(self.txPhone3.GetValue())
                value4 = str(self.txPhone4.GetValue())
                value5 = str(self.txPhone5.GetValue())
                number = value1 + value2 + value3 + value4 + value5
                sPhone = self.AddHyphens(number)
                #--
                sEmail = str(self.txEmail.GetValue())
                
                InsertParameters = (sSurname,
                                    sFirstname,
                                    sPhone,
                                    sEmail)

                sSQL = "INSERT INTO Employees (Surname, \
                                               Firstname, \
                                               Phone, \
                                               Email) \
                                       VALUES (?, ?, ?, ?)"

                # Insert new data in the database.
                self.con.OnQueryUpdate(sSQL, InsertParameters)

                # Guldo... thank you !
                self.caller.OnUpdateList()
                
                wx.MessageBox("New data insert !",
                              AppTitle,
                              wx.OK | wx.ICON_INFORMATION)
            
            elif (retCode == wx.ID_NO):
                wx.MessageBox("Insert operation aborted !",
                              AppTitle,
                              wx.OK | wx.ICON_INFORMATION)
     
            dlgAsk.Destroy()
            self.OnExit(self)
     
    
    def OnUpperCaseText(self, event):        
        """
        ...
        """

        # Write in upper mode on widgets the call it.        
        # Adapted from a script of David Hughes
        # Forestfield Software.   
        # Retrive the widget.
        wdgControl = event.GetEventObject()

        # Retrive what we have write.       
        retValue = wdgControl.GetValue()

        # Upper it.
        upValue = retValue.upper()

        if retValue != upValue:
            wdgControl.SetValue(upValue)
            # Insert it at the end.
            wdgControl.SetInsertionPointEnd()

        event.Skip()


    def OnLowerCaseText(self, event):        
        """
        ...
        """

        # Write in lower mode on widgets the call it.        
        # Adapted from a script of David Hughes
        # Forestfield Software.   
        # Retrive the widget.
        wdgControl = event.GetEventObject()

        # Retrive what we have write.       
        retValue = wdgControl.GetValue()

        # Lower it.
        upValue = retValue.lower()

        if retValue != upValue:
            wdgControl.SetValue(upValue)
            # Insert it at the end.
            wdgControl.SetInsertionPointEnd()

        event.Skip()


    def OnCapitalizeCaseText(self, event):        
        """
        ...
        """

        # Write in capitalize mode on widgets the call it.        
        # Adapted from a script of David Hughes
        # Forestfield Software.   
        # Retrive the widget.
        wdgControl = event.GetEventObject()

        # Retrive what we have write.       
        retValue = wdgControl.GetValue()

        # Capitalize it.
        upValue = retValue.lower().capitalize()

        if retValue != upValue:
            wdgControl.SetValue(upValue)
            # Insert it at the end.
            wdgControl.SetInsertionPointEnd()

        event.Skip()


    def OnChar(self, event):
        """
        Block non numbers.
        """

        # print("\ndef OnChar")
        
        key_code = event.GetKeyCode()

        # Allow ASCII numerics.
        if ord('0') <= key_code <= ord('9'):
            event.Skip()
            return

        # Allow decimal points.
        if key_code == ord('.'):
            event.Skip()
            return

        # Allow tabs, for tab navigation between TextCtrls.
        if key_code == ord('\t'):
            event.Skip()
            return

        # Enable backspace, del, left-right.
        # The values may be platform dependent.
        if key_code in (8, 127, 314, 316):
            event.Skip()
            return

        # Block everything else.
        return


    def AddHyphens(self, nb):
        """
        ...
        """

        phone = nb[0:2] + '-' + nb[2:4] + '-' + nb[4:6] + '-' + nb[6:8] + '-' + nb[8:10]
        
        return phone

        
    def OnExit(self, event):
        """
        ...
        """
     
        self.Destroy()

#-------------------------------------------------------------------------------
        
class MyUpdateDlg(wx.Dialog):
    """
    ...
    """
    def __init__(self, caller_dlgUpdate, title=""):
        wx.Dialog.__init__(self,
                           parent=caller_dlgUpdate,
                           id=-1,
                           title=title,
                           size=(400, 200))

        #------------
        
        self.caller = caller_dlgUpdate

        #------------

        # Return icons folder.
        self.icons_dir = wx.GetApp().GetIconsDir()

        #------------

        # Simplified init method.
        self.ConnectDb()
        self.SetProperties()
        self.CreateCtrls()
        self.BindEvents()
        self.DoLayout()

    #---------------------------------------------------------------------------

    def ConnectDb(self):
        """
        Connection to the database. 
        """

        # Instance from Class MyConnection.       
        self.con = MyConnection()

        
    def SetProperties(self):
        """
        Set the frame properties (title, icon, size...).
        """

        # Setting some frame properties.
        frameIcon = wx.Icon(os.path.join(self.icons_dir,
                                         "icon_wxWidgets.ico"),
                            type=wx.BITMAP_TYPE_ICO)
        self.SetIcon(frameIcon)


    def CreateCtrls(self):
        """
        Create some controls for my frame.
        """

        # wx.Font(pointSize, family, style, weight, underline, faceName)
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetWeight(wx.BOLD)

        #------------
        
        # Widgets.
        self.panel = wx.Panel(self)

        #--
        
        self.stEmployeeID = wx.StaticText(self.panel, -1, "ID :")
        self.stEmployeeID.SetForegroundColour("red")
        self.stEmployeeID.SetFont(font)

        self.txEmployeeID = wx.TextCtrl(self.panel, -1, "", size=(230, -1),
                                        style=wx.TE_READONLY | wx.TE_CENTRE)
        self.txEmployeeID.SetForegroundColour("white")
        self.txEmployeeID.SetBackgroundColour("#CD5C5C")
        self.txEmployeeID.SetFont(font)

        #--
        
        self.stSurname = wx.StaticText(self.panel, -1, "Surname :")
        self.stSurname.SetForegroundColour("gray")
        self.stSurname.SetFont(font)

        self.txSurname = wx.TextCtrl(self.panel, -1, "", size=(230, -1))

        #--
        
        self.stFirstname = wx.StaticText(self.panel, -1, "First name :")
        self.stFirstname.SetForegroundColour("gray")
        self.stFirstname.SetFont(font)

        self.txFirstname = wx.TextCtrl(self.panel, -1, "", size=(230, -1))

        #--
        
        self.stPhone = wx.StaticText(self.panel, -1, "Phone :")
        self.stPhone.SetForegroundColour("gray")
        self.stPhone.SetFont(font)
        
        self.txPhone1 = wx.TextCtrl(self.panel, -1, "", size=(35, -1),
                                    style=wx.TE_CENTRE)
        self.txPhone1.SetMaxLength(2)
        self.txPhone1.SetForegroundColour("gray")
        self.txPhone1.SetBackgroundColour("yellow")
        self.txPhone1.SetFont(font)
        
        self.hyphen1 = wx.StaticText(self.panel, -1, "-")
        
        self.txPhone2 = wx.TextCtrl(self.panel, -1, "", size=(35, -1),
                                    style=wx.TE_CENTRE)
        self.txPhone2.SetMaxLength(2)
        
        self.hyphen2 = wx.StaticText(self.panel, -1, "-")
        
        self.txPhone3 = wx.TextCtrl(self.panel, -1, "", size=(35, -1),
                                    style=wx.TE_CENTRE)
        self.txPhone3.SetMaxLength(2)
        
        self.hyphen3 = wx.StaticText(self.panel, -1, "-")
        
        self.txPhone4 = wx.TextCtrl(self.panel, -1, "", size=(35, -1),
                                    style=wx.TE_CENTRE)
        self.txPhone4.SetMaxLength(2)
        
        self.hyphen4 = wx.StaticText(self.panel, -1, "-")
        
        self.txPhone5 = wx.TextCtrl(self.panel, -1, "", size=(35, -1),
                                    style=wx.TE_CENTRE)
        self.txPhone5.SetMaxLength(2)
        
        #--
        
        self.stEmail = wx.StaticText(self.panel, -1, "Email :")
        self.stEmail.SetForegroundColour("gray")
        self.stEmail.SetFont(font)
        
        self.txEmail = wx.TextCtrl(self.panel, -1, "", size=(230, -1))

        #--
        
        self.StaticSizer = wx.StaticBox(self.panel, -1,"")

        #--
        
        self.bntSave = wx.Button(self.panel, -1, "&Save")
        self.bntSave.SetToolTip("Save !")

        self.bntClose = wx.Button(self.panel, -1, "&Close")
        self.bntClose.SetToolTip("Close !")



    def BindEvents(self):
        """
        Bind all the events related to my frame.
        """

        self.txSurname.Bind(wx.EVT_TEXT, self.OnUpperCaseText)
        self.txFirstname.Bind(wx.EVT_TEXT, self.OnCapitalizeCaseText) 
        self.txEmail.Bind(wx.EVT_TEXT, self.OnLowerCaseText)  

        self.txPhone1.Bind(wx.EVT_CHAR, self.OnChar)
        self.txPhone2.Bind(wx.EVT_CHAR, self.OnChar)
        self.txPhone3.Bind(wx.EVT_CHAR, self.OnChar)
        self.txPhone4.Bind(wx.EVT_CHAR, self.OnChar)
        self.txPhone5.Bind(wx.EVT_CHAR, self.OnChar)
        
        self.Bind(wx.EVT_BUTTON, self.OnSave, self.bntSave)
        self.Bind(wx.EVT_BUTTON, self.OnExit, self.bntClose)

        self.Bind(wx.EVT_CLOSE, self.OnExit)


    def DoLayout(self):
        """
        Do layout.
        """

        # Sizers.
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        textSizer = wx.FlexGridSizer(cols=2, vgap=5, hgap=5)
        textSizer.AddGrowableCol(1)
        
        buttonSizer = wx.StaticBoxSizer(self.StaticSizer, wx.VERTICAL)
        
        # Assign widgets to sizers.

        # textSizer.
        textSizer.Add(self.stEmployeeID, 0, wx.ALIGN_CENTER_VERTICAL)
        textSizer.Add(self.txEmployeeID, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)
        
        textSizer.Add(self.stSurname, 0, wx.ALIGN_CENTER_VERTICAL)
        textSizer.Add(self.txSurname, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)
        
        textSizer.Add(self.stFirstname, 0, wx.ALIGN_CENTER_VERTICAL)
        textSizer.Add(self.txFirstname, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)

        textSizer.Add(self.stPhone, 0, wx.ALIGN_CENTER_VERTICAL)

        ctrlSizer = wx.BoxSizer(wx.HORIZONTAL)
        ctrlSizer.Add(self.txPhone1, 1, wx.EXPAND)
        ctrlSizer.Add(self.hyphen1, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        ctrlSizer.Add(self.txPhone2, 1, wx.EXPAND)
        ctrlSizer.Add(self.hyphen2, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        ctrlSizer.Add(self.txPhone3, 1, wx.EXPAND)
        ctrlSizer.Add(self.hyphen3, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        ctrlSizer.Add(self.txPhone4, 1, wx.EXPAND)
        ctrlSizer.Add(self.hyphen4, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        ctrlSizer.Add(self.txPhone5, 1, wx.EXPAND)

        textSizer.Add(ctrlSizer, 1, wx.EXPAND)
        
        textSizer.Add(self.stEmail, 0, wx.ALIGN_CENTER_VERTICAL)
        textSizer.Add(self.txEmail, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)
        
        # buttonSizer.
        buttonSizer.Add(self.bntSave)
        buttonSizer.Add((5, 5), -1)
        buttonSizer.Add(self.bntClose)
       
        # Assign to mainSizer the other sizers.  
        mainSizer.Add(textSizer, 0, wx.ALL, 10)
        mainSizer.Add(buttonSizer, 0, wx.ALL, 10)
        
        # Assign to panel the mainSizer.
        self.panel.SetSizer(mainSizer)
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)

        
    def FieldsControl(self):
        """
        ...
        """
        
        if len(self.txSurname.GetValue()) == 0:
                wx.MessageBox('ATTENTION !\nThe "Surname" field is empty !',
                              AppTitle,
                              wx.OK | wx.ICON_INFORMATION)
                
                self.txSurname.SetFocus()
                
                return 0

        elif len(self.txFirstname.GetValue()) == 0:
                wx.MessageBox('ATTENTION !\nThe "First name" field is empty !',
                              AppTitle,
                              wx.OK | wx.ICON_INFORMATION)
                
                return 0

        elif len(self.txPhone1.GetValue()) < 2:
                wx.MessageBox('ATTENTION !\nThe "Phone" field is empty or icomplete !',
                              "Phone number",
                              wx.OK | wx.ICON_INFORMATION)
                
                return 0

        elif len(self.txPhone2.GetValue()) < 2:
                wx.MessageBox('ATTENTION !\nThe "Phone" field is empty or icomplete !',
                              "Phone number",
                              wx.OK | wx.ICON_INFORMATION)
                
                return 0

        elif len(self.txPhone3.GetValue()) < 2:
                wx.MessageBox('ATTENTION !\nThe "Phone" field is empty or icomplete !',
                              "Phone number",
                              wx.OK | wx.ICON_INFORMATION)
                
                return 0

        elif len(self.txPhone4.GetValue()) < 2:
                wx.MessageBox('ATTENTION !\nThe "Phone" field is empty or icomplete !',
                              "Phone number",
                              wx.OK | wx.ICON_INFORMATION)
                
                return 0

        elif len(self.txPhone5.GetValue()) < 2:
                wx.MessageBox('ATTENTION !\nThe "Phone" field is empty or icomplete !',
                              "Phone number",
                              wx.OK | wx.ICON_INFORMATION)
                
                return 0
            
        elif len(self.txEmail.GetValue()) == 0:
                wx.MessageBox('ATTENTION !\nThe "Email" field is empty !',
                              AppTitle,
                              wx.OK | wx.ICON_INFORMATION)
                
                return 0
            
            
    def OnSave(self, event):
        """
        ...
        """
        
        if self.FieldsControl()==0:
            
            return
        
        else:
            sMessage = "Save update data?"
            dlgAsk = wx.MessageDialog(None,
                                      sMessage,
                                      AppTitle,
                                      wx.YES_NO | wx.ICON_QUESTION)
            
            retCode = dlgAsk.ShowModal()
            
            if (retCode == wx.ID_YES):

                sEmployeeID = str(self.txEmployeeID.GetValue())
                sSurname = str(self.txSurname.GetValue())
                sFirstname = str(self.txFirstname.GetValue())             
                #--
                value1 = str(self.txPhone1.GetValue())
                value2 = str(self.txPhone2.GetValue())
                value3 = str(self.txPhone3.GetValue())
                value4 = str(self.txPhone4.GetValue())
                value5 = str(self.txPhone5.GetValue())
                number = value1 + value2 + value3 + value4 + value5
                sPhone = self.AddHyphens(number)
                #--                
                sEmail = str(self.txEmail.GetValue())
                
                UpdateParameters = (sSurname,
                                    sFirstname,
                                    sPhone,
                                    sEmail,
                                    sEmployeeID)

                sSQL = "UPDATE Employees SET Surname = ?, \
                                             Firstname = ?, \
                                             Phone = ?, \
                                             Email = ? \
                                       WHERE EmployeeID = ?"

                # Update the database.
                self.con.OnQueryUpdate(sSQL, UpdateParameters)

                # Guldo... thank you !
                self.caller.OnUpdateList()
           
                wx.MessageBox("Data update!",
                              AppTitle,
                              wx.OK | wx.ICON_INFORMATION)
        
            elif (retCode == wx.ID_NO):
                wx.MessageBox("Update operation aborted!",
                              AppTitle,
                              wx.OK | wx.ICON_INFORMATION)
     
            dlgAsk.Destroy()
            self.OnExit(self)
            

    def OnUpperCaseText(self, event):        
        """
        ...
        """
        
        # Write in upper mode on widgets the call it.        
        # Adapted from a script of David Hughes
        # Forestfield Software.   
        # Retrive the widget.
        wdgControl = event.GetEventObject()

        # Retrive what we have write.       
        retValue = wdgControl.GetValue()

        # Upper it.
        upValue = retValue.upper()

        if retValue != upValue:
            wdgControl.SetValue(upValue)
            # Insert it at the end.
            wdgControl.SetInsertionPointEnd()

        event.Skip()


    def OnLowerCaseText(self, event):        
        """
        ...
        """

        # Write in upper mode on widgets the call it.        
        # Adapted from a script of David Hughes
        # Forestfield Software.   
        # Retrive the widget.
        wdgControl = event.GetEventObject()

        # Retrive what we have write.       
        retValue = wdgControl.GetValue()

        # Upper it.
        upValue = retValue.lower()

        if retValue != upValue:
            wdgControl.SetValue(upValue)
            # Insert it at the end.
            wdgControl.SetInsertionPointEnd()

        event.Skip()


    def OnCapitalizeCaseText(self, event):        
        """
        ...
        """

        # Write in upper mode on widgets the call it.        
        # Adapted from a script of David Hughes
        # Forestfield Software.   
        # Retrive the widget.
        wdgControl = event.GetEventObject()

        # Retrive what we have write.       
        retValue = wdgControl.GetValue()

        # Upper it.
        upValue = retValue.lower().capitalize()

        if retValue != upValue:
            wdgControl.SetValue(upValue)
            # Insert it at the end.
            wdgControl.SetInsertionPointEnd()

        event.Skip()
        

    def OnChar(self, event):
        """
        Block non numbers.
        """

        # print("\ndef OnChar")
        
        key_code = event.GetKeyCode()

        # Allow ASCII numerics.
        if ord('0') <= key_code <= ord('9'):
            event.Skip()
            return

        # Allow decimal points.
        if key_code == ord('.'):
            event.Skip()
            return

        # Allow tabs, for tab navigation between TextCtrls.
        if key_code == ord('\t'):
            event.Skip()
            return

        # Enable backspace, del, left-right.
        # The values may be platform dependent.
        if key_code in (8, 127, 314, 316):
            event.Skip()
            return

        # Block everything else.
        return


    def AddHyphens(self, nb):
        """
        ...
        """
        
        phone = nb[0:2] + '-' + nb[2:4] + '-' + nb[4:6] + '-' + nb[6:8] + '-' + nb[8:10]
        
        return phone


    def OnExit(self, event):
        """
        ...
        """
        
        self.Destroy()

#-------------------------------------------------------------------------------

class MyListCtrl(wx.ListCtrl,
                 # listmix.ListRowHighlighter,                 
                 listmix.ColumnSorterMixin,
                 listmix.ListCtrlAutoWidthMixin):   
    """
    ...
    """   
    def __init__(self, parent, id, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        super(MyListCtrl, self).__init__(parent, ID_LIST, pos, size, style)

        #------------

        # Returns bitmaps folder.
        self.bitmaps_dir = wx.GetApp().GetBitmapsDir()

        #------------

        # Simplified init method
        self.ConnectDb()
        self.OpenDatabase()
        self.CreateColumns() 
        self.SetProperties() 
        self.PopulateListCtrl()
        self.BindEvents() 
     
        #------------

        # Mixins.
        # Now that the list exists we can init the other base class.        
        # listmix.ListRowHighlighter.__init__(self)

        # Initialize the listCtrl auto width.
        listmix.ListCtrlAutoWidthMixin.__init__(self)

        # Initialize the column sorter.
        listmix.ColumnSorterMixin.__init__(self, self.GetColumnCount())        
        # or
        # listmix.ColumnSorterMixin.__init__(self, 5)

        #------------
        
        self.SortListItems(0, True)
       
    #---------------------------------------------------------------------------

    def ConnectDb(self):
        """
        Connection to the database.
        """
        
        self.con = MyConnection()


    def OpenDatabase(self):
        """
        Open and connect the database.
        """
        
        # Retrieve employees data from database
        # using the class named MyConnection.
        strSQL = "SELECT * FROM Employees"
        
        # The recordset retrieved
        self.rsRecordset = self.con.OnQuery(strSQL)
        self.items = self.rsRecordset
        
        return self.rsRecordset


    def CreateColumns(self):
        """
        Create columns for listCtrl.
        """
        
        columns = ["ID",
                   "Surname",
                   "First name",
                   "Phone",
                   "Email"]

        # Add some columns (x5).
        for col, header in enumerate(columns):
            self.InsertColumn(col, header)

        #------------

        # Set the width of the columns (x5).
        # Integer, wx.LIST_AUTOSIZE or wx.LIST_AUTOSIZE_USEHEADER.
        for col, width in enumerate((55,
                                     130,
                                     130,
                                     110,
                                     2000)):
            self.SetColumnWidth(col, width)
            
    
    def SetProperties(self):
        """
        Set the list control properties (icon, font, size...).
        """

        # Font size and style for listCtrl.
        fontSize = self.GetFont().GetPointSize()

        # Text attributes for columns title.
        # wx.Font(pointSize, family, style, weight, underline, faceName)
        if wx.Platform in ["__WXMAC__", "__WXGTK__"]:
            boldFont = wx.Font(fontSize-1,
                               wx.DEFAULT,
                               wx.NORMAL,
                               wx.NORMAL,
                               False, "")
            self.SetForegroundColour("black")
            self.SetBackgroundColour("#ece9d8")

        else:
            boldFont = wx.Font(fontSize,
                               wx.DEFAULT,
                               wx.NORMAL,
                               wx.BOLD,
                               False, "")
            self.SetForegroundColour("#808080")
            self.SetBackgroundColour("#ece9d8")

        self.SetFont(boldFont)
     
        #------------

        # Image list.
        self.il = wx.ImageList(16, 16, True)

        # Set an icon for the first column.
        self.bmp1 = wx.Bitmap(os.path.join(self.bitmaps_dir,
                                           "employee.png"),
                              type=wx.BITMAP_TYPE_PNG)


        # Add some arrows for the column sorter.
        self.bmp2  = wx.Bitmap(os.path.join(self.bitmaps_dir,
                                            "sm_up.png"),
                               type=wx.BITMAP_TYPE_PNG)

        self.bmp3 = wx.Bitmap(os.path.join(self.bitmaps_dir,
                                           "sm_down.png"),
                              type=wx.BITMAP_TYPE_PNG)
        
        # Add images to list.        
        self.img_idx = self.il.Add(self.bmp1)
        self.sm_up = self.il.Add(self.bmp2)
        self.sm_down = self.il.Add(self.bmp3)
        
        # Assign the image list to it.
        self.SetImageList(self.il, wx.IMAGE_LIST_SMALL)

     
    def PopulateListCtrl(self):
        """
        Fill the wx.ListCtrl.
        """

        # Add the rows;
        self.itemDataMap = {}

        # Populate the wx.ListCtrl.
        for item in self.rsRecordset:
            index = self.InsertItem(self.GetItemCount(),
                                             ((str(item[0]))))                    
            self.SetItem(index, 1, item[1])
            self.SetItem(index, 2, item[2])
            self.SetItem(index, 3, item[3])
            self.SetItem(index, 4, item[4])
            
            # Not useful.
            self.SetItemImage(self.GetItemCount() - 1,
                              self.img_idx)

            # Give each item a data value, and map it back 
            # to the item values, for the column sorter.
            self.SetItemData(index, index)
            self.itemDataMap[index] = item

            # Alternate the row colors of a ListCtrl.
            # Mike Driscoll... thank you !
            if index % 2:
                self.SetItemBackgroundColour(index, "#ffffff")
            else:
                self.SetItemBackgroundColour(index, "#ece9d8")
       

    def BindEvents(self):
        """
        Bind all the events related to my frame.
        """

        # Intercept the click on the wx.ListCtrl.
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, id=ID_LIST)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected, id=ID_LIST) 
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemActivated, id=ID_LIST)
        self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick, id=ID_LIST)
        self.Bind(wx.EVT_LIST_COL_RIGHT_CLICK, self.OnColRightClick, id=ID_LIST)
        self.Bind(wx.EVT_LIST_COL_BEGIN_DRAG, self.OnColBeginDrag, id=ID_LIST)
        self.Bind(wx.EVT_LIST_COL_CLICK, self.OnSort, id=ID_LIST)


    def GetListCtrl(self):
        """
        Used by the ColumnSorterMixin.
        """
        
        # Alternate the row colors of a ListCtrl.
        if self.GetItemCount() > 0:
            for x in range(self.GetItemCount()):
                if x % 2 == 0:
                    self.SetItemBackgroundColour(x, "#ffffff")
                else:
                    self.SetItemBackgroundColour(x, "#ece9d8")        
        
        return self


    def GetSortImages(self):
        """
        Used by the ColumnSorterMixin.
        """
        
        return (self.sm_down, self.sm_up)
    

    def GetColumnText(self, index, col):
        """
        ...
        """
        
        item = self.GetItem(index, col)
        return item.GetText()


    def OnItemSelected(self, event):
        """
        ...
        """

        global iEmployees

        #------------
        
        self.currentItem = event.Index
        
        item = self.GetItem(self.currentItem)
        
        iEmployees = item.GetText()
        
        #------------

        # Show what was selected in the frame status bar.        
        frame = self.GetTopLevelParent()
        frame.PushStatusText("Selected employee = %s " %(iEmployees), 1)


    def OnItemDeselected(self, event):
        """
        ...
        """

        item = event.GetItem()
        print("OnItemDeselected: %d" % event.Index)

        # Show how to reselect something we don't want deselected.
        # if event.Index == 11:
        #     wx.CallAfter(self.list.SetItemState, 11, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)


    def OnItemActivated(self, event):
        """
        ...
        """
        
        self.currentItem = event.GetIndex()

        item = self.GetItem(self.currentItem)
        
        iEmployee = item.GetText()

        #------------

        # Show what was selected in the frame status bar.        
        frame = self.GetTopLevelParent()
        frame.PushStatusText("Selected employee = %s " %(iEmployee), 1)

        #------------
        
        frame.OnEdit(event)

        
    def OnRetrieveData(self, sSQL, IDParameter):
        """
        ...
        """

        global iEmployees         
        
        # Delete the item from listctrl.
        self.SetFocus()
        self.DeleteAllItems()
        
        # Retrieve the products recordset from data module.
        self.employeeData = self.con.OnQueryParameter(sSQL, IDParameter)

        # Add the rows;
        self.itemDataMap = {}
        
        # Populate the listctrl.       
        if self.employeeData:
            for item in self.employeeData:
                index = self.InsertItem(self.GetItemCount(),
                                                 ((str(item[0]))))
                self.SetItem(index, 1, item[1])
                self.SetItem(index, 2, item[2])
                self.SetItem(index, 3, item[3])
                self.SetItem(index, 4, item[4])
                
                # Not useful.
                self.SetItemImage(self.GetItemCount() - 1,
                                           self.img_idx)

                # Give each item a data value, and map it back 
                # to the item values, for the column sorter.
                self.SetItemData(index, index)
                self.itemDataMap[index] = item

                # Alternate the row colors of a ListCtrl.
                # Mike Driscoll... thank you !
                if index % 2:
                    self.SetItemBackgroundColour(index, "#ffffff")
                else:
                    self.SetItemBackgroundColour(index, "#ece9d8")
                
        else:
             wx.MessageBox("ATTENTION !\nNo results for your research criteria.\nTry with another criteria !",
                           AppTitle,
                           wx.OK | wx.ICON_INFORMATION)
             

    def OnRightDown(self, event):
        """
        Right down.
        """

        x = event.GetX()
        y = event.GetY()

        item, flags = self.HitTest((x, y))

        if item != wx.NOT_FOUND and flags & wx.LIST_HITTEST_ONITEM:
            self.Select(item)

        #------------

        # Tell the event system to continue
        # looking for an event handler, so the
        # default handler will get called.
        event.Skip()
        

    def OnColClick(self, event):
        """
        Column click.
        """

        count = self.GetItemCount()
        self.sortedEmployees = [self.GetItem(row, col=0).GetText() for row in range(count)]
        
        #------------

        # Tell the event system to continue
        # looking for an event handler, so the
        # default handler will get called.
        event.Skip()


    def OnSort(self, event):
        """
        Sort column.
        """

        idx = event.GetColumn()


    def OnColRightClick(self, event):
        """
        Column right click.
        """
        
        item = self.GetColumn(event.GetColumn())
        
        #------------

        if self.HasColumnOrderSupport():
            print("... Column order : %d" %
                  (self.GetColumnOrder(event.GetColumn())))


    def OnColBeginDrag(self, event):
        """
        Show how to not allow a column to be resized.
        """
        
        if event.GetColumn() == 0:
            event.Veto()

#-------------------------------------------------------------------------------
        
class MyFrame(wx.Frame):
    """
    ...
    """
    def __init__(self, parent, id, title, 
                 style=wx.DEFAULT_FRAME_STYLE |
                       wx.NO_FULL_REPAINT_ON_RESIZE |
                       wx.CLIP_CHILDREN):
        super(MyFrame, self).__init__(parent=None,
                                      id=-1,
                                      title=title,
                                      style=style)
        
        #------------

        # Returns application name.
        self.app_name = wx.GetApp().GetAppName() 
        # Returns bitmaps folder.
        self.bitmaps_dir = wx.GetApp().GetBitmapsDir()
        # Returns icons folder.
        self.icons_dir = wx.GetApp().GetIconsDir()

        #------------

        # Simplified init method.
        self.ConnectDb()
        self.SetProperties()
        self.MakeMenuBar()
        self.MakeStatusBar()
        self.CreateCtrls()
        self.BindEvents()
        self.DoLayout()

        #------------

        # Clock.
        self.OnTimer(None)
        
        self.timer = wx.Timer(self)
        self.timer.Start(3000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)

    #---------------------------------------------------------------------------

    def ConnectDb(self):
        """
        Connection to the database. 
        """

        # Instance from Class MyConnection.       
        self.con = MyConnection()

        
    def SetProperties(self):
        """
        Set the frame properties (title, icon, size...).
        """

        # Setting some frame properties.
        frameIcon = wx.Icon(os.path.join(self.icons_dir,
                                         "icon_wxWidgets.ico"),
                            type=wx.BITMAP_TYPE_ICO)
        self.SetIcon(frameIcon)

        #------------
        
        # Frame cursor.
        cursorHand = wx.Cursor(os.path.join(self.icons_dir,
                                            "hand.cur"),
                               type=wx.BITMAP_TYPE_CUR)
        self.SetCursor(cursorHand)
        
        #------------
        
        self.SetTitle(("%s") % (self.app_name))
        

    def MakeMenuBar(self):
        """
        Create the menu bar for my app.
        """

        # Set an icon to the exit/about menu item.
        emptyImg = wx.Bitmap(os.path.join(self.bitmaps_dir,
                                          "item_empty.png"),
                             type=wx.BITMAP_TYPE_PNG)
        
        exitImg = wx.Bitmap(os.path.join(self.bitmaps_dir,
                                         "item_exit.png"),
                            type=wx.BITMAP_TYPE_PNG)

        helpImg = wx.Bitmap(os.path.join(self.bitmaps_dir,
                                         "item_about.png"),
                            type=wx.BITMAP_TYPE_PNG)

        #------------
        
        # menu.
        mnuFile = wx.Menu()
        mnuInfo = wx.Menu()

        # mnuFile.
        # Show how to put an icon in the menu item.
        menuItem1 = wx.MenuItem(mnuFile, -1, "W&IT\tCtrl+Alt+I", "Widget Inspection Tool !")
        menuItem1.SetBitmap(emptyImg)
        mnuFile.Append(menuItem1)
        self.Bind(wx.EVT_MENU, self.OnOpenWidgetInspector, menuItem1)
        
        # Show how to put an icon in the menu item.
        menuItem2 = wx.MenuItem(mnuFile, wx.ID_EXIT, "&Quit\tCtrl+Q", "Close !")
        menuItem2.SetBitmap(exitImg)
        mnuFile.Append(menuItem2)
        self.Bind(wx.EVT_MENU, self.OnExit, menuItem2)

        # mnuInfo.
        # Show how to put an icon in the menu item.
        menuItem2 = wx.MenuItem(mnuInfo, wx.ID_ABOUT, "A&bout\tCtrl+A", "Info about developers !")
        menuItem2.SetBitmap(helpImg)
        mnuInfo.Append(menuItem2)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuItem2)

        # menuBar.
        menubar = wx.MenuBar()

        # Add menu voices.
        menubar.Append(mnuFile, "&File")
        menubar.Append(mnuInfo, "I&nfo")
        
        self.SetMenuBar(menubar)


    def MakeStatusBar(self):  
        """
        Create the status bar for my frame.
        """
        
        # Statusbar.
        self.myStatusBar = self.CreateStatusBar(1)
        self.myStatusBar.SetFieldsCount(2)
        self.myStatusBar.SetStatusWidths([-8, -4])
        self.myStatusBar.SetStatusText("", 0)
        self.myStatusBar.SetStatusText("Python-it.org.", 1)


    def CreateCtrls(self):
        """
        Create some controls for my frame.
        """

        # Font style for wx.StaticText.
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetWeight(wx.BOLD)

        #------------
        
        # Widgets.
        self.panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
   
        self.stEmployees = wx.StaticText(self.panel, -1, "Employees list :")
        self.stEmployees.SetForegroundColour("gray")
        self.stEmployees.SetFont(font)
       
        self.listCtrl = MyListCtrl(self.panel,
                                   id=ID_LIST,
                                   style=wx.LC_REPORT |
                                         wx.LC_SINGLE_SEL |
                                         wx.LC_VRULES |
                                         wx.BORDER_SUNKEN)
        
        self.stSearch = wx.StaticText(self.panel, -1, 'Search "Surname :')
        self.txSearch = wx.TextCtrl(self.panel, -1, "", size=(100, -1))
        self.txSearch.SetToolTip("Search employee !")

        self.StaticSizer = wx.StaticBox(self.panel, -1, "Commands :")
        self.StaticSizer.SetForegroundColour("red")
        self.StaticSizer.SetFont(font)
        
        self.bntSearch = wx.Button(self.panel, -1, "&Search")
        self.bntSearch.SetToolTip("Search employee !")

        self.bntClear = wx.Button(self.panel, -1, "&Clear")
        self.bntClear.SetToolTip("Clear the search text !")

        self.bntShowAll = wx.Button(self.panel, -1, "&All")
        self.bntShowAll.SetToolTip("Show all !")

        self.bntNew = wx.Button(self.panel, -1, "&Insert")
        self.bntNew.SetToolTip("Insert a new employee !")
        
        self.bntEdit = wx.Button(self.panel, -1, "&Update")
        self.bntEdit.SetToolTip("Update selected employee !")

        self.bntDelete = wx.Button(self.panel, -1, "&Delete")
        self.bntDelete.SetToolTip("Delete selected employee !")

        self.bntClose = wx.Button(self.panel, -1, "&Quit")
        self.bntClose.SetToolTip("Close !")   


    def BindEvents(self):
        """
        Bind all the events related to my frame.
        """

        self.txSearch.Bind(wx.EVT_TEXT, self.OnUpperCaseText)
        
        self.Bind(wx.EVT_BUTTON, self.OnSearch, self.bntSearch)
        self.Bind(wx.EVT_BUTTON, self.OnClear, self.bntClear)        
        self.Bind(wx.EVT_BUTTON, self.OnShowAll, self.bntShowAll)
        self.Bind(wx.EVT_BUTTON, self.OnNew, self.bntNew)        
        self.Bind(wx.EVT_BUTTON, self.OnEdit, self.bntEdit)
        self.Bind(wx.EVT_BUTTON, self.OnDelete, self.bntDelete)
        self.Bind(wx.EVT_BUTTON, self.OnExit, self.bntClose)

        self.Bind(wx.EVT_CLOSE, self.OnExit)
      

    def DoLayout(self):
        """
        Do layout.
        """

        # Sizer.
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        textSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.StaticBoxSizer(self.StaticSizer, wx.VERTICAL)

        # Assign widgets to sizers.
        
        # textSizer.
        textSizer.Add(self.stEmployees, 0, wx.BOTTOM, 5)
        textSizer.Add(self.listCtrl, 1, wx.EXPAND)

        # btnSizer.
        btnSizer.Add(self.stSearch)
        btnSizer.Add(self.txSearch)
        btnSizer.Add((5, 5), -1)
        btnSizer.Add(self.bntSearch, 0, wx.ALL, 5)
        btnSizer.Add((5, 5), -1)
        btnSizer.Add(self.bntClear, 0, wx.ALL, 5)
        btnSizer.Add((5, 5), -1)
        btnSizer.Add(self.bntShowAll, 0, wx.ALL, 5)
        btnSizer.Add((5, 5), -1)
        btnSizer.Add(self.bntNew, 0, wx.ALL, 5)
        btnSizer.Add((5, 5), -1)
        btnSizer.Add(self.bntEdit, 0, wx.ALL, 5)
        btnSizer.Add((5, 5), -1)
        btnSizer.Add(self.bntDelete, 0, wx.ALL, 5)
        btnSizer.Add((5, 5), -1)
        btnSizer.Add(self.bntClose, 0, wx.ALL, 5)

        # Assign to mainSizer the other sizers.  
        mainSizer.Add(textSizer, 1, wx.ALL | wx.EXPAND, 10)  
        mainSizer.Add(btnSizer, 0, wx.ALL, 10)

        # Assign to panel the mainSizer.
        self.panel.SetSizer(mainSizer)             
        mainSizer.Fit(self)
        # mainSizer.SetSizeHints(self)      
         
        
    def OnDelete(self, event):
        """
        ...
        """
        
        global iEmployees
        
        # It means that we haven't select a record.  
        if iEmployees ==0:
             wx.MessageBox("ATTENTION !\nSelect an employee !",
                           AppTitle,
                           wx.OK | wx.ICON_INFORMATION)
             
             return

        else:
            # Ask for delete.
            sMessage = "Delete selected employee ? %s " %(iEmployees)
            dlgAsk = wx.MessageDialog(None,
                                      sMessage,
                                      AppTitle,
                                      wx.YES_NO | wx.ICON_QUESTION)
            
            retCode = dlgAsk.ShowModal()
            
            if (retCode == wx.ID_YES):
                
                sSQL = "DELETE FROM Employees WHERE EmployeeID = ?"
                self.con.OnQueryParameter(sSQL, iEmployees)

                self.OnShowAll(self)
                
                wx.MessageBox("Delete operation terminate !",
                              AppTitle,
                              wx.OK | wx.ICON_INFORMATION)
            
            elif (retCode == wx.ID_NO):
                wx.MessageBox("Delete operation aborted !",
                              AppTitle,
                              wx.OK | wx.ICON_INFORMATION)
     
            dlgAsk.Destroy()
            
    
    def OnUpdateList(self):
        """
        ...
        """
   
        self.OnShowAll(self)
        
        
    def OnShowAll(self, event):
        """
        ...
        """

        wx.BeginBusyCursor()
        
        sSQL = "SELECT * FROM Employees WHERE EmployeeID LIKE ? "
        sSearch = "%"
        
        self.listCtrl.OnRetrieveData(sSQL, sSearch)

        self.myStatusBar.SetStatusText("Python-it.org.", 1)

        self.OnClear(self)

        wx.CallAfter(wx.EndBusyCursor)
        

    def OnClear(self, event):
        """
        ...
        """
        
        global iEmployees
        
        sSQL = "SELECT * FROM Employees WHERE EmployeeID LIKE ? "
        sSearch = "%"
        
        self.listCtrl.OnRetrieveData(sSQL, sSearch)
    
        self.txSearch.Clear()
        self.txSearch.SetFocus()

        iEmployees = 0
        

    def OnSearch(self, event):
        """
        ...
        """
        
        # Retrieve what we have write.
        sSearch = str(self.txSearch.GetValue())
        
        # Remove spaces.
        # sSearch = "".join(sSearch.strip().split())
        
        # Add & symbol to force the search.
        sSearch = sSearch+"%"
        
        # Control if we have write something
        # before launch the research.
        if sSearch == "%" :
                wx.MessageBox("ATTENTION !\nThe search text is empty !",
                              AppTitle,
                              wx.OK | wx.ICON_INFORMATION)
                
                self.txSearch.SetFocus()
                
                return
            
        else:
            sSQL = "SELECT * FROM Employees WHERE Surname LIKE ? "
            self.listCtrl.OnRetrieveData(sSQL, sSearch)
            
       
    def OnEdit(self, event):
        """
        ...
        """
        
        global iEmployees
        
        # It means that we haven't select an employee.  
        if iEmployees ==0:
             wx.MessageBox("ATTENTION !\nSelect an employee !",
                           AppTitle,
                           wx.OK | wx.ICON_INFORMATION)
             
             return

        else:  
            sSQL = "SELECT * FROM Employees WHERE EmployeeID = ?"
            self.OnOpenEdit(sSQL, iEmployees)


    def OnNew(self, event):
        """
        ...
        """
                    
        # Create an instance of the Child_Frame.
        self.dlgInsert = self.dlgInsert = MyInsertDlg(caller_dlgInsert=self)
            
        sTitle = "Insert new employee"
        self.dlgInsert.SetTitle(sTitle)
        self.dlgInsert.CenterOnParent(wx.BOTH)
        self.dlgInsert.ShowModal()
        self.dlgInsert.Destroy()

            
    def OnOpenEdit(self, sSQL, sParameter):
        """
        ...
        """
        
        # Retrieve data for the selected product.
        rsEmployees = self.con.OnQueryParameter(sSQL, sParameter)
            
        # Create an instance of the Child_Frame.
        self.dlgEdit = self.dlgEdit = MyUpdateDlg(caller_dlgUpdate=self)
            
        # Populate the fields of the frame with the recordset.
        for i in rsEmployees:
            self.dlgEdit.txEmployeeID.SetValue(str(i[0]))
            self.dlgEdit.txSurname.SetValue(str(i[1]))
            self.dlgEdit.txFirstname.SetValue(str(i[2]))
            self.dlgEdit.txPhone1.SetValue(str(i[3][0:2]))
            self.dlgEdit.txPhone2.SetValue(str(i[3][3:5]))
            self.dlgEdit.txPhone3.SetValue(str(i[3][6:8]))
            self.dlgEdit.txPhone4.SetValue(str(i[3][9:11]))
            self.dlgEdit.txPhone5.SetValue(str(i[3][12:14]))              
            self.dlgEdit.txEmail.SetValue(str(i[4]))
                
            # We use this for the title of the frame.
            sEmployees =(str(i[1]))              

        sTitle = "Select employee : %s" %(sEmployees)
        self.dlgEdit.SetTitle(sTitle)
        self.dlgEdit.CenterOnParent(wx.BOTH)
        self.dlgEdit.ShowModal()
        self.dlgEdit.Destroy()
            

    def OnUpperCaseText(self, event):        
        """
        ...
        """

        # Write in upper mode on widgets the call it.        
        # Adapted from a script of David Hughes
        # Forestfield Software. 
        # Retrive the widget.
        wdgControl = event.GetEventObject()

        # Retrive what we have write.       
        retValue = wdgControl.GetValue()

        # Upper it.
        upValue = retValue.upper()

        if retValue != upValue:
            wdgControl.SetValue(upValue)
            # Insert it at the end.
            wdgControl.SetInsertionPointEnd()

        event.Skip()


    def OnOpenWidgetInspector(self, event):
        """
        Activate the widget inspection tool,
        giving it a widget to preselect in the tree.
        Use either the one under the cursor,
        if any, or this frame.
        """

        from wx.lib.inspection import InspectionTool
        wnd = wx.FindWindowAtPointer()
        if not wnd:
            wnd = self
        InspectionTool().Show(wnd, True)

        
    def OnAbout(self, event):
        """
        ...
        """

        # Returns SQLite version.
        sSQLversion = self.con.OnSqliteVersion()
           
        message = """Python-it.org\n
                     How to use a wx.ListCtrl.
                     Developed in wxPython by Guldo and Beppe.\n
                     Modified and updated for wxPython Phoenix by Ecco :-)\n
                     Have fun ! ---> Amusez-vous bien !\n
                     SQLite version : %s""" %(sSQLversion)

        wx.MessageBox(message,
                      AppTitle,
                      wx.OK)


    def OnClose(self):
        """
        ...
        """
            
        ret=wx.MessageBox("Do you want exit ?",
                          AppTitle,
                          wx.YES_NO |wx.ICON_QUESTION|
                          wx.CENTRE |wx.NO_DEFAULT)
        
        return ret

                    
    def OnExit(self, event):
        """
        ...
        """
        
        # Ask for exit.
        intChoice = self.OnClose()
        
        if intChoice == 2:
            # Disconnect from server.
            self.con.OnCloseDb()
            self.Destroy()


    def OnTimer(self, event):
        """
        ...
        """
        
        t = time.localtime(time.time())
        sbTime = time.strftime("Astral date %d/%m/%Y are %H:%M:%S", t)
        self.myStatusBar.SetStatusText(sbTime, 0)
    
#-------------------------------------------------------------------------------

class MyApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
    """
    Thanks to Andrea Gavana.
    """
    def OnInit(self):

        #------------

        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)

        #------------

        self.SetAppName("List of employees (v0.0.3) - Sort")

        #------------

        self.installDir = os.path.split(os.path.abspath(sys.argv[0]))[0]

        #------------

        # Simplified init method.            
        # For the InspectionMixin base class.
        self.InitInspection()      

        #------------
        
        frame = MyFrame(None, -1, title="")
        frame.SetSize(800, 527)
        self.SetTopWindow(frame)
        frame.Center()
        frame.Show(True)

        return True

    #---------------------------------------------------------------------------

    def GetInstallDir(self):
        """
        Returns the installation directory for my application.
        """

        return self.installDir
    
    
    def GetIconsDir(self):
        """
        Returns the icons directory for my application.
        """

        icons_dir = os.path.join(self.installDir, "icons")
        return icons_dir


    def GetBitmapsDir(self):
        """
        Returns the bitmaps directory for my application.
        """

        bitmaps_dir = os.path.join(self.installDir, "bitmaps")
        return bitmaps_dir


    def GetDatabaseDir(self):
        """
        Returns the database directory for my application.
        """

        if not os.path.exists("data"):
            # Create the data folder, it still doesn't exist.
            os.makedirs("data")
            
        database_dir = os.path.join(self.installDir, "data")
        return database_dir
        
#-------------------------------------------------------------------------------

def main():
    app = MyApp(redirect=False)
    app.MainLoop()

#-------------------------------------------------------------------------------

if __name__ == "__main__" :
    main()
