auto-checkIn

# 成大簽到退、嘉藥刷登入

# 成大簽到退:
需先下載 Chome Driver，將driver exe檔放到Python安裝目錄下。

AutoClockIn.py : 簽到退功能class

ClockIn.py : 簽到腳本，執行此腳本可自動簽到

ClockOut.py : 簽退腳本，執行此腳本可自動簽退

以上腳本僅單次執行，故需配合排程器。

Windows可自行設定工作排程器，Linux 則使用Crontab

# 嘉藥網路大學自動刷登入次數:
loop_signInOut.py : 執行此腳本，會無限自動登入登出，六秒一次
