def export_csv(df, filename="resultado.csv"):

    df.to_csv(filename, index=False)

    return filename
