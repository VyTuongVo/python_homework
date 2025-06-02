import pandas as pd

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)
    
    def print_with_headers(self):
        steps = 10 
        length = len(self)

        for i in range( 0, length, steps):
            end = min(i + steps, length)
            print(self.iloc[i:end])


if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")

    dfp.print_with_headers()