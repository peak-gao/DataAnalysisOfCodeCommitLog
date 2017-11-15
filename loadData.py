from dateutil import parser
import calendar

def parseLine(line):
    splitString = ':   '
    return line.split(splitString, 1)

def parseLines(readLines):
    commitLog = {}
    for line in readLines:
        tokens = parseLine(line)
        commitLog[tokens[0]] = tokens[1].strip()
        if tokens[0] == 'date':
            dateValue = parser.parse(tokens[1])
            commitLog['date'] = dateValue.strftime('%Y-%m-%d')
            commitLog['weekday'] = calendar.day_abbr[dateValue.weekday()]
            commitLog['month'] = dateValue.month
    return commitLog

def load():
    lines = open('./commitLogs.log').readlines()
    readLines = []
    commitLogs = []
    for line in lines:
        if (line != '\n'):
            readLines.append(line)
        else:
            commitLogs.append(parseLines(readLines))
            readLines = []
    return commitLogs
    
if __name__ == "__main__":
    print load()[-10:]
