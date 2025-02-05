class Andhra:
    def __init__(self, capital) -> None:
        self.capital=capital
    def fetch_capital(self):
        print(f'I"m from fetch capital{self.capital}')
class TG:
    def __init__(self, capital) -> None:
        self.capital=capital
    def fetch_capital(self):
        print(f'I"m from fetch capital{self.capital}')

def main():
    A=Andhra("Amaravathi")
    T=TG("hyderabad")
    print(id(A.fetch_capital()))
    print(id(T.fetch_capital()))
    # for each in [A,T]:
    #     print(id(each))
    #     temp=each.fetch_capital()
    #     print(id(temp))
if __name__=="__main__":
    main()