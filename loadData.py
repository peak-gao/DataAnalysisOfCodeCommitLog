from dateutil import parser
import calendar


def getValue(line):
    splitString = ':   '
    return line.split(splitString)[-1].strip()


def createDictionary(changeset, user, date, summary):
    dateValue = parser.parse(date)
    return {
        'changeset': changeset,
        'user': user,
        'date': dateValue.strftime('%Y-%m-%d'),
        'summary': summary,
        'weekday': calendar.day_abbr[dateValue.weekday()]
    }


def load():
    lines = open('./hg_201711.log').readlines()
    length = len(lines)
    commits = []

    #the first 5 lines are tip log
    tipLines = lines[0:5]
    changeset = getValue(tipLines[0])
    user = getValue(tipLines[2])
    date = getValue(tipLines[3])
    summary = getValue(tipLines[4])
    commits.append(createDictionary(changeset, user, date, summary))

    for i in range(6, length, 5):
        changeset = getValue(lines[i])
        user = getValue(lines[i + 1])
        date = getValue(lines[i + 2])
        summary = getValue(lines[i + 3])
        commits.append(createDictionary(changeset, user, date, summary))

    return commits


if __name__ == "__main__":
    print load()
