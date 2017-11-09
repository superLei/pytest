# coding = utf-8
import sys

sys.path.append("../")
import setting

import testlink


class TestLink_Module:
    def __init__(self):
        url = setting.TESTLINK_CONFIG["url"]
        key = setting.TESTLINK_CONFIG["key"]
        self.tlc = testlink.TestlinkAPIClient(url, key)
        # print tlc.connectionInfo()

    def get_suite(self):
        projects = self.tlc.getProjects()
        top_suites = self.tlc.getFirstLevelTestSuitesForTestProject(projects[0]["id"])
        for suite in top_suites:
            print suite["id"], suite["name"]
            # print projects

    def get_case(self, case_name):
        case = self.tlc.getTestCaseIDByName(case_name)
        caseID = case[0]["id"]
        case = self.tlc.getTestCase(caseID)
        input = case[0]['steps'][0]['actions']
        expect = case[0]['steps'][0]['expected_results']
        return input, expect


if __name__ == '__main__':
    TestLink_Module().get_suite()
    print TestLink_Module().get_case("test")
