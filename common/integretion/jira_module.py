# coding=utf-8

from jira import JIRA
from jira import JIRAError


class Jira_Util:
    def __init__(self):
        try:
            self.con = JIRA('http://jira.hualala.com', basic_auth=('zhangpeizhe', 'zpzjsj@126.com'))
            # print type(con.issue('YYZX-144', fields='summary,description，comment'))
        except JIRAError as e:
            print e.status_code
            print e.text

    def get_issue_summary(self, issueId):
        ret = self.con.issue(issueId)
        issue_summary = ret.fields.summary
        return issue_summary
        # description = res.fields.description


if __name__ == '__main__':
    print Jira_Util().get_issue_summary('YYZX-144')
    print Jira_Util().get_issue_summary('YYZX-145')
