import binpacking

# 4x cert
dashboards_suite_dict = {
    "ArcGIS org Integration": 31,  # (suite)
    "Home Page": 7,  # (Suite)
    "Dashboard Level Settings": 30,  # (Suite)
    "Layout": 17,  # (Suite)
    "Details Element": 21,  # 7 (Common-all) + 4 (common details-identify) + 10 (suite)
    "Embedded Content": 20,  # 7 (Common-all) + 13 (suite)
    "Gauge": 47,  # 19 (Common-all) + 28 (Suite)
    "Indicator": 47,  # 4 (Common-all) + 43 (suite)
    "Legend Element": 11,  # 3 (Common-all) + 6 (common legend) + 2 (suite)
    "List": 30,  # 8 (Common-all) + 15 (actions) + 7 (suite)
    "Map": 52,  # 2 (Common-all) + 4 (common details-identify) + 14 (actions) + 31 (suite)
    "Pie Chart": 104,  # 22 (Common-all) + 17 (actions) + 65 (Pie Chart)
    "Rich Text Element": 4,  # 2 (Common-all) + 2 (suite)
    "Selectors": 72,  # 21 (Common-all) + 29 (actions) + 22 (suite)
    "Serial Chart": 140,  # 29 (Common-all) + 25 (Actions) + 86 (suite)
    "Data Sources": 25,  # (suite)
    "URL Parameters": 22,  # (actions)
    "Side Panel": 3,  # 3 (suite)
    # "L10N_I8N":
    "Arcade": 7,  # 7 (suite)
}

# 3x cert
classic_suite_dict = {
    "ArcGIS org Integration": 47,  # (suite)
    "Home Page": 4,  # (suite)
    "Dashboard Level Settings": 15,
    "Data Sources": 5,  # (suite)
    "Indicator": 50,  # 7 (common) + 41 (suite)
    "Rich Text Element": 4,  # 2 (common) + 2 (suite)
    "Pie Chart": 8,  # (common)
    "Details Element": 5,  # (common)
    "Embedded Content": 5,  # (Common)
    "ArcGIS Online New Features": 0,
    "Side Panel": 3,  # (suite)
    "Serial Chart": 35,  # 18 (suite) + 17 (Common)
    "Gauge": 10,  # Common
    "Legend Element": 2,  # common
    "List": 5,  # (common)
    "Map": 5,  # 3 (common actions) + 2 (Common)
    "Selectors": 17,  # (common)
    "One Offs": 0,
}

EMPLOYEES = 3
suite_dict = classic_suite_dict
total_test_cases = sum(suite_dict.values())
bins = binpacking.to_constant_bin_number(suite_dict, EMPLOYEES)

print(f"There are a total of {total_test_cases} test cases")
for index, employee in enumerate(bins):
    print(f"\n Bucket {index} has {sum(employee.values())} tests")
    print(employee)
    # print(employee.keys())
