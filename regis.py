import _winreg


key=_winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT,'Folder\\shell',0,_winreg.KEY_ALL_ACCESS)
n=_winreg.CreateKey(key,'NewMenu')
_winreg.SetValueEx(n,'SubCommands',0,_winreg.REG_SZ,'python.info')
_winreg.SetValueEx(n,'MUIVerb',0,_winreg.REG_SZ,'Download Subtitles')


key1=_winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommandStore\\shell',0,_winreg.KEY_ALL_ACCESS|_winreg.KEY_WOW64_64KEY)
n1=_winreg.CreateKeyEx(key1,'python.info',0,_winreg.KEY_ALL_ACCESS|_winreg.KEY_WOW64_64KEY)
_winreg.SetValueEx(n1,None,0,_winreg.REG_SZ,'Are You Sure?')
n2=_winreg.CreateKeyEx(n1,'command',0,_winreg.KEY_ALL_ACCESS|_winreg.KEY_WOW64_64KEY)
_winreg.SetValueEx(n2,None,0,_winreg.REG_SZ,'python C:\Python27\subs.py %1')