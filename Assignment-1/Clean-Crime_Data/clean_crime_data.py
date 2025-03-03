import pandas as pd

# Define focus crime categories
focuscrimes = {
    "WEAPON LAWS", "PROSTITUTION", "ROBBERY", "BURGLARY", "ASSAULT", 
    "DRUNKENNESS", "DRUG/NARCOTIC", "TRESPASS", "LARCENY/THEFT", 
    "VANDALISM", "VEHICLE THEFT", "STOLEN PROPERTY", "DISORDERLY CONDUCT", 
    "DRIVING UNDER THE INFLUENCE"
}

# Define crime category renaming dictionary
crime_rename_mapping = {
    "MOTOR VEHICLE THEFT": "VEHICLE THEFT",
    "MOTOR VEHICLE THEFT?": "VEHICLE THEFT",
    "LARCENY THEFT": "LARCENY/THEFT",
    "DRUG VIOLATION": "DRUG/NARCOTIC",
    "DRUG OFFENSE": "DRUG/NARCOTIC",
    "MALICIOUS MISCHIEF": "VANDALISM",
    "BURGLARY RESIDENTIAL": "BURGLARY",
    "BURGLARY COMMERCIAL": "BURGLARY",
    "BATTERY": "ASSAULT",
    "PROPERTY DAMAGE": "VANDALISM",
    "WEAPONS OFFENSE": "WEAPON LAWS",
    "WEAPONS OFFENCE": "WEAPON LAWS",
    "WEAPONS CARRYING ETC": "WEAPON LAWS",
    "SEX OFFENSES, FORCIBLE": "ASSAULT",
    "SEX OFFENSES, NON FORCIBLE": "PROSTITUTION",
    "HUMAN TRAFFICKING, COMMERCIAL SEX ACTS": "ASSAULT",
    "HUMAN TRAFFICKING (A), COMMERCIAL SEX ACTS": "ASSAULT",
    "HUMAN TRAFFICKING (B), INVOLUNTARY SERVITUDE": "ASSAULT",
    "prostitution": "PROSTITUTION",
}

# Function to clean and filter crime data
def clean_crime_data(df):
    """Cleans and standardizes crime category names and police district names in the dataset."""
    
    # Convert "Incident Date" to datetime if it's not already
    if not pd.api.types.is_datetime64_any_dtype(df["Incident Date"]):
        df["Incident Date"] = pd.to_datetime(df["Incident Date"])

    # Rename crime categories based on mapping
    df["Incident Category"] = df["Incident Category"].replace(crime_rename_mapping)

    # Standardize Police District to UPPERCASE before filtering
    df["Police District"] = df["Police District"].str.strip().str.upper()

    # Filter dataset to only include focus crimes
    df_filtered = df[df["Incident Category"].isin(focuscrimes)].copy()

    return df_filtered
