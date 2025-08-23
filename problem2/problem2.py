

def date_format(date:str) -> str:
    date_parts = date.split('/')
    new_date=f"{date_parts[2]}-{date_parts[0]}-{date_parts[1]}"
    return new_date