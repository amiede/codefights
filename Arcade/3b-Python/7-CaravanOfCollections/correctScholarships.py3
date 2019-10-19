# https://app.codesignal.com/arcade/python-arcade/caravan-of-collections/f3dcuz6yoKv9yorzh
def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents) <= set(scholarships) < set(allStudents)