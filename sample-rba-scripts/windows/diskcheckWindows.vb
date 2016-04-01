'diskcheck.vbs script returns disk details, including Name, Caption, File System Total Capacity(in GB), Free Space(in GB)

Set objSWbemLocator = CreateObject("WbemScripting.SWbemLocator")
Set objSWbemServices = objSWbemLocator.ConnectServer(".", "root\cimv2")
Set colSWbemObjectSet = objSWbemServices.ExecQuery("Select * from Win32_LogicalDisk where DriveType=3")

'Display results heading

WScript.Echo "Disk details:"
WScript.Echo "-----------------------------"

'Loop to display results details

For Each objSWbemObject in colSWbemObjectSet
	
	WScript.Echo "Name:"&CStr(objSWbemObject.Name)
	WScript.Echo "Caption:"&CStr(objSWbemObject.Caption)
	WScript.Echo "File System:"&CStr(objSWbemObject.FileSystem)
	WScript.Echo "Total Capacity(in GB):"&CStr(Round(Int(objSWbemObject.Size)/1073741824,2))
	WScript.Echo "Free Space(in GB):"&CStr(Round(Int(objSWbemObject.FreeSpace)/1073741824,2))
	WScript.Echo "-----------------------------"
Next