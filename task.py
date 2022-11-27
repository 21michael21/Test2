import pandas
class Downloader:

    def __init__(self,datapath:str) -> None:
        self.datapath = datapath
        self.file = pandas.read_csv(datapath,sep= ";", encoding="1251")



    def info(self) -> dict:
        self.file.info(memory_usage=False)
        d = dict()
        d['Количество столбцов'] = len(self.file.columns)
        d['Количество строк'] = len(self.file)
        d['Заголовки'] = list(self.file)
        return d



pays = Downloader(r'E:\Data\pays.csv')
pays.info()
        