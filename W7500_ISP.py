# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import serial.tools.list_ports
import w7500_isp_cmd
import binascii
import hexeditor
import time
import os


def byte_to_binary(n):
    return ''.join(str((n & (1 << i)) and 1) for i in reversed(range(8)))

def hex_to_binary(h):
    return ''.join(byte_to_binary(ord(b)) for b in binascii.unhexlify(h))

###########################################################################
## Class W7500_ISP
###########################################################################


class W7500_ISP ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"W7500 ISP Tool", pos = wx.DefaultPosition, size = wx.Size( 561,722 ), style = wx.CAPTION|wx.DEFAULT_FRAME_STYLE|wx.FRAME_TOOL_WINDOW|wx.MAXIMIZE_BOX|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
        self.SetFont( wx.Font( 8, 74, 90, 90, False, "Verdana" ) )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer5.SetMinSize( wx.Size( 0,0 ) ) 
        gSizer3 = wx.GridSizer( 0, 0, 0, 0 )
        
        gSizer3.SetMinSize( wx.Size( 0,0 ) ) 
        sbSizer_Step1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Step 1 - Serial Option" ), wx.VERTICAL )
        
        sbSizer_Step1.SetMinSize( wx.Size( 0,0 ) ) 
        fgSizer4 = wx.FlexGridSizer( 0, 3, 0, 0 )
        fgSizer4.SetFlexibleDirection( wx.BOTH )
        fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText_serial_port = wx.StaticText( self, wx.ID_ANY, u"Serial Port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_serial_port.Wrap( -1 )
        fgSizer4.Add( self.m_staticText_serial_port, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        m_comboBox_serial_portChoices = []
        self.m_comboBox_serial_port = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_serial_portChoices, 0 )
        fgSizer4.Add( self.m_comboBox_serial_port, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        self.m_button_serial_refresh = wx.Button( self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        fgSizer4.Add( self.m_button_serial_refresh, 0, wx.ALL, 5 )
        
        self.m_staticText_baud_rate = wx.StaticText( self, wx.ID_ANY, u"Baud Rate", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_baud_rate.Wrap( -1 )
        fgSizer4.Add( self.m_staticText_baud_rate, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
        
        m_comboBox_baud_rateChoices = [ u"2400", u"9600", u"14400", u"19200", u"38400", u"57600", u"76800", u"115200", u"230400", u"460800" ]
        self.m_comboBox_baud_rate = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_baud_rateChoices, 0 )
        self.m_comboBox_baud_rate.SetSelection( 7 )
        fgSizer4.Add( self.m_comboBox_baud_rate, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        fgSizer4.AddSpacer( ( 0, 0), 1, 0, 5 )
        
        self.m_button_serial_open = wx.Button( self, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.Size( 0,0 ), 0 )
        self.m_button_serial_open.SetDefault() 
        fgSizer4.Add( self.m_button_serial_open, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        self.m_button_serial_close = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_serial_close.SetDefault() 
        self.m_button_serial_close.Enable( False )
        
        fgSizer4.Add( self.m_button_serial_close, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        
        fgSizer4.AddSpacer( ( 0, 0), 1, 0, 5 )
        
        
        sbSizer_Step1.Add( fgSizer4, 1, 0, 5 )
        
        
        gSizer3.Add( sbSizer_Step1, 0, wx.ALIGN_CENTER, 5 )
        
        sbSizer_Step2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Step 2 - Erase" ), wx.VERTICAL )
        
        sbSizer_Step2.SetMinSize( wx.Size( 0,0 ) ) 
        bSizer_Step2_Child = wx.BoxSizer( wx.VERTICAL )
        
        m_listBox_EraseBlockChoices = [ u"Erase Data  0 (0x0003FE00~0x0003FEFF)", u"Erase Data  1 (0x0003FF00~0x0003FFFF)", u"Erase Block 0 (0x00000000~0x00000FFF)", u"Erase Block 1 (0x00001000~0x00001FFF)", u"Erase Block 2 (0x00002000~0x00002FFF)", u"Erase Block 3 (0x00003000~0x00003FFF)", u"Erase Block 4 (0x00004000~0x00004FFF)", u"Erase Block 5 (0x00005000~0x00005FFF)", u"Erase Block 6 (0x00006000~0x00006FFF)", u"Erase Block 7 (0x00007000~0x00007FFF)", u"Erase Block 8 (0x00008000~0x00008FFF)", u"Erase Block 9 (0x00009000~0x00009FFF)", u"Erase Block10 (0x0000A000~0x0000AFFF)", u"Erase Block11 (0x0000B000~0x0000BFFF)", u"Erase Block12 (0x0000C000~0x0000CFFF)", u"Erase Block13 (0x0000D000~0x0000DFFF)", u"Erase Block14 (0x0000E000~0x0000EFFF)", u"Erase Block15 (0x0000F000~0x0000FFFF)", u"Erase Block16 (0x00010000~0x00010FFF)", u"Erase Block17 (0x00011000~0x00011FFF)", u"Erase Block18 (0x00012000~0x00012FFF)", u"Erase Block19 (0x00013000~0x00013FFF)", u"Erase Block20 (0x00014000~0x00014FFF)", u"Erase Block21 (0x00015000~0x00015FFF)", u"Erase Block22 (0x00016000~0x00016FFF)", u"Erase Block23 (0x00017000~0x00017FFF)", u"Erase Block24 (0x00018000~0x00018FFF)", u"Erase Block25 (0x00019000~0x00019FFF)", u"Erase Block26 (0x0001A000~0x0001AFFF)", u"Erase Block27 (0x0001B000~0x0001BFFF)", u"Erase Block28 (0x0001C000~0x0001CFFF)", u"Erase Block29 (0x0001D000~0x0001DFFF)", u"Erase Block30 (0x0001E000~0x0001EFFF)", u"Erase Block31 (0x0001F000~0x0001FFFF)" ]
        self.m_listBox_EraseBlock = wx.ListBox( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( -1,80 ), m_listBox_EraseBlockChoices, wx.LB_HSCROLL|wx.LB_MULTIPLE )
        self.m_listBox_EraseBlock.Enable( False )
        
        bSizer_Step2_Child.Add( self.m_listBox_EraseBlock, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_checkBox_erase_mass = wx.CheckBox( self, wx.ID_ANY, u"Erase Data Block All Code Block", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox_erase_mass.SetValue(True) 
        bSizer_Step2_Child.Add( self.m_checkBox_erase_mass, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_checkBox_erase_chip = wx.CheckBox( self, wx.ID_ANY, u"Erase All Code Block", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_Step2_Child.Add( self.m_checkBox_erase_chip, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        sbSizer_Step2.Add( bSizer_Step2_Child, 0, 0, 2 )
        
        
        gSizer3.Add( sbSizer_Step2, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer5.Add( gSizer3, 0, 0, 5 )
        
        sbSizer_Step3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Step 3 - Code Read Lock or Data R/W Lock" ), wx.VERTICAL )
        
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_checkBox_all_code_read_lock = wx.CheckBox( self, wx.ID_ANY, u"All Code Read Lock/Data R/W Lock", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox_all_code_read_lock.SetValue(True) 
        bSizer9.Add( self.m_checkBox_all_code_read_lock, 0, wx.ALL, 5 )
        
        self.m_checkBox_all_code_read_unlock = wx.CheckBox( self, wx.ID_ANY, u"All Code Read Unlock/Data R/W Unlock", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_checkBox_all_code_read_unlock, 0, wx.ALL, 5 )
        
        
        sbSizer_Step3.Add( bSizer9, 0, wx.ALL|wx.EXPAND, 5 )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_checkBox_crl = wx.CheckBox( self, wx.ID_ANY, u"Code Read", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_checkBox_crl, 0, wx.ALL, 5 )
        
        self.m_checkBox_cabwl = wx.CheckBox( self, wx.ID_ANY, u"Code All Block Write", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_checkBox_cabwl, 0, wx.ALL, 5 )
        
        
        sbSizer_Step3.Add( bSizer10, 0, wx.ALL|wx.EXPAND, 5 )
        
        bSizer92 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_checkBox_drl1 = wx.CheckBox( self, wx.ID_ANY, u"Data 1 Read", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer92.Add( self.m_checkBox_drl1, 0, wx.ALL, 5 )
        
        self.m_checkBox_drl0 = wx.CheckBox( self, wx.ID_ANY, u"Data 0 Read", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer92.Add( self.m_checkBox_drl0, 0, wx.ALL, 5 )
        
        self.m_checkBox_dwl1 = wx.CheckBox( self, wx.ID_ANY, u"Data 1 Write", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer92.Add( self.m_checkBox_dwl1, 0, wx.ALL, 5 )
        
        self.m_checkBox_dwl0 = wx.CheckBox( self, wx.ID_ANY, u"Data 0 Write", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer92.Add( self.m_checkBox_dwl0, 0, wx.ALL, 5 )
        
        
        sbSizer_Step3.Add( bSizer92, 1, wx.EXPAND, 5 )
        
        
        bSizer5.Add( sbSizer_Step3, 0, wx.ALL|wx.EXPAND, 5 )
        
        sbSizer_Step4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Step 4 - Code Write Lock" ), wx.VERTICAL )
        
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_checkBox_all_code_write_lock = wx.CheckBox( self, wx.ID_ANY, u"All Code Write Lock", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_checkBox_all_code_write_lock, 0, wx.ALL, 5 )
        
        self.m_checkBox_all_code_write_unlock = wx.CheckBox( self, wx.ID_ANY, u"All Code Write Unlock", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_checkBox_all_code_write_unlock, 0, wx.ALL, 5 )
        
        
        sbSizer_Step4.Add( bSizer11, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        sbSizer_code_write_block = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Block" ), wx.VERTICAL )
        
        gSizer8 = wx.GridSizer( 0, 16, 0, 0 )
        
        self.m_staticText_cwl31 = wx.StaticText( self, wx.ID_ANY, u"31", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl31.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl31, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
        
        self.m_staticText_cwl30 = wx.StaticText( self, wx.ID_ANY, u"30", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl30.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl30, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticText_cwl29 = wx.StaticText( self, wx.ID_ANY, u"29", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl29.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl29, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl28 = wx.StaticText( self, wx.ID_ANY, u"28", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl28.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl28, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl27 = wx.StaticText( self, wx.ID_ANY, u"27", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl27.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl27, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl26 = wx.StaticText( self, wx.ID_ANY, u"26", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl26.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl26, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl25 = wx.StaticText( self, wx.ID_ANY, u"25", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl25.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl24 = wx.StaticText( self, wx.ID_ANY, u"24", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl24.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl23 = wx.StaticText( self, wx.ID_ANY, u"23", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl23.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl23, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl22 = wx.StaticText( self, wx.ID_ANY, u"22", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl22.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl21 = wx.StaticText( self, wx.ID_ANY, u"21", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl21.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl20 = wx.StaticText( self, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl20.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl19 = wx.StaticText( self, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl19.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl18 = wx.StaticText( self, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl18.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl17 = wx.StaticText( self, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl17.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl16 = wx.StaticText( self, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl16.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl31 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl30 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl30, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl29 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl29, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl28 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl28, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl27 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl27, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl26 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl26, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl25 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl24 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl23 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl23, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl22 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl21 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl20 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl19 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl18 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl17 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl16 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl15 = wx.StaticText( self, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl15.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl14 = wx.StaticText( self, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl14.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl13 = wx.StaticText( self, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl13.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl12 = wx.StaticText( self, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl12.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl11 = wx.StaticText( self, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl11.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl10 = wx.StaticText( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl10.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl9 = wx.StaticText( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl9.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl8 = wx.StaticText( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl8.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl7 = wx.StaticText( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl7.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl6 = wx.StaticText( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl6.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl5 = wx.StaticText( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl5.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl4 = wx.StaticText( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl4.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl3 = wx.StaticText( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl3.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl2 = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl2.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl1 = wx.StaticText( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl1.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_cwl0 = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_cwl0.Wrap( -1 )
        gSizer8.Add( self.m_staticText_cwl0, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl15 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl14 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl13 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl12 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl11 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl10 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl9 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl8 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl7 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl6 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl5 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl4 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl3 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl2 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl1 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_checkBox_cwl0 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer8.Add( self.m_checkBox_cwl0, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer_code_write_block.Add( gSizer8, 0, wx.ALL|wx.FIXED_MINSIZE, 4 )
        
        
        sbSizer_Step4.Add( sbSizer_code_write_block, 0, wx.ALL|wx.FIXED_MINSIZE, 5 )
        
        
        bSizer5.Add( sbSizer_Step4, 0, wx.ALL, 5 )
        
        sbSizer_Step5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Step 5 - Select the binary file" ), wx.VERTICAL )
        
        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
        
        fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
        fgSizer5.SetFlexibleDirection( wx.BOTH )
        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText_Binary_File = wx.StaticText( self, wx.ID_ANY, u"Binary File :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Binary_File.Wrap( -1 )
        fgSizer5.Add( self.m_staticText_Binary_File, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_File_Path = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
        fgSizer5.Add( self.m_textCtrl_File_Path, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_browse = wx.Button( self, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_button_browse, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        bSizer14.Add( fgSizer5, 0, wx.EXPAND, 5 )
        
        
        sbSizer_Step5.Add( bSizer14, 0, wx.EXPAND|wx.ALL, 5 )
        
        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer15.SetMinSize( wx.Size( 0,0 ) ) 
        self.m_checkBox_verify = wx.CheckBox( self, wx.ID_ANY, u"Verify after programming", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox_verify.Enable( False )
        
        bSizer15.Add( self.m_checkBox_verify, 0, wx.ALL, 5 )
        
        self.m_checkBox_WriteMainFlash = wx.CheckBox( self, wx.ID_ANY, u"Write MainFlash", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox_WriteMainFlash.SetValue(True) 
        bSizer15.Add( self.m_checkBox_WriteMainFlash, 0, wx.ALL, 5 )
        
        self.m_checkBox_WriteDataFlash = wx.CheckBox( self, wx.ID_ANY, u"Write DataFlash", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.m_checkBox_WriteDataFlash, 0, wx.ALL, 5 )
        
        
        sbSizer_Step5.Add( bSizer15, 0, wx.EXPAND|wx.ALL, 1 )
        
        
        bSizer5.Add( sbSizer_Step5, 0, wx.ALL, 5 )
        
        bSizer91 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_button_Isp_start = wx.Button( self, wx.ID_ANY, u"ISP Start", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_button_Isp_start.SetFont( wx.Font( 12, 74, 90, 92, False, "Verdana" ) )
        self.m_button_Isp_start.SetMinSize( wx.Size( 300,-1 ) )
        
        bSizer91.Add( self.m_button_Isp_start, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        bSizer5.Add( bSizer91, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        self.SetSizer( bSizer5 )
        self.Layout()
        self.m_statusBar_W7500_Status = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu_file = wx.Menu()
        self.m_menu_file.AppendSeparator()
        
        self.m_menu2 = wx.Menu()
        self.m_menu_file.AppendSubMenu( self.m_menu2, u"&Quit\tCtrl+Q" )
        
        self.m_menubar1.Append( self.m_menu_file, u"&File" ) 
        
        self.m_menu_ISP = wx.Menu()
        self.m_menuItem_HexEditor = wx.MenuItem( self.m_menu_ISP, wx.ID_ANY, u"&HexEditor", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_ISP.AppendItem( self.m_menuItem_HexEditor )
        
        self.m_menu_Dump = wx.Menu()
        self.m_menuItem_MainFlashDump = wx.MenuItem( self.m_menu_Dump, wx.ID_ANY, u"&Main Flash Dump", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_Dump.AppendItem( self.m_menuItem_MainFlashDump )
        
        self.m_menuItem_Data_Dump = wx.MenuItem( self.m_menu_Dump, wx.ID_ANY, u"&Data Dump ", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_Dump.AppendItem( self.m_menuItem_Data_Dump )
        
        self.m_menu_ISP.AppendSubMenu( self.m_menu_Dump, u"&Dump" )
        
        self.m_menubar1.Append( self.m_menu_ISP, u"&ISP" ) 
        
        self.m_menu_help = wx.Menu()
        self.m_menubar1.Append( self.m_menu_help, u"Help" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        
        
        self.Centre( wx.VERTICAL )
        
        # Connect Events
        self.m_button_serial_refresh.Bind( wx.EVT_BUTTON, self.onRefresh )
        self.m_button_serial_open.Bind( wx.EVT_BUTTON, self.onSerialOpen )
        self.m_button_serial_close.Bind( wx.EVT_BUTTON, self.onSerialClose )
        self.m_checkBox_erase_mass.Bind( wx.EVT_CHECKBOX, self.onCheckEraseMass )
        self.m_checkBox_erase_chip.Bind( wx.EVT_CHECKBOX, self.onCheckEraseChip )
        self.m_checkBox_all_code_read_lock.Bind( wx.EVT_CHECKBOX, self.onAllCodeReadLock )
        self.m_checkBox_all_code_read_unlock.Bind( wx.EVT_CHECKBOX, self.onAllCodeReadUnlock )
        self.m_checkBox_all_code_write_lock.Bind( wx.EVT_CHECKBOX, self.onAllCodeWriteLock )
        self.m_checkBox_all_code_write_unlock.Bind( wx.EVT_CHECKBOX, self.onAllCodeWriteUnlock )
        self.m_button_browse.Bind( wx.EVT_BUTTON, self.onBrowse )
        self.m_checkBox_WriteMainFlash.Bind( wx.EVT_CHECKBOX, self.onWriteMainFlash )
        self.m_checkBox_WriteDataFlash.Bind( wx.EVT_CHECKBOX, self.onWriteDataFlash )
        self.m_button_Isp_start.Bind( wx.EVT_BUTTON, self.onISP_Start )
        self.Bind( wx.EVT_MENU, self.onHexEditor, id = self.m_menuItem_HexEditor.GetId() )
        self.Bind( wx.EVT_MENU, self.onFlashDump, id = self.m_menuItem_MainFlashDump.GetId() )
        self.Bind( wx.EVT_MENU, self.onDataDump, id = self.m_menuItem_Data_Dump.GetId() )

        
        #USER CODE
        self.GetComPortList()


        
    def __del__( self ):
        if self.isopen == 1:
            self.isp.__del__()
    
    # Virtual event handlers, overide them in your derived class
    def onRefresh( self, event ):
        self.GetComPortList()
         
    def onSerialOpen( self, event ):
        self.m_statusBar_W7500_Status.SetStatusText("W7500 ISP is Auto Negotiating....")
        
        com = self.m_comboBox_serial_port.GetValue()
        baud = int(self.m_comboBox_baud_rate.GetValue())
        if com =='':
            wx.MessageBox("Please Select Serial Port", 'Warning',wx.OK | wx.ICON_ERROR)
            return
        
        self.isp = w7500_isp_cmd.W7500_ISP_CMD(com,baud,self,1)
        if( self.isp.negoComP() == -1 ):
            self.isp.__del__()
            wx.MessageBox("Serial Open Error.\r\nPlease check BOOT pin and retry after reset the W7500 board", 'Warning',wx.OK | wx.ICON_ERROR)
            return
        
        #Check Lock Info
        self.checkbox_flockr0_list = [self.m_checkBox_crl,self.m_checkBox_cabwl,self.m_checkBox_drl1,self.m_checkBox_drl0,self.m_checkBox_dwl1,self.m_checkBox_dwl0]

        self.checkbox_flockr1_list  = [self.m_checkBox_cwl31,self.m_checkBox_cwl30,self.m_checkBox_cwl29,self.m_checkBox_cwl28,self.m_checkBox_cwl27,self.m_checkBox_cwl26,self.m_checkBox_cwl25,self.m_checkBox_cwl24]
        self.checkbox_flockr1_list += [self.m_checkBox_cwl23,self.m_checkBox_cwl22,self.m_checkBox_cwl21,self.m_checkBox_cwl20,self.m_checkBox_cwl19,self.m_checkBox_cwl18,self.m_checkBox_cwl17,self.m_checkBox_cwl16]
        self.checkbox_flockr1_list += [self.m_checkBox_cwl15,self.m_checkBox_cwl14,self.m_checkBox_cwl13,self.m_checkBox_cwl12,self.m_checkBox_cwl11,self.m_checkBox_cwl10,self.m_checkBox_cwl9,self.m_checkBox_cwl8]
        self.checkbox_flockr1_list += [self.m_checkBox_cwl7,self.m_checkBox_cwl6,self.m_checkBox_cwl5,self.m_checkBox_cwl4,self.m_checkBox_cwl3,self.m_checkBox_cwl2,self.m_checkBox_cwl1,self.m_checkBox_cwl0]

        self.isp.writeCmd("","3")
        result = self.isp.writeCmd("LOCK READ").split()

        str_flockr1 = result.pop()
        str_flockr0 = result.pop()

        bin_flockr1 = hex_to_binary(str_flockr1)
        bin_flockr0 = hex_to_binary(str_flockr0)

        for idx in range(len(self.checkbox_flockr1_list)):
            if( (bin_flockr1[idx]) == '1') :
                self.checkbox_flockr1_list[idx].SetValue(True)
            else:
                self.checkbox_flockr1_list[idx].SetValue(False)

        for idx in range(len(self.checkbox_flockr0_list)):
            if(idx < 2):
                if( bin_flockr0[idx] == '1'):
                    self.checkbox_flockr0_list[idx].SetValue(True)
                else:
                    self.checkbox_flockr0_list[idx].SetValue(False)
            else:
                if( bin_flockr0[idx+26] == '1' ):
                    self.checkbox_flockr0_list[idx].SetValue(True)
                else:
                    self.checkbox_flockr0_list[idx].SetValue(False)

        self.m_button_serial_open.Disable()
        self.m_button_serial_close.Enable()
        self.isopen = True
        self.m_statusBar_W7500_Status.SetStatusText("Serial Open Complete")

    
    def onSerialClose( self, event ):
        self.isp.writeCmd("REST",'8')
        
        self.isp.__del__()
        self.m_button_serial_open.Enable()
        self.m_button_serial_close.Disable()
        self.isopen = False

    def onCheckEraseMass( self, event ):
        self.m_checkBox_erase_chip.SetValue(False)
        self.m_checkBox_erase_mass.SetValue(True)


    def onCheckEraseChip( self, event ):
        self.m_checkBox_erase_mass.SetValue(False)
        self.m_checkBox_erase_chip.SetValue(True)


    def onAllCodeReadLock( self, event ):
        self.m_checkBox_all_code_read_unlock.SetValue(False)
        for idx in range(len(self.checkbox_flockr0_list)):
            self.checkbox_flockr0_list[idx].SetValue(True)
            
    
    def onAllCodeReadUnlock( self, event ):
        self.m_checkBox_all_code_read_lock.SetValue(False)
        for idx in range(len(self.checkbox_flockr0_list)):
            self.checkbox_flockr0_list[idx].SetValue(False)
            
    
    def onAllCodeWriteLock( self, event ):
        self.m_checkBox_all_code_write_unlock.SetValue(False)
        for idx in range(len(self.checkbox_flockr1_list)):
            self.checkbox_flockr1_list[idx].SetValue(True)
        
    
    def onAllCodeWriteUnlock( self, event ):
        self.m_checkBox_all_code_write_lock.SetValue(False)
        for idx in range(len(self.checkbox_flockr1_list)):
            self.checkbox_flockr1_list[idx].SetValue(False)
        
    
    def onBrowse( self, event ):
        filename = ''
        dlg = wx.FileDialog(self, message='Choose a file')
        
        if dlg.ShowModal() == wx.ID_OK:
            #get the new filename from the dialog
            filename = dlg.GetPath()
        dlg.Destroy() #
        
        if filename:
            self.m_textCtrl_File_Path.SetValue(filename)

    def onWriteMainFlash( self, event ):
        self.m_checkBox_WriteDataFlash.SetValue(False)
        self.m_checkBox_WriteMainFlash.SetValue(True)
    
    def onWriteDataFlash( self, event ):
        self.m_checkBox_WriteMainFlash.SetValue(False)
        self.m_checkBox_WriteDataFlash.SetValue(True)
        
    def onISP_Start( self, event ):
        str = ''
        bin_flockr1=list('00000000000000000000000000000000')
        bin_flockr0=list('00000000000000000000000000000000')
        hex_flockr1=''
        hex_flockr0=''
        
        if self.isopen != True:
            wx.MessageBox("Serial is not opened", 'Warning',wx.OK | wx.ICON_ERROR)
            
        #Set Lock Information
        for idx in range(len(self.checkbox_flockr1_list)):
            if(self.checkbox_flockr1_list[idx].IsChecked()):
                bin_flockr1[idx] = '1'
            else:
                bin_flockr1[idx] = '0'
         
        for idx in range(len(self.checkbox_flockr0_list)):
            if(idx < 2):
                if( self.checkbox_flockr0_list[idx].IsChecked() ):
                    bin_flockr0[idx] = '1'
                else:
                    bin_flockr0[idx] = '0'
            else:
                if( self.checkbox_flockr0_list[idx].IsChecked() ):
                    bin_flockr0[idx+26] = '1'
                else:
                    bin_flockr0[idx+26] = '0'

        hex_flockr0 = hex(int("".join(bin_flockr0),2))[2:10]
        hex_flockr1 = hex(int("".join(bin_flockr1),2))[2:10]
        cmd = "LOCK PROG" + " " + hex_flockr0.zfill(8) + " " + hex_flockr1.zfill(8)
        resp = self.isp.writeCmd(cmd)
        if( resp[0] != '0'):
            msg_error = "ERROR LOCK PROG : " + resp
            wx.MessageBox(msg_error, 'Warning',wx.OK | wx.ICON_ERROR)
            return
        #Set Lock Information
        
        if self.m_checkBox_erase_mass.IsChecked():
            ret = self.isp.writeCmd("ERAS MASS")
            if ret[0] != '0':
                msg_error = 'ERROR MASS ERASE '
                msg_error += ret
                wx.MessageBox(msg_error, 'Warning',wx.OK | wx.ICON_ERROR)
                return
        
        if self.m_checkBox_erase_chip.IsChecked():
            ret = self.isp.writeCmd("ERAS CHIP")
            if ret[0] != '0':
                msg_error = 'ERROR CHIP ERASE '
                msg_error += ret
                wx.MessageBox(msg_error, 'Warning',wx.OK | wx.ICON_ERROR)
                return
                
        filename = self.m_textCtrl_File_Path.GetValue()
        if filename == '':
            return
        
        if filename.find('.bin') == -1:
            msg_error = "It can use only binary format file.\r\nPlease check your binary file."
            wx.MessageBox(msg_error, 'Warning',wx.OK | wx.ICON_ERROR)
            return
            
        self.isp.Xmodem_init()
        if self.m_checkBox_WriteMainFlash.IsChecked():
            if os.stat(filename).st_size > (128 * 1024):
                msg_error = "File size is over."
                wx.MessageBox(msg_error, 'Warning',wx.OK | wx.ICON_ERROR)
                return
                
            
            self.xmodemDialog = wx.ProgressDialog('W7500 Firmware Writing','Loading Memory', 1024, style= wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME | wx.PD_AUTO_HIDE )
            self.isp.Xmodem_Send("00000000", "00020000", filename, self.xmodem_callback)
            self.xmodemDialog.Destroy()

            wx.MessageBox("Download Complete", 'W7500ISP',wx.OK | wx.ICON_INFORMATION)

            self.isp.writeCmd("REMP FLSH")
            self.isp.writeCmd("REST")

            self.isp.__del__()
            self.m_button_serial_open.Enable()
            self.m_button_serial_close.Disable()
            self.isopen = False

        elif self.m_checkBox_WriteDataFlash.IsChecked():
            f = open(filename,"rb")

            if os.stat(filename).st_size > 512 :
                f.close()
                msg_error = "File size is over. It can use only 512byte file."
                wx.MessageBox(msg_error, 'Warning',wx.OK | wx.ICON_ERROR)
                return
            
            #Write to DAT0
            self.isp.writeCmd("DOWN 20000000 00000200","0",1,0) #512Byte
            for i in range(512):
                self.isp.ser.write(f.read())
            resp = self.isp.ser.readline()
            if resp[0] != '0' :
                f.close()
                msg_error = "[ERROR] Write to SRAM"
                wx.MessageBox(msg_error, 'Warning',wx.OK | wx.ICON_ERROR)
                return

            resp = self.isp.writeCmd("PROG DAT0 20000000")
            if resp[0] != '0' :
                f.close()
                msg_error = "[ERROR] Write DAT0"
                wx.MessageBox(msg_error, 'Warning',wx.OK | wx.ICON_ERROR)
                return
            
            #Write to DAT1
            resp = self.isp.writeCmd("PROG DAT1 20000100")
            if resp[0] != '0' :
                f.close()
                msg_error = "[ERROR] Write DAT1"
                wx.MessageBox(msg_error, 'Warning',wx.OK | wx.ICON_ERROR)
                return
        

    def onHexEditor( self, event ):
        dlg = hexeditor.HexEditorDialog()
        dlg.ShowModal()
        dlg.Destroy()
       
    
    def onFlashDump( self, event ):
        if self.isopen != 1:
            wx.MessageBox("Serial is not open.", 'Warning',wx.OK | wx.ICON_ERROR)
            return
        
        print 'test'
        progressMax = 32768 + 1         # (128K / 4) + 1
        filename = 'main_flash.bin'

        
        # count 32
        cmd_addr_list  = ['00000000','00000800','00001000','00001800','00002000','00002800','00003000','00003800','00004000','00004800']
        cmd_addr_list += ['00005000','00005800','00006000','00006800','00007000','00007800','00008000','00008800','00009000','00009800']
        cmd_addr_list += ['0000A000','0000A800','0000B000','0000B800','0000C000','0000C800','0000D000','0000D800','0000E000','0000E800','0000F000','0000F800']
        cmd_addr_list += ['00010000','00010800','00011000','00011800','00012000','00012800','00013000','00013800','00014000','00014800']
        cmd_addr_list += ['00015000','00015800','00016000','00016800','00017000','00017800','00018000','00018800','00019000','00019800']
        cmd_addr_list += ['0001A000','0001A800','0001B000','0001B800','0001C000','0001C800','0001D000','0001D800','0001E000','0001E800','0001F000','0001F800']
        loopcnt = 0
 
        progressDialog = wx.ProgressDialog('W7500 Flash Dump','Loading Memory', progressMax,
                                           style= wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME )
 
        f = open(filename,"wb")
        try:
            for i in range(64):
                cmd = "DUMP" + " " + cmd_addr_list[i] + " " + "00000800" + "\r"
                self.isp.ser.write(cmd)
                binary = []
                
                time.sleep(0.3)
                for j in range(512):
                    loopcnt = loopcnt + 1
                    respData = self.isp.ser.readline()
                    print respData
                    
                    if len(respData) != 19:
                        f.close()
                        progressDialog.Destroy() 
                        wx.MessageBox("[ERROR:200] Flash Dump ", 'Warning',wx.OK | wx.ICON_ERROR)
                        return
                    else:
                        little_enddian = ""
                        little_enddian = respData[15:17] + respData[13:15] + respData[11:13] + respData[9:11]
                        binary.append(binascii.a2b_hex(little_enddian))
                     
                progressDialog.Update(loopcnt)
                for cnt in range(len(binary)):
                    f.write(binary[cnt])
                
                respData = self.isp.ser.readline()
                if respData[:2] != '0\r':
                    f.close()
                    wx.MessageBox("[ERROR:201] Flash Dump Command Error ", 'Warning',wx.OK | wx.ICON_ERROR)
                    return
            
            f.close()
            progressDialog.Destroy() 
 
        except ValueError:
            f.close()
            wx.MessageBox("[ERROR:202] Data Flash Dump Error ", 'Warning',wx.OK | wx.ICON_ERROR)
            return
        
        dlg = hexeditor.HexEditorDialog()
        dlg.OpenFile(filename)
        dlg.ShowModal()
        dlg.Destroy()

    def onDataDump( self, event ):
        if self.isopen != 1:
            wx.MessageBox("Serial is not open.", 'Warning',wx.OK | wx.ICON_ERROR)
            return
        
        progressMax = 128 + 1         # (512B / 4) + 1
        filename = 'data_flash.bin'

        progressDialog = wx.ProgressDialog('W7500 Flash Dump','Loading Memory', progressMax,
                                           style= wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME )

        cmd = "DUMP 0003FE00 00000200" + "\r"
        print "Send Command : %s" % cmd
        self.isp.ser.write(cmd)
        f = open(filename,"wb")
        
        time.sleep(1)
        for i in range(progressMax):
            respData = self.isp.ser.readline()

            little_enddian = ""
            little_enddian = respData[15:17] + respData[13:15] + respData[11:13] + respData[9:11]
            binary = binascii.a2b_hex(little_enddian)
            
            #binary = binascii.a2b_hex(respData[9:17])
            f.write(binary)
            progressDialog.Update(i)
        
        f.close()        
        progressDialog.Destroy()

        dlg = hexeditor.HexEditorDialog()
        dlg.OpenFile(filename)
        dlg.ShowModal()
        dlg.Destroy()


    def xmodem_callback(self,total_packets, success_count, error_count):
        self.xmodemDialog.Update(success_count)
        
        
    def GetComPortList(self):
        comboBox_serial_portChoices = []
        self.ports_available = list(serial.tools.list_ports.comports())
        for self.port in self.ports_available:
            if(self.port[2] != 'n/a'):
                comboBox_serial_portChoices.append(self.port[0])
 
        self.m_comboBox_serial_port.SetItems(comboBox_serial_portChoices)
        


if __name__ == "__main__":
    app = wx.App(0)
    w7500_isp = W7500_ISP(None)
    app.SetTopWindow(w7500_isp)
    w7500_isp.Show()
    app.MainLoop()
    