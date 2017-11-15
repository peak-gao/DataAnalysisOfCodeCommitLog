"""
load commit log
"""
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
            commitLog['year'] = dateValue.year
    return commitLog


def parseSummary(readLines):
    commitSummary = ''
    for line in readLines:
        tokens = parseLine(line)
        if tokens[0] == 'summary':
            commitSummary = tokens[1]
            break
    return commitSummary


def loadCommitLogs():
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


def loadSummaries():
    lines = open('./commitLogs.log').readlines()
    readLines = []
    commitSummaries = []
    for line in lines:
        if (line != '\n'):
            readLines.append(line)
        else:
            commitSummaries.append(parseSummary(readLines))
            readLines = []
    return "".join(commitSummaries)


if __name__ == "__main__":
    print loadSummaries()
