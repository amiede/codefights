"https://app.codesignal.com/challenge/FWYRbc5nQWCBgEtyT"
Object subclass: centuryFromYear [
    year: year [
        ^ (year / 100.0) asFloat ceiling.
    ]
]