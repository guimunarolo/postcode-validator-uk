import re

UK_POSTCODE_VALIDATION_REGEX = re.compile(
    r"^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO"
    r" ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4,5}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"
)
UK_POSTCODE_AREA_REGEX = re.compile(r"^[A-Z]{1,2}")
UK_POSTCODE_DISTRICT_REGEX = re.compile(r"[0-9]{1,2}[A-Z]?$")
UK_POSTCODE_SECTOR_REGEX = re.compile(r"^[0-9]")
UK_POSTCODE_UNIT_REGEX = re.compile(r"[A-Z0-9]{2}$")
