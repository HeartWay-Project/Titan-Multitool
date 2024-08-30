from Config.Util import *
from Config.Config import *
try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except Exception as e:
   ErrorModule(e)
   

Title("Number Info (Lookup)")

try:
    phone_number = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Phone Number -> {color.RESET}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if phonenumbers.is_valid_number(parsed_number):
            if phone_number.startswith("+"):
                country_code = "+" + phone_number[1:3] 
            else:
                country_code = "None"
            operator = carrier.name_for_number(parsed_number, "fr")
            type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
            timezones = timezone.time_zones_for_number(parsed_number)
            timezone_info = timezones[0] if timezones else None
            country = phonenumbers.region_code_for_number(parsed_number)
            region = geocoder.description_for_number(parsed_number, "fr")
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
            status = "Valid"
        else:
            formatted_number = "None"
            region = "None"
            country = "None"
            operator = "None"
            type_number = "None"
            timezone_info = "None"
            country_code = "None"
            status = "Invalid"


        print(f"""
    {INFO_ADD} Phone        : {secondary}{phone_number}{invalid}
    {INFO_ADD} Formatted    : {secondary}{formatted_number}{invalid}
    {INFO_ADD} Status       : {secondary}{status}{invalid}
    {INFO_ADD} Country Code : {secondary}{country_code}{invalid}
    {INFO_ADD} Country      : {secondary}{country}{invalid}
    {INFO_ADD} Region       : {secondary}{region}{invalid}
    {INFO_ADD} Timezone     : {secondary}{timezone_info}{invalid}
    {INFO_ADD} Operator     : {secondary}{operator}{invalid}
    {INFO_ADD} Type Number  : {secondary}{type_number}{invalid}
    """)
        Continue()
        Reset()
    except:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Invalid Format ! [Ex: {secondary}+442012345678{invalid} or {secondary}+33623456789{invalid}]")
        Continue()
        Reset()
except Exception as e:
    Error(e)