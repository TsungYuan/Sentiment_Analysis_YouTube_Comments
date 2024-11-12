import pandas as pd

def saveToCsv(df, filename):
    """
    Save a DataFrame to a CSV file.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        filename: (str): The path and name of the CSV file to save.
    """
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


def saveToJson(df, filename):
    """
    Save a DataFrame to a JSON file.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        filename: (str): The path and name of the JSON file to save.
    """
    df.to_json(filename, orient="records", lines=True)
    print(f"Data saved to {filename}")