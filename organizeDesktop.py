from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'AK':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)
                #Add the folder path & also create all the folders

extensions_folders = {
#No name
    'noname' : "C:/Users/Houcem/Desktop/AK/Other/Uncategorized",
#Audio
    '.aif' : "C:/Users/Houcem/Desktop/AK/Audio",
    '.cda' : "C:/Users/Houcem/Desktop/AK/Audio",
    '.mid' : "C:/Users/Houcem/Desktop/AK/Audio",
    '.midi' : "C:/Users/Houcem/Desktop/AK/Audio",
    '.mp3' : "C:/Users/Houcem/Desktop/AK/Audio",
    '.mpa' : "C:/Users/Houcem/Desktop/AK/Audio",
    '.ogg' : "C:/Users/Houcem/Desktop/AK/Audio",
    '.wav' : "C:/Users/Houcem/Desktop/AK/Audio",
    '.wma' : "C:/Users/Houcem/Desktop/AK/Audio",
    '.wpl' : "C:/Users/Houcem/Desktop/AK/Audio",
    '.m3u' : "C:/Users/Houcem/Desktop/AK/Audio",
#Text
    '.txt' : "C:/Users/Houcem/Desktop/AK/Text/TextFiles",
    '.doc' : "C:/Users/Houcem/Desktop/AK/Text/Microsoft/Word",
    '.docx' : "C:/Users/Houcem/Desktop/AK/Text/Microsoft/Word",
    '.odt ' : "C:/Users/Houcem/Desktop/AK/Text/TextFiles",
    '.pdf': "C:/Users/Houcem/Desktop/AK/Text/PDF",
    '.rtf': "C:/Users/Houcem/Desktop/AK/Text/TextFiles",
    '.tex': "C:/Users/Houcem/Desktop/AK/Text/TextFiles",
    '.wks ': "C:/Users/Houcem/Desktop/AK/Text/TextFiles",
    '.wps': "C:/Users/Houcem/Desktop/AK/Text/TextFiles",
    '.wpd': "C:/Users/Houcem/Desktop/AK/Text/TextFiles",
#Video
    '.3g2': "C:/Users/Houcem/Desktop/AK/Video",
    '.3gp': "C:/Users/Houcem/Desktop/AK/Video",
    '.avi': "C:/Users/Houcem/Desktop/AK/Video",
    '.flv': "C:/Users/Houcem/Desktop/AK/Video",
    '.h264': "C:/Users/Houcem/Desktop/AK/Video",
    '.m4v': "C:/Users/Houcem/Desktop/AK/Video",
    '.mkv': "C:/Users/Houcem/Desktop/AK/Video",
    '.mov': "C:/Users/Houcem/Desktop/AK/Video",
    '.mp4': "C:/Users/Houcem/Desktop/AK/Video",
    '.mpg': "C:/Users/Houcem/Desktop/AK/Video",
    '.mpeg': "C:/Users/Houcem/Desktop/AK/Video",
    '.rm': "C:/Users/Houcem/Desktop/AK/Video",
    '.swf': "C:/Users/Houcem/Desktop/AK/Video",
    '.vob': "C:/Users/Houcem/Desktop/AK/Video",
    '.wmv': "C:/Users/Houcem/Desktop/AK/Video",
#Images
    '.ai': "C:/Users/Houcem/Desktop/AK/Images",
    '.bmp': "C:/Users/Houcem/Desktop/AK/Images",
    '.gif': "C:/Users/Houcem/Desktop/AK/Images",
    '.ico': "C:/Users/Houcem/Desktop/AK/Images",
    '.jpg': "C:/Users/Houcem/Desktop/AK/Images",
    '.jpeg': "C:/Users/Houcem/Desktop/AK/Images",
    '.png': "C:/Users/Houcem/Desktop/AK/Images",
    '.ps': "C:/Users/Houcem/Desktop/AK/Images",
    '.psd': "C:/Users/Houcem/Desktop/AK/Images",
    '.svg': "C:/Users/Houcem/Desktop/AK/Images",
    '.tif': "C:/Users/Houcem/Desktop/AK/Images",
    '.tiff': "C:/Users/Houcem/Desktop/AK/Images",
    '.CR2': "C:/Users/Houcem/Desktop/AK/Images",
#Internet
    '.asp': "C:/Users/Houcem/Desktop/AK/Other/Internet",
    '.aspx': "C:/Users/Houcem/Desktop/AK/Other/Internet",
    '.cer': "C:/Users/Houcem/Desktop/AK/Other/Internet",
    '.cfm': "C:/Users/Houcem/Desktop/AK/Other/Internet",
    '.cgi': "C:/Users/Houcem/Desktop/AK/Other/Internet",
    '.pl': "C:/Users/Houcem/Desktop/AK/Other/Internet",
    '.css': "C:/Users/Houcem/Desktop/AK/Other/Internet",
    '.htm': "C:/Users/Houcem/Desktop/AK/Other/Internet",
    '.js': "C:/Users/Houcem/Desktop/AK/Other/Internet",
    '.jsp': "C:/Users/Houcem/Desktop/AK/Other/Internet",
    '.part': "C:/Users/Houcem/Desktop/AK/Other/Internet",
    '.php': "C:/Users/Houcem/Desktop/AK/Other/Internet",
    '.rss': "C:/Users/Houcem/Desktop/AK/Other/Internet",
    '.xhtml': "C:/Users/Houcem/Desktop/AK/Other/Internet",
#Compressed
    '.7z': "C:/Users/Houcem/Desktop/AK/Other/Compressed",
    '.arj': "C:/Users/Houcem/Desktop/AK/Other/Compressed",
    '.deb': "C:/Users/Houcem/Desktop/AK/Other/Compressed",
    '.pkg': "C:/Users/Houcem/Desktop/AK/Other/Compressed",
    '.rar': "C:/Users/Houcem/Desktop/AK/Other/Compressed",
    '.rpm': "C:/Users/Houcem/Desktop/AK/Other/Compressed",
    '.tar.gz': "C:/Users/Houcem/Desktop/AK/Other/Compressed",
    '.z': "C:/Users/Houcem/Desktop/AK/Other/Compressed",
    '.zip': "C:/Users/Houcem/Desktop/AK/Other/Compressed",
#Disc
    '.bin': "C:/Users/Houcem/Desktop/AK/Other/Disc",
    '.dmg': "C:/Users/Houcem/Desktop/AK/Other/Disc",
    '.iso': "C:/Users/Houcem/Desktop/AK/Other/Disc",
    '.toast': "C:/Users/Houcem/Desktop/AK/Other/Disc",
    '.vcd': "C:/Users/Houcem/Desktop/AK/Other/Disc",
#Data
    '.csv': "C:/Users/Houcem/Desktop/AK/Programming/Database",
    '.dat': "C:/Users/Houcem/Desktop/AK/Programming/Database",
    '.db': "C:/Users/Houcem/Desktop/AK/Programming/Database",
    '.dbf': "C:/Users/Houcem/Desktop/AK/Programming/Database",
    '.log': "C:/Users/Houcem/Desktop/AK/Programming/Database",
    '.mdb': "C:/Users/Houcem/Desktop/AK/Programming/Database",
    '.sav': "C:/Users/Houcem/Desktop/AK/Programming/Database",
    '.sql': "C:/Users/Houcem/Desktop/AK/Programming/Database",
    '.tar': "C:/Users/Houcem/Desktop/AK/Programming/Database",
    '.xml': "C:/Users/Houcem/Desktop/AK/Programming/Database",
    '.json': "C:/Users/Houcem/Desktop/AK/Programming/Database",
#Executables
    '.apk': "C:/Users/Houcem/Desktop/AK/Other/Executables",
    '.bat': "C:/Users/Houcem/Desktop/AK/Other/Executables",
    '.com': "C:/Users/Houcem/Desktop/AK/Other/Executables",
    '.exe': "C:/Users/Houcem/Desktop/AK/Other/Executables",
    '.gadget': "C:/Users/Houcem/Desktop/AK/Other/Executables",
    '.jar': "C:/Users/Houcem/Desktop/AK/Other/Executables",
    '.wsf': "C:/Users/Houcem/Desktop/AK/Other/Executables",
#Fonts
    '.fnt': "C:/Users/Houcem/Desktop/AK/Other/Fonts",
    '.fon': "C:/Users/Houcem/Desktop/AK/Other/Fonts",
    '.otf': "C:/Users/Houcem/Desktop/AK/Other/Fonts",
    '.ttf': "C:/Users/Houcem/Desktop/AK/Other/Fonts",
#Presentations
    '.key': "C:/Users/Houcem/Desktop/AK/Text/Presentations",
    '.odp': "C:/Users/Houcem/Desktop/AK/Text/Presentations",
    '.pps': "C:/Users/Houcem/Desktop/AK/Text/Presentations",
    '.ppt': "C:/Users/Houcem/Desktop/AK/Text/Presentations",
    '.pptx': "C:/Users/Houcem/Desktop/AK/Text/Presentations",
#Programming
    '.c': "C:/Users/Houcem/Desktop/AK/Programming/C&C++",
    '.class': "C:/Users/Houcem/Desktop/AK/Programming/Java",
    '.dart': "C:/Users/Houcem/Desktop/AK/Programming/Dart",
    '.py': "C:/Users/Houcem/Desktop/AK/Programming/Python",
    '.sh': "C:/Users/Houcem/Desktop/AK/Programming/Shell",
    '.swift': "C:/Users/Houcem/Desktop/AK/Programming/Swift",
    '.html': "C:/Users/Houcem/Desktop/AK/Programming/C&C++",
    '.h': "C:/Users/Houcem/Desktop/AK/Programming/C&C++",
#Spreadsheets
    '.ods' : "C:/Users/Houcem/Desktop/AK/Text/Microsoft/Excel",
    '.xlr' : "C:/Users/Houcem/Desktop/AK/Text/Microsoft/Excel",
    '.xls' : "C:/Users/Houcem/Desktop/AK/Text/Microsoft/Excel",
    '.xlsx' : "C:/Users/Houcem/Desktop/AK/Text/Microsoft/Excel",
#System
    '.bak' : "C:/Users/Houcem/Desktop/AK/System",
    '.cab' : "C:/Users/Houcem/Desktop/AK/System",
    '.cfg' : "C:/Users/Houcem/Desktop/AK/System",
    '.cpl' : "C:/Users/Houcem/Desktop/AK/System",
    '.cur' : "C:/Users/Houcem/Desktop/AK/System",
    '.dll' : "C:/Users/Houcem/Desktop/AK/System",
    '.dmp' : "C:/Users/Houcem/Desktop/AK/System",
    '.drv' : "C:/Users/Houcem/Desktop/AK/System",
    '.icns' : "C:/Users/Houcem/Desktop/AK/System",
    '.ico' : "C:/Users/Houcem/Desktop/AK/System",
    '.ini' : "C:/Users/Houcem/Desktop/AK/System",
    '.lnk' : "C:/Users/Houcem/Desktop/AK/System",
    '.msi' : "C:/Users/Houcem/Desktop/AK/System",
    '.sys' : "C:/Users/Houcem/Desktop/AK/System",
    '.tmp' : "C:/Users/Houcem/Desktop/AK/System",
}

folder_to_track = 'C:/Users/Houcem/Desktop'
folder_destination = 'C:/Users/Houcem/Desktop/AK'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()