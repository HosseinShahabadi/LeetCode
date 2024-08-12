import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return [len(players.index), len(players.columns)]
