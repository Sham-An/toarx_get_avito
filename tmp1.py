#
import os
from pathlib import Path


def main():
    path1 = "C:/Users/sselt/Documents/blog_demo/"
    #os.path.isdir(path1)
    #os.path.isfile(path1)
    #os.path.getsize(path1)

    path1: Path = Path("C:/Users/sselt/Documents/blog_demo/")
    print(path1.is_dir())
    path1.is_file()
    #path1.stat().st_size

    path = 'D:\home\Riot Games\VALORANT\live\VALORANT.exe'
    print(os.path.basename(path).split('\\')[-1])

    filename: Path = Path("some_file.txt")
    'C:\\Users\\Solmark\\Desktop\\СЕРИИ\\Омепразол 30\\бланк1.VDF'
    # hier path mit überflüssigem Trenner am Schluss
    path: Path = Path("C:/Users/sselt/Documents/blog_demo/")

    # hier path mit doppeltem Trenner
    path: Path = Path("C:/Users/sselt/Documents/blog_demo//")
    # hier path völlig durcheinander
    path: Path = Path("C:\\Users\\sselt\\Documents\\blog_demo")  # hier ein wilder Mix
    #path: Path = Path('C:\Users\Solmark\Desktop\СЕРИИ\Омепразол 30\бланк1.VDF')
    # alle Varianten führen zum selben Ergebnis
    print(path / filename)

    filesurvey = []
    for row in os.walk(path1):  # row beinhaltet jeweils einen Ordnerinhalt
        for filename in row[2]:  # row[2] ist ein tupel aus Dateinamen
            full_path: Path = Path(row[0]) / Path(filename)  # row[0] ist der Ordnerpfad
            #filesurvey.append([path1, filename, full_path.stat().st_mtime, full_path.stat().st_size])


if __name__ == '__main__':
    main()
